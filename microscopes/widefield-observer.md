---
title: Widefield Observer
description: Guide for using the Zeiss Observer microscope, particularly for multi-well imaging
published: true
date: 2025-02-05T20:50:01.000Z
tags: microscopes, widefield, observer, multi-well
editor: markdown
dateCreated: 2025-02-05T20:50:01.000Z
---

# Widefield Observer

## Multi-well Imaging Setup

This guide covers the setup process for multi-well imaging using the Zeiss Observer microscope with Zen-blue software.

### Initial Setup

1. Launch Zen-blue software
2. Calibrate the stage
3. Navigate to acquisition tab
4. Activate the tiles module

### Sample Carrier Configuration

1. In the tiles menu, select "Sample Carrier"
2. Choose your desired carrier type
3. Use Smart Setup to configure imaging conditions
   > At least one channel must be set up for carrier calibration
   <!-- {blockquote:.is-info} -->

### Calibration Process

1. **Stage Calibration**
   - Option to calibrate using transmitted light (recommended)
   - Choose between re-calibrating or continuing with existing calibration

2. **Calibration Points**
   - Select calibration method (7 points recommended)
   - Position points with high accuracy
   - More points generally yield better results

### Advanced Setup

#### Region Setup Options

1. **Contour Method**
   - Draw regions manually for imaging

2. **Predefined Method**
   - Click on slide to add region
   - Use plus button to add setup region

3. **Carrier Method**
   - Set fill factor for coverage
   - Configure columns/rows for custom layout
   - Click create to generate tile regions

#### Position Setup Options

1. **Location Method**
   - Manual point placement
   - Click to add specific points

2. **Array Method**
   - Add multiple points in random or grid pattern
   - Draw regions to define point distribution area

3. **Carrier Method**
   - Add regions (columns/rows) in each well

### Focus Settings

1. Access Support Point Editor (circle with dot icon above calibrate button)
2. Add support points for focus shift:
   - Manual addition via plus button
   - Add one per container
   - Set row/column distribution
3. Adjust point positions as needed

### Final Steps

1. Verify all tile regions
2. Review support point positions
3. Confirm settings before starting acquisition

> For optimal results, carefully verify focus points and tile regions before starting a long acquisition sequence.
<!-- {blockquote:.is-success} -->

## Best Practices

1. Use transmitted light for initial calibration when possible
2. Add sufficient support points to maintain focus across the sample
3. Verify all settings before starting long acquisitions
4. Consider sample characteristics when choosing imaging regions

