# napari

Fast, interactive, multi-dimensional image viewer for Python.

## Overview

napari displays n-dimensional images (2D/3D/4D+) with layered overlays for labels, points, shapes, and tracks. It's often used as the front-end for Python-based analysis workflows and as a host for plugins that wrap other tools (Cellpose, micro-sam, StarDist, and many more).

**Key features**

- N-dimensional viewing with synchronized slicing
- Layer system for images, labels, points, shapes, surfaces, tracks, vectors
- Plugin ecosystem via [napari-hub](https://www.napari-hub.org/)
- Scriptable from Jupyter, IPython, or standalone scripts via the Python API

## Installation

See [Python environments](conda.md) for package manager setup (pixi or conda).

**Recommended if you want napari alongside a specific tool.** The [AI_tools_pixi](https://github.com/Leiden-Cell-Observatory/AI_tools_pixi) repository bundles napari into the environments where it's actually used:

- [`AI_tools_pixi/omero`](https://github.com/Leiden-Cell-Observatory/AI_tools_pixi/blob/master/omero/pixi.toml) — napari + napari-omero for browsing and annotating OMERO images.
- `AI_tools_pixi/micro_sam` — napari + micro-sam + trackastra + napari-omero.
- `AI_tools_pixi/stardist` — napari + StarDist.

Clone the repo, `cd` into the folder, then `pixi install` and `pixi run napari`.

**Standalone napari (pixi).**

```bash
mkdir napari && cd napari
pixi init
pixi add python=3.11 napari pyqt
pixi run napari
```

**Standalone napari (conda).**

```bash
conda create -n napari -c conda-forge python=3.11 napari pyqt
conda activate napari
napari
```

For `pip` or other install options, see the [official install guide](https://napari.org/stable/tutorials/fundamentals/installation.html).

## Official documentation

- [napari website](https://napari.org/)
- [Documentation](https://napari.org/stable/)
- [GitHub](https://github.com/napari/napari)

## Learning resources

### Written

- [Getting started tutorial](https://napari.org/stable/tutorials/fundamentals/getting_started.html)
- [napari-hub](https://www.napari-hub.org/) — browse plugins by task (segmentation, tracking, file IO, etc.).
- [napari tag on Image.sc](https://forum.image.sc/tag/napari) — community Q&A.
