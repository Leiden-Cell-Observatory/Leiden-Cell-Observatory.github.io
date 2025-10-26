# Sharing microscopy data
   
- When publishing your microscopy data, it is important to share the data in a way that allows others to **access** and **reuse** it. This often involves depositing the data in a **public repository**. The choice of repository depends on the type of microscopy data you have.

- We can advice and support you on how to prepare your **imaging data** and **metadata** for repository submission.   

- Ideally you already have your imaging data stored in OMERO. However, since the Leiden University OMERO is not accessible from the internet it is not possible to directly transfer the data to a public repository. Also, different repositories require different organization of the (meta)data. Please **reach out** to us so we can help you to get your imaging data in the right format.

## Repositories 

=== "BioImage Archive (BIA)"

    The [BioImage Archive](https://www.ebi.ac.uk/bioimage-archive/) accepts microscopy data from all different modalities. Submitting your imaging data requires adding metadata according to the [REMBI](https://www.ebi.ac.uk/bioimage-archive/rembi-help-overview/) standard.  

    More info:  
      - How to submit your data: <https://www.ebi.ac.uk/bioimage-archive/submit/>  
      - [FAIR cookbook BIA submission](https://faircookbook.elixir-europe.org/content/recipes/applied-examples/BIA_submission.html) Here you can find a detailed description of how to organize your imaging data and metadata for BIA submission.  
      - [Quick Tour at BIA](https://www.ebi.ac.uk/training/online/courses/bioimage-archive-quick-tour/)  

=== "Image Data Resource (IDR)"

    The [Image Data Resource](<https://idr.openmicroscopy.org/>) is a curated repository for complete microscopy data sets. The IDR is based on the OMERO platform and to thus allows to access published data easily. Normally imaging data set should by accompanied with a publication. The IDR allows you to assign a DOI to your data set.

    Since IDR is based on OMERO it might be possible to transfer data from OMERO to IDR directly. However, you will need to provide extensive metadata with your imaging data.

    Please check here:  
    - <https://idr.openmicroscopy.org/about/submission.html>

=== "Zenodo"  

    [Zenodo](http://zenodo.org/) is a general repository for scientific data that allows you to share any kind of data. Zenodo allows you to upload your data to the repository and to share it with others. Zenodo also allows you to publish your data and to assign a DOI to it.  

    Submission to Zenodo is free of charge, but normally it is limited to 50GB per dataset.

    - <https://help.zenodo.org/docs/deposit/>

    !!! tip "Sharing scripte with reviewers"
        If you don't want that your zenodo repository is published on Zenodo before your paper is accepted and published, but still want the reviewers to see the intended submission, there is way to do so.   
             1. First you create a draft version of your submission, which include all your files, without publishing it.    
             2. You can already request a DOI for the Zenodo submission to include in your paper. Later, upon publication your data can be found via this doi.    
             3. Then it is possible to [create a public link](https://help.zenodo.org/docs/share/link-sharing/) to the draft so you can share this with the reviewers. The reviewers can see your submission through this link.    
## Sharing your image analysis code
Common practice is to maintain your image analysis scripts and other code in a version control system such as GitHub. This allows you to share your code with others and to keep track of changes you make to your code over time.    

When publishing a paper that includes image analysis, it is a good idea to include a link to the code repository in the paper. This allows others to reproduce your analysis and to build on your work.    

The Cell Observatory also has its own Github repository where you can share your code with others, see <https://github.com/Leiden-Cell-Observatory/> . Please reach out if you would like to create a repository at the Cell Observatory Github.    

It is worth to consider to create a release of the version of the code at time of publication and to assign a DOI to this version. This allows to refer to the exact version of the code that was used in the paper and to reproduce your results.    

One way to get a DOI is to deposit your Github code at Zenodo. Zenodo will create a DOI for the code at time of deposition. This DOI can be included in the paper.     
1. Login at Zenodo with your ORCID account    
2. Connect Zenodo with your Github account    
3. Enable the Zenodo Github integration for your repository    
4. Create a release of your code in Github. This will automatically create a DOI for the code in Zenodo.    

More information:    
- <https://guides.github.com/activities/citable-code/>    
