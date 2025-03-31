# Microscope File Formats

Preferably upload microscope data in its original file format to OMERO. This ensures that all metadata and dimensions are preserved, unless otherwise instructed. Below you can find guidelines for importing common microscopy file types of our microscopes.

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
- CZI files
- LSM files

### ImageXpress

### TIFF Series
- Keep sequential naming intact
- Include any companion metadata files

## Best Practices

**Verify File Completeness**

  - Include all necessary metadata files
  - Keep original file structure
  - Don't split multi-dimensional data


**Check Before Import**

   - Verify file readability
   - Ensure all dimensions are preserved
   - Check channel names and metadata


**After Import** 

   - Verify all dimensions imported correctly
   - Check channel settings
   - Confirm metadata transferred properly