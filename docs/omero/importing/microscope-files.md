# Microscope File Formats

Preferably upload your microscopy data in its original file format to OMERO. This ensures that all image acquisition metadata and dimensions are preserved.   
Below you can find guidelines for importing common microscopy file types of our microscopes.

!!! question "Questions?"
      If you are still running into problems with uploading your data, or when you are not sure how to do it properly, please reach out to one of the OMERO admins for help!

## Supported File Types

OMERO supports most common microscopy formats including:

   - Nikon `.nd2`
   - Zeiss `.lsm` and `.czi`
   - Leica `.lif`
   - Imaris  `.ics` e.g. from the Dragon Spinning disc confocal
   - ImageXpress `.jdce` and `.htd`
   - (OME)-TIFF files
   - And many more through Bio-Formats
   - Tiff files EVOS microscope - Some exported datasets from the EVOS microscope give issues when importing into OMERO. Please reach out so we can help you to resolve the issue.
   - Incucyte archive(s) - These files cannot imported into OMERO directly. If you like to import incycyte data into OMERO files need to be converted. We have developed a converter in Python which allows conversion of Incucyte archives in to OME-TIFF or OME-ZARR. You can find more information via the following link, but feel free to ask for help. [NL-Bioimaging/biomero-converter](https://github.com/NL-BioImaging/biomero-converter )

## Import Guidelines

### Nikon ND2 Files
Nikon files can be uploaded directly using OMERO.insight, however when dealing in high-content screening data, it is recommended to split the ND2 files into individual wells before uploading, otherwise you might loose the information from which well the images were . You can find the details how to work with ND2 files in the [HCS Data Structure](hcs-data.md#pre-processing-of-nikon-data) guide.

### Zeiss Files
Zeiss .CZI and .LSM (old Zeiss microscope format) can be uploaded directly to OMERO.

## Leica LIF Files
Leica .lif files can be uploaded directly to OMERO. LIF files containing multiple microscope images are splitted as separated OMERO images automatically.

## Imaris ICS
These files can be uploaded directly via OMERO.insight. Often you will get multiple OMERO images at different 'resolution-levels' in OMERO. Make sure to keep the highest (original) resolution images, you can remove the low resolution images if you don't need them. 

### ImageXpress .JDCE
Data from the new [ImageXpress HT.ai](../../../microscopes/mic_pages/imagexpress-htai/) cannot be imported directly via OMERO.insight. One solution is to first convert the data to OME-TIFF before importing to OMERO. If you do so using the [NGFF Converter](https://www.glencoesoftware.com/products/ngff-converter/) metadata will be properly handled.

### ImageXpress .HTD
Data from the now deprecated ImageXpress microscope are stored in a database at the microscope. For proper importing to OMERO into plate format the data needs to be exported from the database. Check the instructions [here](hcs-data.md#pre-processing-of-imagexpress-data).

### TIFF Series
- Keep sequential naming intact
- Avoid uploading TIFF files with separate channels as they won't be combined automatically in OMERO
- Include any companion metadata files

## After Import
   - Verify all dimensions imported correctly
   - Check channel settings
   - Confirm metadata transferred properly

