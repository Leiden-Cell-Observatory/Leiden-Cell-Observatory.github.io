# ilastik

Interactive machine-learning toolkit for pixel and object classification with sparse annotation.

## Overview

ilastik trains classifiers from a few user-drawn brush strokes and applies them across full datasets. It's useful when thresholding or classical segmentation isn't separable enough but you don't have (or want) a labelled training set for deep learning.

**Key features**

- Pixel classification and object classification workflows
- Autocontext, carving, and tracking workflows for harder cases
- Headless/batch mode via CLI
- Works on 2D, 3D, and time-series data

## Installation

Download the installer for your OS from [ilastik.org/download](https://www.ilastik.org/download.html). ilastik is distributed as a self-contained application; no Python environment needed.

## Integration with other tools

- **Fiji**: apply a trained ilastik project to many images via [the ilastik ImageJ plugin](https://www.ilastik.org/documentation/fiji_export/plugin).
- **TrackMate**: use ilastik segmentations as input to tracking via the [TrackMate-ilastik detector](https://imagej.net/plugins/trackmate/trackmate-ilastik).
- **CellProfiler**: load ilastik predictions as input to a CellProfiler pipeline.

## Official documentation

- [ilastik website](https://www.ilastik.org/)
- [Documentation](https://www.ilastik.org/documentation/)
- [GitHub](https://github.com/ilastik/ilastik)

## Learning resources

### Written

- [Pixel classification tutorial](https://www.ilastik.org/documentation/pixelclassification/pixelclassification) — the most common workflow, good starting point.
- [Object classification tutorial](https://www.ilastik.org/documentation/objects/objects)
- [Tracking workflow](https://www.ilastik.org/documentation/tracking/tracking)

### Video
- [ilastik tutorial at i2k 2022](https://youtu.be/F6KbJ487iiU)

