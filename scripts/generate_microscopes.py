#!/usr/bin/env python3
import os
import requests
from pathlib import Path
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
docs_dir = project_root / 'docs'
microscopes_dir = docs_dir / 'microscopes' / 'mic_pages'
templates_dir = project_root / 'templates'

# Create directories
microscopes_dir.mkdir(parents=True, exist_ok=True)

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

def extract_value(field_data):
    """Extract value from Baserow field (handles nested objects and arrays)"""
    if field_data is None:
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

def sanitize_filename(name):
    """Convert name to valid filename"""
    if not name or name == 'N/A':
        return None
    filename = name.lower().replace(' ', '-')
    filename = ''.join(c for c in filename if c.isalnum() or c in '-_')
    return f"{filename}.md"

def generate_page(microscope):
    """Generate a single microscope page"""
    template = jinja_env.get_template('microscope.md.jinja2')
    
    # Extract values using field IDs
    name = extract_value(microscope.get('field_5930781'))
    institute = extract_value(microscope.get('field_5930780'))
    location = extract_value(microscope.get('field_5930782'))
    microscope_type = extract_value(microscope.get('field_5930783'))
    
    # Skip if no name
    if not name or name == 'N/A' or name == '':
        return None, None
    
    context = {
        'name': name,
        'microscope_type': microscope_type,
        'institute': institute,
        'location': location if location else 'N/A'
    }
    
    content = template.render(**context)
    filename = sanitize_filename(context['name'])
    
    if not filename:
        return None, None
    
    filepath = microscopes_dir / filename
    
    with open(filepath, 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ {context['name']}")
    return filename, context

def generate_index(microscopes):
    """Generate overview page"""
    content = """# Microscope Overview

This page provides a complete list of all microscopes available across the Cell Observatory facilities.

!!! tip "Finding a Microscope"
    Use the institute sections below to find available equipment, or visit the dedicated pages:
    
    - [IBL Microscopes](iblmicroscopes.md)
    - [LACDR Microscopes](lacdrmicroscopes.md) 
    - [LIC Microscopes](licmicroscopes.md)

---

"""
    
    # Group by institute
    by_institute = {}
    for filename, data in microscopes:
        institute = data['institute']
        if institute not in by_institute:
            by_institute[institute] = []
        by_institute[institute].append((filename, data['name'], data['microscope_type']))
    
    for institute in sorted(by_institute.keys()):
        content += f"\n## {institute}\n\n"
        content += "| Microscope | Type |\n"
        content += "|------------|------|\n"
        
        for filename, name, mtype in sorted(by_institute[institute]):
            content += f"| [{name}](microscopes/mic_pages/{filename}) | {mtype} |\n"
        
        content += "\n"
    
    with open(docs_dir / 'microscope_overview.md', 'w', encoding='utf-8') as f:
        f.write(content)
    
    print(f"✓ Generated index")

# Main execution
if __name__ == '__main__':
    print("Fetching microscopes from Baserow...")
    microscopes = fetch_microscopes()
    print(f"Found {len(microscopes)} microscopes\n")
    
    # Clean old pages
    for file in microscopes_dir.glob('*.md'):
        file.unlink()
    
    # Generate pages
    generated = []
    for microscope in microscopes:
        result = generate_page(microscope)
        if result[0] is not None:  # Skip empty entries
            generated.append(result)
    
    # Generate index
    if generated:
        generate_index(generated)
    
    print(f"\n✓ Done! Generated {len(generated)} pages")