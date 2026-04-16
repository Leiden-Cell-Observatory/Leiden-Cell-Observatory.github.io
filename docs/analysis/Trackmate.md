# TrackMate

Fiji plugin for detecting and tracking objects (cells, foci, single molecules) across time-lapse images.

## Overview

TrackMate splits tracking into two stages: first detect objects in each frame, then link detections into tracks. Both stages offer multiple algorithms, so the same plugin covers use cases from nuclear tracking to single-molecule analysis.

**Key features**

- Multiple detectors: LoG/DoG spot detection, thresholding, label-image import, [StarDist](https://imagej.net/plugins/trackmate/trackmate-stardist), [Cellpose](https://imagej.net/plugins/trackmate/trackmate-cellpose), [ilastik](https://imagej.net/plugins/trackmate/trackmate-ilastik)
- Multiple trackers: LAP, Kalman, nearest-neighbour, overlap-based
- Interactive track editing and filtering
- Scriptable in Jython/Groovy for reproducible pipelines
- TrackMate Batcher for running the same settings over many files without scripting

## Installation

TrackMate ships with Fiji — no separate install needed. Detector extensions (StarDist, Cellpose, ilastik) are enabled via their respective update sites; see the plugin pages linked above.

## Saving and loading results

- Results save as an XML file containing detections, tracks, and the source image reference.
- Reopen via `Plugins > Tracking > Load a TrackMate file`.

!!! tip
    To project existing tracks onto a different image (e.g. a registered version), open the XML in a text editor and edit the image filename reference before loading.

## Official documentation

- [TrackMate plugin page](https://imagej.net/plugins/trackmate/)
- [Getting started](https://imagej.net/plugins/trackmate/tutorials/getting-started)
- [Scripting guide](https://imagej.net/plugins/trackmate/scripting/scripting)

## Learning resources

### Written

- [TrackMate tutorials index](https://imagej.net/plugins/trackmate/tutorials/) — covers detectors, trackers, and analysis workflows.
- [TrackMate Batcher + SPT metrics](https://forum.image.sc/t/new-version-of-the-trackmate-helper-v1-2-1-with-a-batcher-and-the-spt-metrics/68180) — run the same pipeline on multiple movies without scripting.
