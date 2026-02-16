#!/usr/bin/env python3
import os
import requests
from pathlib import Path
from jinja2 import Environment, FileSystemLoader
from dotenv import load_dotenv
import mkdocs_gen_files

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

# Setup Jinja2
jinja_env = Environment(loader=FileSystemLoader(str(templates_dir)))

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
        'photo': photo if photo != 'N/A' else None,
        'video_url': video_url if video_url != 'N/A' else None,
        'related_microscopes': related_microscopes,
        'category': get_category(microscope_type),
    }
    
    content = template.render(**context)
    filename = sanitize_filename(context['name'])
    
    if not filename:
        return None, None
    
    # Use mkdocs_gen_files to write the file
    filepath = f"microscopes/mic_pages/{filename}"
    with mkdocs_gen_files.open(filepath, 'w') as f:
        f.write(content)
    
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

    with mkdocs_gen_files.open('microscopes/microscope_overview.md', 'w') as f:
        f.write(content)

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

    with mkdocs_gen_files.open('microscopes/index.md', 'w') as f:
        f.write(content)

    print(f"✓ Generated interactive table (index)")

# Main execution
try:
    print("Fetching microscopes from Baserow...")
    microscopes_data = fetch_microscopes()
    print(f"Found {len(microscopes_data)} microscopes")
    
    # Create navigation object
    nav = mkdocs_gen_files.Nav()
    
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
            
            # Add to navigation
            nav["Microscopes", mic_data['category'], mic_data['institute'], mic_data['name']] = f"microscopes/mic_pages/{mic_data['filename']}"
    
    print(f"\nGenerated {len(generated)} microscope pages")
    
    # Add overview page to navigation
    nav["Microscopes", "Overview"] = "microscopes/microscope_overview.md"
    
    print("\nGenerating overview page...")
    generate_index(generated)

    print("\nGenerating interactive table...")
    generate_interactive_table(all_microscopes)

    # Generate navigation file
    print("\nGenerating navigation...")
    with mkdocs_gen_files.open("microscopes/SUMMARY.md", "w") as nav_file:
        nav_file.write("---\nsearch:\n  exclude: true\n---\n\n")
        nav_file.writelines(nav.build_literate_nav())
    
    print("\n✓ All done!")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    raise