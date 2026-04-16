# CellProfiler

GUI-based pipeline tool for high-throughput image analysis, develop an image analysis workflow without the need for programming.

## Overview

CellProfiler chains modular image processing steps (illumination correction, segmentation, measurement, export) into a pipeline that can be saved, shared, and run headlessly on many images. It's a common choice for high-content screening and any workflow where the same analysis applies to hundreds or thousands of images.

**Key features**

- Modular pipeline builder with no scripting required
- Headless batch execution for cluster/HPC processing
- Extensible via Python plugins, including deep-learning segmenters (StarDist, Cellpose)
- Export to tables (CSV) or SQL for downstream analysis

## Installation

Download the latest release from [cellprofiler.org/releases](https://cellprofiler.org/releases). Older versions are available via [previous releases](https://cellprofiler.org/previous-releases) — some published pipelines only work with a specific CellProfiler version.

### CellProfiler with AI tools included

Getting CellProfiler to talk to Cellpose and StarDist is awkward to configure from scratch. Glencoe Software maintains a fork of CellProfiler v4.2.8 with both pre-bundled:

- Installer: [CellProfiler + Stardist/Cellpose release (v4.2.80002-ai)](https://github.com/glencoesoftware/CellProfiler/releases/v4.2.80002-ai/)

Install this version and the AI modules work out of the box.

## Official documentation

- [CellProfiler website](https://cellprofiler.org/)
- [Manual](https://cellprofiler-manual.s3.amazonaws.com/CellProfiler-4.2.8/index.html)
- [GitHub](https://github.com/CellProfiler/CellProfiler)

## Learning resources

### Written

- [Getting started tutorials](https://cellprofiler.org/tutorials) — official worked examples covering common pipelines.
- [Published example pipelines](https://cellprofiler.org/examples) — adapt a nearby pipeline rather than building from scratch.
