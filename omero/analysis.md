---
title:  Data Analysis with OMERO
description: 
published: true
date: 2025-02-05T14:46:22.267Z
tags: 
editor: markdown
dateCreated: 2025-02-05T10:35:21.282Z
---

# Data Analysis with OMERO

There are different ways you can interact with data in OMERO.

## Setting Up Fiji for OMERO

### Installation Steps

1. Install Fiji
2. Update Fiji and ensure all plugins are up to date (Help > Update)
   - If you get errors, repeat the update (the updater might need multiple attempts)
   - After seeing "Updated successfully. Please restart ImageJ!" message, restart Fiji

![Update success message](images/media/image1.png)

3. After restart, update again and click "Manage Update Sites"

![Manage update sites](images/media/image2.png)

4. Enable these required sites:
   - Fiji legacy
   - 3D Image suite
   - ImageScience
   - Leiden University

![Update sites selection](images/media/image3.png)

5. Click Close and Apply Changes
6. Restart Fiji
7. Install the Simple OMERO Client:
   - Download from [GitHub releases](https://github.com/GReD-Clermont/simple-omero-client/releases)
   - Place in Fiji's plugins folder
   - Restart Fiji

## Analysis Methods

### Manual Single Image Analysis

1. Open OMERO connection:
   - Go to Plugins > OMERO > Connect to OMERO
   - Login with ULCN credentials
   - OMERO insight connected to Fiji will open

2. Access your image:
   - Locate image in left sidebar or thumbnails
   - Double-click to open

3. Configure BioFormats Import:
   ![BioFormats import options](images/media/image4.png)
   - Adjust settings as needed
   - Click OK
   - Wait for loading (may take several minutes, no progress bar visible)

### Dataset Analysis

#### Manual Dataset Analysis

1. Launch dataset opener:
   - Go to Plugins > LeidenUniv > OMERO > Open OMERO dataset
   - Enter login credentials:
   ![Login screen](images/media/image5.png)

2. Select dataset:
   ![Dataset selection](images/media/image6.png)
   - Choose group, user, project, and dataset
   - Click OK

3. Monitor progress:
   ![Loading progress](images/media/image7.png)
   - Watch log window for loading progress

#### Automated Dataset Analysis

1. Start automated analysis:
   - Go to Plugins > LeidenUniv > OMERO > Run OMERO plugin
   - Choose plugin from menu:
   ![Plugin selection](images/media/image8.png)

2. Provide credentials:
   ![Login for automated analysis](images/media/image9.png)

3. Select dataset:
   ![Dataset selection for automation](images/media/image10.png)

4. View results:
   - Results attach to image/dataset automatically
   ![Results attachment](images/media/image11.png)
   ![Detailed results](images/media/image12.png)

::: {.callout-note}
If you need a plugin that isn't available, contact J.J. (Joost) Willemse  for assistance.
:::

## Exporting Data

### Quick Downloads
- Use download button (yellow) on OMERO web interface:
![Download button](images/media/image13.png)
- Choose export format:
![Export options](images/media/image14.png)

### Large Dataset Downloads

> The web browser downloads timeout after 1 minute (60s). For large datasets, use OMERO.insight client.
{.is-warning}

1. In OMERO.insight:
   - Navigate to your dataset
   - Click download button
   ![Download in insight](images/media/image15.png)

2. Select export format:
   ![Export format selection](images/media/image16.png)
   - Download proceeds in background

## Server Scripts

Access server scripts through the web interface:
![Server scripts](images/media/image17.png)

> ## Important Notes
> - Server is optimized for storage, not computation
> - Scripts may take significant time to process
> - All scripts must be tested on test-server first
> - **DO NOT develop or test scripts without admin consultation**


For new script development, contact Willemse, J.J. (Joost).