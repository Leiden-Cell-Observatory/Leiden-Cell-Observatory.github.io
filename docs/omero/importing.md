# Importing Data into OMERO

This section covers the general procedures for importing data into OMERO at the Leiden Cell Observatory.

## Overview

OMERO.insight is the primary tool for importing data. This client is:
- Pre-installed on all microscope PC's
- Available for download on computers (Windows, Mac, Linux) 
https://www.openmicroscopy.org/omero/downloads/

## Basic Import Workflow

1. **Prepare Your Data**
   - Organize files in a clear structure
   - Consider project/dataset organization
   - Prepare any metadata you want to include

2. **Launch OMERO.insight**
   - Connect to server: omero.services.universiteitleiden.nl
   - Login with ULCN credentials
   - Navigate to your group/project space

3. **Import Process**
   - Use File > Import or the import icon
   - Select files for import
   - Choose or create projects/datasets
   - Add any tags or annotations
   - Review and start import

## Data Organization

### Project Structure
OMERO uses a two-level organization system:
- Projects (top level)
- Datasets (within projects)

### Recommended Folder Structure

When preparing data for import:

```
✅ Recommended Structure:
Project folder (selected folder)
├── subfolder 1
│   └── image 1, etc.
└── subfolder 2
    └── image 1, etc.

❌ Avoid:
Project folder
└── subfolder 1
    ├── subfolder I (experiment 1)
    └── subfolder II (experiment 2)
```

!!! success "Planning Your Import"
    Before starting a large import:
    1. Plan your project/dataset structure
    2. Prepare metadata if needed
    3. Consider file type specific requirements

## Next Steps

- For specific file types, see [Microscope Files](importing/microscope-files.md)
- For high-content screening data, check [HCS Data](importing/hcs-data.md)
- To add metadata, refer to [Metadata Annotations](importing/metadata.md)