## HCS metadata

### Minimal Information for High Content Screening in Microscopy Experiments (MIHCSME)

For HCS experiments we use the MIHCSME metadata template. This Excel template allows to describe your screen at different levels (Study, Assay, and per Plate and Well). 

The template can be found at [this repository](https://github.com/Leiden-Cell-Observatory/metadata_templates/tree/main/MIHCSME_template), with some filled-in examples.

For reference the templates are originally published here here: <https://fairdomhub.org/investigations/575>

## Adding Metadata templates to OMERO
### Attaching a description, metadata and quantified results to your images

The current recommendation is to attach metadata template to your Screen in OMERO. Make sure to convert your data in OMERO into Plates and Screens first.   
Then attach the template as an attachement to your screen.
When you update the template you can create a new version of the template and add a version number (_v2, v2,1, v3 etc,).   
It is possible to add more files such as a library file to the Screen as well.

2)  Add the (mandatory) attachments to the file using the attachment section (green box). This includes the metadata template in pdf format and all additional files.

![alt text](metadata/images/metadata_07.png)

*Overview of screen where you can describe the data that is in a plate and add the attachments.*
