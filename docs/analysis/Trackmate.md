---
title: Trackmate
description: 
published: true
date: 2025-03-14T13:56:45.617Z
tags: 
editor: markdown
dateCreated: 2025-03-11T06:28:29.067Z
---

# TrackMate

https://imagej.net/plugins/trackmate/
Getting started: https://imagej.net/plugins/trackmate/tutorials/getting-started

Fiji plugin to track objects e.g. cells, foci or single-molecules.

Basically consists of two steps. First segmentation/detection of objects then apply a tracking algorithm on this.

Segmentation of objects can be done through different methods e.g. spot detector, on a binary image, Stardist (nuclei), Cellpose, ilastik.
For tracking also different algorithms are available.

Scriptable in Fiji.
https://imagej.net/plugins/trackmate/scripting/scripting

Also tools available to apply same analysis on multiple images without writing a script.
Trackmate batcher: https://forum.image.sc/t/new-version-of-the-trackmate-helper-v1-2-1-with-a-batcher-and-the-spt-metrics/68180

## Saving TrackMate projects
- TrackMate results can be saved as XML files containing all tracking data
- You can open this again in Fiji via Plugins->Tracking->Load a TrackMate file
- Trick for projecting tracks onto a different image: You can open the XML file in a text editor, then search for the image filename reference and modify it

## Key points to discuss:

- Integration with OMERO: How to store and retrieve TrackMate results in OMERO
- Batch processing: Methods for applying the same tracking parameters across multiple images
- Script examples: Basic Jython/Groovy scripts for automating TrackMate analysis
- Export options: Different ways to export tracking results (CSV, ROIs, visualizations)
- TrackMate parameters: Explanation of key tracking settings and when to adjust them
