# OMERO.scripts

OMERO scripts allows to modify, organize your image data directly on OMERO. These scripts are run from OMERO.web.

[![alt text](scripts/scripts_menu.png){width=250px}]

In the menu you can find both the official scripts provided by OMERO (folder `omero`) and custom scripts from Leiden University (folder `user`).

## Official OMERO.scripts
The official documentation can be found at [omero-scripts.readthedocs.io](https://omero-scripts.readthedocs.io/en/stable/)

=== "Analysis"

    ### Kymograph
    Processes images with Line or PolyLine ROIs to create kymograph images showing spatial-temporal dynamics. Creates new OMERO images where each line ROI is transformed into a horizontal visualization of changes over time.

    ### Kymograph Analysis
    Analyzes lines drawn on kymograph images previously created by the Kymograph script. Designed as a follow-up analysis tool to extract quantitative measurements from kymograph visualizations.

    ### Plot Profile
    Extracts intensity profiles from images with Line or PolyLine ROIs and exports the data to CSV files. Measures pixel intensities along defined lines across selected channels and attaches results to the original images.

=== "Annotation"

    The annotation scripts can be useful for organizing image metadata by Key-Pair values on OMERO. A walktrough of how to use the different scripts can be found [here](https://omero-guides.readthedocs.io/en/latest/scripts/docs/walkthrough.html).   
       
    ### Convert KeyVal namespace
    Converts the namespace of key-value pair annotations on OMERO objects. Can update existing annotations to a new namespace or merge multiple namespaces into one, with options to preserve or remove original annotations. Namespaces are used to group annotations. By default annotations added via OMERO.web end up in `openmicroscopy.org/omero/client/mapAnnotation`, but if you need more organization using namespaces is a good idea. This script can help with that.

    ### Export to CSV
    Exports metadata (key-value pairs, tags, and ancestry information) from images, datasets, or projects to a CSV file. The generated CSV is attached to the source object for download. It is possible to modify the metadata in the CSV file and import again.

    ### Import from CSV
    Imports key-value pairs and tags from a CSV file to annotate OMERO objects. Matches CSV rows to objects by name or ID, and can create new tags if needed.

    ### Remove KeyVal
    Removes all key-value pair annotations associated with specified namespaces from OMERO objects. Can target specific namespaces or remove all annotations using wildcard ('*').

=== "Export"

    ### Batch Image Export
    Exports individual image planes (by channel, Z-slice, and timepoint) from multiple images and packages them in a ZIP file for download. Supports various formats (PNG, TIFF, OME-TIFF) with options for projection, grayscale, and zoom.

    ### Batch ROI Export
    Exports ROI intensity measurements and coordinates from selected images to a CSV file. Captures shape geometry (length, area) and pixel intensities for all ROIs, with physical dimension calculations.

=== "Figure"

    ### Movie ROI Figure
    Creates a figure showing zoomed regions defined by ROIs from multiple images, displayed as a movie sequence. Shows split-channel views and merged images for each ROI region across time points, with adjustable zoom and column layout.

    ### Figure to Pdf
    Script used by OMERO.figure to convert a figure to a PDF. Here can be manually used to convert a JSON describing the figure to a PDF.   

=== "Import"

    ### Populate Metadata
    Processes a CSV file to populate an OMERO.table with metadata, creating one row per Image, Well, or ROI. The table data is then displayed in OMERO clients for easy viewing and filtering. Supports the omero-metadata CSV format specification.  
    
    !!! warning
        This script uses an outdated metadata plugin, might not work as expected.

=== "Utility"

    ### Channel Offsets
    Creates new images from existing images by applying independent X, Y, and Z shifts to each channel. Useful for correcting chromatic aberration or channel misalignment in multi-channel images.

    ### Combine Images
    Merges multiple images or Z-stacks to create new dimensions (C, T, or Z). Assembles separate images into a single multi-dimensional image with customizable organization and optional color mapping for channels.

    ### Dataset To Plate
    Converts a Dataset of images into a Plate format, placing one image per well at specified row and column positions. Useful for organizing images into high-content screening plate layouts.

    ### Images From ROIs
    Extracts regions defined by rectangular ROIs from images and creates new images from those regions. Can generate either Z-stacks (one tile per ROI) or full 5D images cropped to ROI dimensions.

    ### Move Annotations
    Moves annotations (tags, key-value pairs, comments) from images to their parent wells. Useful for organizing plate-based data by consolidating image-level annotations at the well level, with options to remove original annotations.

=== "User"
    
    [![alt text](scripts/scripts_menu_user.png){width=250px}]   
    ### Dataset to Plate Choose Start position   
    This script is a modification from the `Dataset To Plate` script. It allows you to define a start position (i.e. you did not use the top rows or columns of you plate).
