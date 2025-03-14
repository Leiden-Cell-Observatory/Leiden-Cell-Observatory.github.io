# Microscope Files

This guide covers importing specific microscope file formats into OMERO.

## Supported File Types

OMERO supports most common microscopy formats including:
- Nikon ND2
- Zeiss LSM and CZI
- Leica LIF
- TIFF series
- And many more through Bio-Formats

## Import Guidelines

### Nikon ND2 Files
- Keep associated metadata files together
- Import complete ND2 files, not exported TIFFs
- Verify all channels are preserved

### Zeiss Files
- For LSM files, ensure metadata is preserved
- With CZI files, check all scenes are included
- Maintain folder structure for multi-file datasets

### TIFF Series
- Keep sequential naming intact
- Include any companion metadata files
- Maintain channel order and naming

## Best Practices

1. **Verify File Completeness**
   - Include all necessary metadata files
   - Keep original file structure
   - Don't split multi-dimensional data

2. **Check Before Import**
   - Verify file readability
   - Ensure all dimensions are preserved
   - Check channel names and metadata

3. **After Import**
   - Verify all dimensions imported correctly
   - Check channel settings
   - Confirm metadata transferred properly