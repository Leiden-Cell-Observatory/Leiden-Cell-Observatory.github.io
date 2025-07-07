# Microscope File Formats

Preferably upload your microscopy data in its original file format to OMERO. This ensures that all image acquisition metadata and dimensions are preserved.   
Below you can find guidelines for importing common microscopy file types of our microscopes.

!!! question "Questions?"
      If you are still running into problems with uploading your data, or when you are not sure how to do it properly, please reach out to one of the OMERO admins for help!

## Supported File Types

OMERO supports most common microscopy formats including:

   - Nikon ND2
   - Zeiss LSM and CZI
   - Leica LIF
   - (OME)-TIFF files
   - And many more through Bio-Formats

## Import Guidelines

### Nikon ND2 Files
Nikon files can be uploaded directly, however when dealing in high-content screening data, it is recommended to split the ND2 files into individual wells before uploading. You can find the details how to work with ND2 files in the [HCS Data Structure](hcs-data.md#pre-processing-of-nikon-data) guide.

### Zeiss Files
Zeiss .CZI and .LSM (old Zeiss microscope format) can be uploaded directly to OMERO.

## Leica Files
Leica .lif files can be uploaded directly to OMERO.

### ImageXpress
Data from the ImageXpress microscope are stored in a database at the microscope. For proper importing to OMERO into plate format the data needs to be exported from the database. Check the instructions [here](hcs-data.md#pre-processing-of-imagexpress-data).

### TIFF Series
- Keep sequential naming intact
- Avoid uploading TIFF files with separate channels as they won't be combined automatically in OMERO
- Include any companion metadata files

## After Import
   - Verify all dimensions imported correctly
   - Check channel settings
   - Confirm metadata transferred properly

