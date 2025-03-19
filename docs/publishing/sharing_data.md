# Sharing microscopy data

## Repositories 

### BioImage Archive
https://www.ebi.ac.uk/bioimage-archive/

The BioImage Archive accepts microscopy data from all different modalities. 

More info:
- https://www.ebi.ac.uk/bioimage-archive/submit/

### IDR
https://idr.openmicroscopy.org/

The IDR is a repository for complete microscopy data sets. The IDR is based on the OMERO platform and allows you to upload your data to the repository and to share it with others, so other can reuse your imaging data. Normally imaging data set should by accompanied with a publication. The IDR allows you to assign a DOI to your data set.

Since IDR is based on OMERO it might be possible to transfer data from OMERO to IDR directly. However, you will need to provide extensive metadata with your imaging data.

Please check here:
- https://idr.openmicroscopy.org/about/submission.html

### Zenodo
http://zenodo.org/

Zenodo is a general repository for scientific data that allows you to share any kind of data. Zenodo allows you to upload your data to the repository and to share it with others. Zenodo also allows you to publish your data and to assign a DOI to it.

Submission to Zenodo is free of charge, but normally it is limited to 50GB per dataset.

- https://zenodo.org/

### Sharing your image analysis code
Common practice is to maintain your image analysis scripts and other code in a version control system such as GitHub. This allows you to share your code with others and to keep track of changes you make to your code over time.

When publishing a paper that includes image analysis, it is a good idea to include a link to the code repository in the paper. This allows others to reproduce your analysis and to build on your work.

It is worth to consider to release a specific version of the code at time of publication and to assign a DOI to this version. This allows others to refer to the exact version of the code that was used in the paper and to reproduce your results
.
One way to do so is to deposit your Github code at Zenodo. Zenodo will create a DOI for the code at time of deposition. This DOI can be included in the paper.

More information:
- https://guides.github.com/activities/citable-code/