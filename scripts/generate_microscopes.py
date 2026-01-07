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
        'objectives': objectives,
        'emission_filters': emission_filters,
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
    """Generate overview page"""
    content = """---
search:
  exclude: true
---

# Microscope Overview

This page provides a complete list of all microscopes available across the Leiden Cell Observatory facilities.

---

"""
    
    # Define categories and their order
    categories = {
        'Confocal': [],
        'Widefield': [],
        'Stereo': [],
        'Electron': [],
        'Slide Scanner': [],
        'High-Content': [],
        'Lightsheet': [],
        'Other': []
    }
    
    # Group microscopes by type
    for filename, data in microscopes:
        mtype = data['microscope_type']
        categorized = False
        
        # Check which category this microscope belongs to
        for category in categories.keys():
            if category.lower() in mtype.lower():
                categories[category].append((filename, data))
                categorized = True
                break
        
        # If no category matches, put in 'Other'
        if not categorized:
            categories['Other'].append((filename, data))
    
    # Generate grid with all categories
    content += '<div class="grid cards" markdown>\n\n'
    
    for category, items in categories.items():
        if not items:
            continue
        
        content += f"-   **{category} Microscopes**\n\n"
        content += f"    ---\n\n"
        
        # Group by institute within each category
        by_institute = {}
        for filename, data in sorted(items, key=lambda x: (x[1]['institute'], x[1]['name'])):
            institute = data['institute']
            if institute not in by_institute:
                by_institute[institute] = []
            by_institute[institute].append((filename, data))
        
        # Output grouped by institute
        for institute, inst_items in sorted(by_institute.items()):
            content += f"    **{institute}**\n\n"
            
            for filename, data in inst_items:
                name = data['name']
                location = data['location']
                content += f"    - [{name}](microscopes/mic_pages/{filename}) ({location})\n"
            content += "\n"        
        content += "\n"
    
    content += '</div>\n\n'
    
    # Use mkdocs_gen_files to write the index
    with mkdocs_gen_files.open('microscope_overview.md', 'w') as f:
        f.write(content)
    
    print(f"✓ Generated index")

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
    nav["Microscopes", "Overview"] = "microscope_overview.md"
    
    print("\nGenerating overview page...")
    generate_index(generated)
    
    # Generate navigation file
    print("\nGenerating navigation...")
    with mkdocs_gen_files.open("microscopes/SUMMARY.md", "w") as nav_file:
        nav_file.write("---\nsearch:\n  exclude: true\n---\n\n")
        nav_file.writelines(nav.build_literate_nav())
    
    print("\n✓ All done!")
    
except Exception as e:
    print(f"\n✗ Error: {e}")
    raise