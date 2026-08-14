#!/usr/bin/env python3
import os
import re
import requests
from pathlib import Path
from urllib.parse import unquote
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv

# Load environment variables
load_dotenv()

# Configuration
BASEROW_API_TOKEN = os.getenv('BASEROW_API_TOKEN')
BASEROW_TABLE_ID = os.getenv('BASEROW_TABLE_ID')
BASEROW_API_URL = f"https://api.baserow.io/api/database/rows/table/{BASEROW_TABLE_ID}/"

if not BASEROW_API_TOKEN or not BASEROW_TABLE_ID:
    raise ValueError("Missing BASEROW_API_TOKEN or BASEROW_TABLE_ID in .env file")

# Setup paths
project_root = Path(__file__).parent.parent
templates_dir = project_root / 'templates'
docs_dir = project_root / 'docs'
mic_pages_dir = docs_dir / 'microscopes' / 'mic_pages'
photos_dir = docs_dir / 'microscopes' / 'images' / 'baserow'

# Photos are downloaded from Baserow and committed, so that visitors of the
# site never make a request to Baserow. Names of downloaded photos are
# collected here so unused ones can be cleaned up afterwards.
downloaded_photos = set()
SAFE_FILENAME = re.compile(r'^[A-Za-z0-9][A-Za-z0-9._-]*\.[A-Za-z0-9]+$')

# Setup Jinja2
jinja_env = Environment(loader=FileSystemLoader(str(templates_dir)))

def write_doc(relpath, content):
    """Write a generated page into the docs directory"""
    path = docs_dir / relpath
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(content, encoding='utf-8')

def localize_photo(url):
    """Download a microscope photo from Baserow and return a path relative
    to the generated microscope page.

    Baserow file names contain a hash of the file contents, so a file that is
    already present is always up to date and is never downloaded again. A
    changed photo arrives under a new name and the old one is cleaned up by
    prune_photos().
    """
    if not url or url == 'N/A' or not url.startswith('http'):
        return None

    filename = unquote(url.split('?')[0].rsplit('/', 1)[-1])
    if not SAFE_FILENAME.match(filename):
        print(f"  ! Skipping photo with unexpected file name: {filename}")
        return None

    target = photos_dir / filename
    if not target.exists():
        try:
            response = requests.get(url, timeout=30)
            response.raise_for_status()
        except requests.RequestException as e:
            print(f"  ! Could not download {filename}: {e}")
            return None
        photos_dir.mkdir(parents=True, exist_ok=True)
        target.write_bytes(response.content)
        print(f"  ↓ downloaded {filename}")

    downloaded_photos.add(filename)
    return f"../images/baserow/{filename}"

def prune_photos():
    """Remove downloaded photos that are no longer used by any microscope"""
    if not photos_dir.exists():
        return
    for photo in photos_dir.iterdir():
        if photo.is_file() and photo.name not in downloaded_photos:
            photo.unlink()
            print(f"✗ removed unused photo {photo.name}")

def fetch_microscopes():
    """Fetch all microscopes from Baserow"""
    headers = {
        'Authorization': f'Token {BASEROW_API_TOKEN}'
    }
    response = requests.get(BASEROW_API_URL, headers=headers)
    response.raise_for_status()
    return response.json()['results']

def extract_value(field_data, is_file=False):
    """Extract value from Baserow field (handles nested objects and arrays)"""
    if field_data is None:
        return 'N/A'
    
    # Handle file fields specially
    if is_file:
        if isinstance(field_data, list) and len(field_data) > 0:
            # Return the URL of the first file
            return field_data[0].get('url', 'N/A')
        return 'N/A'
    
    if isinstance(field_data, dict):
        return field_data.get('value', 'N/A')
    if isinstance(field_data, list):
        if len(field_data) == 0:
            return 'N/A'
        # Join multiple values with comma
        values = [item.get('value', '') for item in field_data if isinstance(item, dict)]
        return ', '.join(values) if values else 'N/A'
    return str(field_data)

def extract_boolean(field_data):
    """Extract boolean value from Baserow field"""
    if field_data is None:
        return None
    if isinstance(field_data, bool):
        return field_data
    # Sometimes booleans come as strings
    if isinstance(field_data, str):
        if field_data.lower() in ('true', '1', 'yes'):
            return True
        if field_data.lower() in ('false', '0', 'no'):
            return False
    return None

def wavelength_to_color(nm):
    """Convert a wavelength in nm to an approximate RGB hex color."""
    try:
        nm = float(nm)
    except (ValueError, TypeError):
        return None
    if nm < 380 or nm > 780:
        return None
    # peicewise linear approximation of the visible spectrum
    if nm < 440:
        r = -(nm - 440) / (440 - 380)
        g = 0.0
        b = 1.0
    elif nm < 490:
        r = 0.0
        g = (nm - 440) / (490 - 440)
        b = 1.0
    elif nm < 510:
        r = 0.0
        g = 1.0
        b = -(nm - 510) / (510 - 490)
    elif nm < 580:
        r = (nm - 510) / (580 - 510)
        g = 1.0
        b = 0.0
    elif nm < 645:
        r = 1.0
        g = -(nm - 645) / (645 - 580)
        b = 0.0
    else:
        r = 1.0
        g = 0.0
        b = 0.0
    # intensity adjustment at the edges
    if nm < 420:
        factor = 0.3 + 0.7 * (nm - 380) / (420 - 380)
    elif nm > 700:
        factor = 0.3 + 0.7 * (780 - nm) / (780 - 700)
    else:
        factor = 1.0
    r = int(round(255 * (r * factor) ** 0.8))
    g = int(round(255 * (g * factor) ** 0.8))
    b = int(round(255 * (b * factor) ** 0.8))
    return f"#{r:02x}{g:02x}{b:02x}"


def parse_illumination(raw):
    """Parse illumination string into list of {label, color, text_color} dicts."""
    if not raw or raw == 'N/A':
        return []
    import re
    items = [s.strip() for s in raw.split(',')]
    result = []
    for item in items:
        # Try to extract a leading number (wavelength)
        m = re.match(r'^(\d{3,4})', item)
        if m:
            nm = int(m.group(1))
            bg = wavelength_to_color(nm)
            if bg:
                # choose black or white text based on luminance
                r, g, b = int(bg[1:3], 16), int(bg[3:5], 16), int(bg[5:7], 16)
                lum = 0.299 * r + 0.587 * g + 0.114 * b
                text_color = '#000' if lum > 140 else '#fff'
                result.append({'label': item, 'color': bg, 'text_color': text_color})
            else:
                result.append({'label': item, 'color': None, 'text_color': None})
        else:
            result.append({'label': item, 'color': None, 'text_color': None})
    return result


def split_list(raw):
    """Split a comma-separated string into a list of trimmed items."""
    if not raw or raw == 'N/A':
        return []
    return [s.strip() for s in raw.split(',') if s.strip()]


def sanitize_filename(name):
    """Convert name to valid filename"""
    if not name or name == 'N/A':
        return None
    filename = name.lower().replace(' ', '-')
    filename = ''.join(c for c in filename if c.isalnum() or c in '-_')
    return f"{filename}.md"

def get_category(microscope_type):
    """Determine category for a microscope type"""
    categories = [
        'Confocal',
        'Widefield',
        'Stereo',
        'Electron Microscope',
        'Slide Scanner',
        'High-Content',
        'Lightsheet',
    ]
    
    for category in categories:
        if category.lower() in microscope_type.lower():
            return category
    
    return 'Other'

def generate_page(microscope, related_microscopes=None):
    """Generate a single microscope page"""
    template = jinja_env.get_template('microscope.md.jinja2')
    
    if related_microscopes is None:
        related_microscopes = []
    
    # Extract values using field IDs
    name = extract_value(microscope.get('field_5930781'))
    institute = extract_value(microscope.get('field_5930780'))
    location = extract_value(microscope.get('field_5930782'))
    specialists = extract_value(microscope.get('field_5930821'))
    microscope_type = extract_value(microscope.get('field_5930783'))
    booking_link_url = extract_value(microscope.get('field_6299627'))
    inverted = extract_boolean(microscope.get('field_5930784'))
    temperature_control = extract_boolean(microscope.get('field_5930785'))
    co2_control = extract_boolean(microscope.get('field_5930786'))
    o2_control = extract_boolean(microscope.get('field_5930787'))
    automated_stage = extract_boolean(microscope.get('field_5930788'))
    detectors = extract_value(microscope.get('field_5930789'))
    illumination = extract_value(microscope.get('field_5931199'))
    objectives = extract_value(microscope.get('field_5995733'))
    emission_filters = extract_value(microscope.get('field_5930791'))
    applications = extract_value(microscope.get('field_5930806'))
    samples = extract_value(microscope.get('field_5930818'))
    photo = extract_value(microscope.get('field_5998355'), is_file=True)
    video_url = extract_value(microscope.get('field_6299632'))
    
    # Skip if no name
    if not name or name == 'N/A' or name == '':
        return None, None
    
    context = {
        'name': name,
        'microscope_type': microscope_type,
        'institute': institute,
        'specialists': specialists,
        'booking_link_url': booking_link_url if booking_link_url != 'N/A' else None,
        'location': location if location else 'N/A',
        'inverted': inverted,
        'temperature_control': temperature_control,
        'co2_control': co2_control,
        'o2_control': o2_control,
        'automated_stage': automated_stage,
        'detectors': detectors,
        'illumination': illumination,
        'illumination_list': parse_illumination(illumination),
        'objectives': objectives,
        'objectives_list': split_list(objectives),
        'emission_filters': emission_filters,
        'emission_filters_list': split_list(emission_filters),
        'applications': applications,
        'samples': samples,
        'photo': localize_photo(photo),
        'video_url': video_url if video_url != 'N/A' else None,
        'related_microscopes': related_microscopes,
        'category': get_category(microscope_type),
    }
    
    content = template.render(**context)
    filename = sanitize_filename(context['name'])
    
    if not filename:
        return None, None
    
    write_doc(f"microscopes/mic_pages/{filename}", content)
    
    print(f"✓ {context['name']}")
    return filename, context

def generate_index(microscopes):
    """Generate overview page with compact card grid"""
    template = jinja_env.get_template('microscope_overview.md.jinja2')

    # Define categories and their order
    category_order = [
        'Confocal', 'Widefield', 'Stereo', 'Electron',
        'Slide Scanner', 'High-Content', 'Lightsheet', 'Other'
    ]
    category_items = {cat: [] for cat in category_order}

    # Group microscopes by type
    for filename, data in microscopes:
        mtype = data['microscope_type']
        categorized = False
        for category in category_order:
            if category.lower() in mtype.lower():
                category_items[category].append((filename, data))
                categorized = True
                break
        if not categorized:
            category_items['Other'].append((filename, data))

    # Build ordered dict: category -> institute -> [{name, slug, location}]
    from collections import OrderedDict
    categories = OrderedDict()
    for category in category_order:
        items = category_items[category]
        if not items:
            continue

        by_institute = OrderedDict()
        for filename, data in sorted(items, key=lambda x: (x[1]['institute'], x[1]['name'])):
            institute = data['institute']
            if institute not in by_institute:
                by_institute[institute] = []
            slug = filename.replace('.md', '') if filename else ''
            by_institute[institute].append({
                'name': data['name'],
                'slug': slug,
                'location': data['location'],
            })
        categories[category] = by_institute

    content = template.render(categories=categories)

    write_doc('microscopes/microscope_overview.md', content)

    print(f"✓ Generated index")

def generate_interactive_table(all_microscopes):
    """Generate an interactive, filterable table page"""
    template = jinja_env.get_template('microscope_table.md.jinja2')

    # Collect unique types and institutes for filter chips
    types = sorted(set(mic['category'] for mic in all_microscopes))
    institutes = sorted(set(mic['institute'] for mic in all_microscopes if mic['institute'] != 'N/A'))

    # Build microscope list with all needed fields
    table_data = []
    for mic in sorted(all_microscopes, key=lambda x: x['name']):
        applications = extract_value(mic['raw_data'].get('field_5930806'))
        slug = mic['filename'].replace('.md', '') if mic['filename'] else ''
        table_data.append({
            'name': mic['name'],
            'slug': slug,
            'institute': mic['institute'],
            'location': mic['location'],
            'microscope_type': mic['category'],
            'applications': applications,
        })

    content = template.render(
        microscopes=table_data,
        types=types,
        institutes=institutes,
    )

    write_doc('microscopes/index.md', content)

    print(f"✓ Generated interactive table (index)")

# Main execution
try:
    print("Fetching microscopes from Baserow...")
    microscopes_data = fetch_microscopes()
    print(f"Found {len(microscopes_data)} microscopes")
    
    # First pass: extract all microscope data
    print("\nExtracting microscope data...")
    all_microscopes = []
    for microscope in microscopes_data:
        name = extract_value(microscope.get('field_5930781'))
        if not name or name == 'N/A' or name == '':
            continue
        
        microscope_type = extract_value(microscope.get('field_5930783'))
        institute = extract_value(microscope.get('field_5930780'))
        location = extract_value(microscope.get('field_5930782'))
        
        all_microscopes.append({
            'name': name,
            'filename': sanitize_filename(name),
            'microscope_type': microscope_type,
            'category': get_category(microscope_type),
            'institute': institute,
            'location': location,
            'raw_data': microscope
        })
    
    # Group by category for navigation
    by_category = {}
    for mic in all_microscopes:
        category = mic['category']
        if category not in by_category:
            by_category[category] = []
        by_category[category].append(mic)
    
    # Second pass: generate pages with navigation
    print("\nGenerating individual microscope pages...")
    generated = []
    for mic_data in all_microscopes:
        # Get related microscopes in same category
        related = [
            {
                'name': m['name'],
                'filename': m['filename'],
                'institute': m['institute'],
                'location': m['location']
            }
            for m in by_category[mic_data['category']]
            if m['name'] != mic_data['name']
        ]
        
        result = generate_page(mic_data['raw_data'], related_microscopes=related)
        if result[0]:
            generated.append(result)

    print(f"\nGenerated {len(generated)} microscope pages")

    # Remove pages of microscopes that are no longer in Baserow
    current = {filename for filename, _ in generated}
    for stale in mic_pages_dir.glob('*.md'):
        if stale.name not in current:
            stale.unlink()
            print(f"✗ removed stale page {stale.name}")

    prune_photos()

    print("\nGenerating overview page...")
    generate_index(generated)

    print("\nGenerating interactive table...")
    generate_interactive_table(all_microscopes)

    print("\n✓ All done!")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    raise