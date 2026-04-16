# QuPath

Open-source software for bioimage analysis, with a focus on digital pathology and whole-slide imaging.

## Overview

QuPath is built around efficient viewing and annotation of large 2D images (whole-slide scans, tiled images). It combines classical detection (cell/nucleus detection, pixel classifiers) with deep-learning extensions and is scriptable in Groovy for reproducible pipelines.

**Key features**

- Fast viewing of multi-gigapixel whole-slide images
- Annotation, cell detection, and pixel classification built in
- Groovy scripting with a clear API
- Extension system covering deep-learning segmentation and external data sources

## Installation

Download the latest version from [qupath.github.io](https://qupath.github.io/). Detailed install notes (including GPU setup for deep-learning extensions) are in the [official installation guide](https://qupath.readthedocs.io/en/stable/docs/intro/installation.html).

## Extensions

Useful extensions commonly used alongside QuPath:

- [InstanSeg](https://qupath.readthedocs.io/en/stable/docs/deep/instanseg.html) — generalist cell/nucleus segmentation built into recent QuPath versions.
- [StarDist](https://qupath.readthedocs.io/en/stable/docs/deep/stardist.html) — star-convex nucleus segmentation.
- [Cellpose](https://github.com/BIOP/qupath-extension-cellpose) — calls a local Cellpose install from QuPath.
- [OMERO extension](https://qupath.readthedocs.io/en/stable/docs/advanced/omero.html#omero-extension) — load images directly from an OMERO server into a QuPath project.

## Official documentation

- [QuPath website](https://qupath.github.io/)
- [Documentation](https://qupath.readthedocs.io/)
- [GitHub](https://github.com/qupath/qupath)

## Learning resources

- The official documentation has very clear [tutorials](https://qupath.readthedocs.io/en/stable/docs/tutorials/index.html)   

### Written

- The official documentation has very clear [Tutorials](https://qupath.readthedocs.io/en/stable/docs/tutorials/index.html)
- [Scripting guide](https://qupath.readthedocs.io/en/stable/docs/scripting/index.html) — automating analysis with Groovy.

### Video

- [QuPath tutorials by Pete Bankhead](https://www.youtube.com/@QuPath) — the maintainer's own walkthroughs; the best starting point.

