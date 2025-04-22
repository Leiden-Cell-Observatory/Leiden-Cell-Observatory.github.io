---
title: Downloading from OMERO
description: 
published: true
date: 2025-02-28T20:25:09.132Z
tags: 
editor: markdown
dateCreated: 2025-02-05T10:35:24.344Z
---

# Downloading and Exporting Data

This page describes how to download and export data from OMERO.

## OMERO.web Downloads

### Quick Downloads
Access downloads through the OMERO web interface:

1. Locate your data
2. Click the download button at the right panel
3. Choose export format:
   - Original files
   - Original metadata
   - OME-TIFF format
   - JPEG format
   - PNG format
   - TIFF format

![Download from OMERO web](downloading/images/downloading_01.png)

!!! warning "Web Browser Timeout Limitation"
    Connections via the web browser automatically disconnect after 1 minute (60s), so often you won't be able to download large files. For larger datasets, use OMERO.insight instead.

## OMERO.insight Downloads

### Large Dataset Downloads
1. Launch and log into OMERO.insight
2. Navigate to your dataset
3. Click the download button
   ![Download in insight](downloading/images/downloading_02.png)
4. Select export format

Downloads proceed in the background - no progress bar is shown, but the process remains active.

## Fiji Downloads

Alternatively you can use the OMERO Fiji plugin for downloading data. You can find more information [here](../analysis/analysis_fiji/#exporting-data)

## Export Formats

### Standard Formats
- **Original Format**: Exact copy of uploaded file
- **OME-TIFF**: Standard microscopy format
- **JPEG/PNG**: For presentations/publications
- **TIFF**: For analysis software

### Format Selection
Choose based on intended use:  

- Analysis: Original or OME-TIFF  
- Presentation: JPEG/PNG  
- Archive: Original format  


