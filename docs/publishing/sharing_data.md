# Sharing microscopy data

## Exporting data from OMERO for publication
    
When publishing your microscopy data, it is important to share the data in a way that allows others to access and reuse it. This often involves depositing the data in a public repository. The choice of repository depends on the type of data you have and the requirements of your field.

Ideally you already have your imaging data stored in OMERO. However, since the Leiden University OMERO is not accessible from the internet it is not possible to directly transfer the data to a public repository. Therefore you need to export the data from OMERO to a local computer and then upload it to the public repository. Different repositories require different organization of the (meta)data. To maintain the organization of your data it is recommended to export the data from OMERO in a specific way. Please reach out to the OMERO admins for help with this.

## Repositories 

### BioImage Archive

The BioImage Archive accepts microscopy data from all different modalities. <https://www.ebi.ac.uk/bioimage-archive/> 

More info:  
  - <https://www.ebi.ac.uk/bioimage-archive/submit/>  
  - [FAIR cookbook BIA submission](https://faircookbook.elixir-europe.org/content/recipes/applied-examples/BIA_submission.html) Here you can find a detailed description of how to organize your imaging data and metadata for BIA submission.  
  - [Quick Tour at BIA](https://www.ebi.ac.uk/training/online/courses/bioimage-archive-quick-tour/)  

### Image Data Resource (IDR)


The IDR (<https://idr.openmicroscopy.org/>) is a repository for complete microscopy data sets. The IDR is based on the OMERO platform and allows you to upload your data to the repository and to share it with others, so other can reuse your imaging data. Normally imaging data set should by accompanied with a publication. The IDR allows you to assign a DOI to your data set.

Since IDR is based on OMERO it might be possible to transfer data from OMERO to IDR directly. However, you will need to provide extensive metadata with your imaging data.

Please check here:  
- <https://idr.openmicroscopy.org/about/submission.html>

### Zenodo  

Zenodo (<http://zenodo.org/>) is a general repository for scientific data that allows you to share any kind of data. Zenodo allows you to upload your data to the repository and to share it with others. Zenodo also allows you to publish your data and to assign a DOI to it.  

Submission to Zenodo is free of charge, but normally it is limited to 50GB per dataset.

- <https://help.zenodo.org/docs/deposit/>

### Sharing your image analysis code
Common practice is to maintain your image analysis scripts and other code in a version control system such as GitHub. This allows you to share your code with others and to keep track of changes you make to your code over time.

When publishing a paper that includes image analysis, it is a good idea to include a link to the code repository in the paper. This allows others to reproduce your analysis and to build on your work.

The Cell Observatory also has its own Github repository where you can share your code with others, see <https://github.com/Leiden-Cell-Observatory/> . Please reach out if you would like to create a repository at the Cell Observatory Github.

It is worth to consider to create a release of the version of the code at time of publication and to assign a DOI to this version. This allows to refer to the exact version of the code that was used in the paper and to reproduce your results.
.
One way to get a DOI is to deposit your Github code at Zenodo. Zenodo will create a DOI for the code at time of deposition. This DOI can be included in the paper. 
- Login at Zenodo with your ORCID account
- Connect Zenodo with your Github account
- Enable the Zenodo Github integration for your repository
- Create a release of your code in Github. This will automatically create a DOI for the code in Zenodo.

More information:
- <https://guides.github.com/activities/citable-code/>