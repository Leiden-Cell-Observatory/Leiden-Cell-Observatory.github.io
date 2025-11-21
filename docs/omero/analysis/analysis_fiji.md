## Fiji image analysis for OMERO

While an official OMERO plugin for Fiji exists, which allows to load images from OMERO directly in Fiji and upload results and ROIs back to OMERO, at Leiden University we have our own developed plugin, which allows to directly run developed Fiji scripts/plugins on images in OMERO.

By following the steps below, you can install the required plugins and run your analysis on images in Fiji.

### Installation Steps

1. Install Fiji
2. Update Fiji and ensure all plugins are up to date (Help > Update)  
    - If you get errors, repeat the update (the updater might need multiple attempts)  
    - After seeing "Updated successfully. Please restart ImageJ!" message, restart Fiji  

![Update success message](analysis_fiji/images/analysis_fiji_01.png)

3. After restarting, update again and click "Manage Update Sites"

![Manage update sites](analysis_fiji/images/analysis_fiji_02.png)

4. Enable these required sites:  
    - Fiji legacy
    - 3D Image suite
    - ImageScience
    - Leiden University
    - PTBIOP

![Update sites selection](analysis_fiji/images/analysis_fiji_03.png)


1. Click Close and Apply Changes
2. Restart Fiji
3. Install the Simple OMERO Client:  
    - Download from [GitHub releases](https://github.com/GReD-Clermont/simple-omero-client/releases)  
    - Place in Fiji's plugins folder  
    - Restart Fiji  

## Analysis Methods

### Manual Single Image Analysis

1. Open OMERO connection:  
    - Go to Plugins > OMERO > Connect to OMERO  
    - Login with ULCN credentials  
    - OMERO.insight connected to Fiji will open  

2. Access your image:  
    - Locate image in left sidebar or thumbnails  
    - Double-click to open  

3. Configure BioFormats Import:  
   ![BioFormats import options](analysis_fiji/images/analysis_fiji_04.png)
    - Adjust settings as needed
    - Click OK
    - Wait for loading (may take several minutes, no progress bar visible)

### Dataset Analysis

#### Manual Dataset Analysis

1. Launch dataset opener:
   - Go to Plugins > LeidenUniv > OMERO > Open OMERO dataset
   - Enter login credentials:
   ![Login screen](analysis_fiji/images/OmeroOpenDataset_01.png)

2. Select dataset:  
   ![Dataset selection](analysis_fiji/images/OmeroOpenDataset_02.png)  
   - Choose group, user, project, and dataset
   - Click OK

3. Monitor progress:  
   ![Loading progress](analysis_fiji/images/OmeroOpenDataset_03.png)  
   - Watch log window for loading progress
  
4. Analyze your data creating either:
   Resultstables
   ROIs
   Images

5. Upload results to OMERO via Plugins>Omero>
   Save results to OMERO
   Save Rois to OMERO
   Save Image(s) to OMERO   

#### Automated Dataset Analysis

1. Start automated analysis:  
    - Go to Plugins > LeidenUniv > OMERO > Run OMERO plugin  
   - Enter login credentials:
   ![Login screen](analysis_fiji/images/OmeroOpenDataset_01.png)

2. Choose Plugin to run:  
   ![Choose Plugin](analysis_fiji/images/OmeroOpenDataset_04.png)  

3. Select dataset:  
   ![Dataset selection for automation](analysis_fiji/images/OmeroOpenDataset_02.png)

4. Optionally set plugin parameters

5. View results after the plugin finishes:  
    - Results attach to image/dataset automatically  
   ![Log](analysis_fiji/images/OmeroOpenDataset_05.png)  
   ![Results attachment](analysis_fiji/images/OmeroOpenDataset_06.png)
   ![Detailed results](analysis_fiji/images/OmeroOpenDataset_07.png)

!!! info
    If you need a plugin that isn't available, contact [Joost Willemse](mailto:jwillemse@biology.leidenuniv.nl) for assistance.

## Exporting Data

### Quick Downloads
- Use download button (yellow) on OMERO web interface:
![Download button](analysis_fiji/images/analysis_fiji_13.png)
- Choose export format:
![Export options](analysis_fiji/images/analysis_fiji_14.png)

### Large Dataset Downloads

1. In OMERO.insight:
    - Navigate to your dataset
    - Click download button
    ![Download in insight](analysis_fiji/images/analysis_fiji_15.png)

2. Select export format:
    ![Export format selection](analysis_fiji/images/analysis_fiji_16.png)
    - Download proceeds in background

## Server Scripts

Access server scripts through the web interface:
![Server scripts](analysis_fiji/images/analysis_fiji_17.png)

> ## Important Notes
> - Server is optimized for storage, not computation
> - Scripts may take significant time to process
> - All scripts must be tested on test-server first
> - **DO NOT develop or test scripts without admin consultation**
<!-- {blockquote:.is-danger} -->

For new script development, contact Joost Willemse.
