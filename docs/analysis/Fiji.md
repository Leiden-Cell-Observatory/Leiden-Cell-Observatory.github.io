# Fiji

Fiji Is Just ImageJ — a distribution of ImageJ bundled with plugins for scientific image analysis.

## Overview

Fiji packages ImageJ with a curated set of plugins for the life sciences, plus an integrated updater that keeps both Fiji and its plugins current. It runs as a standalone application (Java is bundled — no separate install needed) on Windows, macOS, and Linux.

**Key features**

- Large plugin ecosystem via [update sites](https://imagej.net/update-sites/)
- Macro recorder and scripting in ImageJ Macro, Jython, Groovy, JavaScript, BeanShell
- Bio-Formats for reading most microscopy file formats
- ROI Manager, 3D Viewer, stitching, registration, and deconvolution plugins

## Installation

1. Download from the [Fiji download page](https://fiji.sc/#download).
2. Extract the archive and run the executable for your OS (`ImageJ-win64.exe`, `Fiji.app`, or `ImageJ-linux64`).
3. Keep it current via `Help > Update...` and manage extra plugin sources via `Help > Update... > Manage Update Sites`.

!!! tip
    Many Cell Observatory workflows depend on the `PTBIOP` update site (e.g. the Cellpose wrapper). Enable it via `Manage Update Sites` when needed.

## Scripting

Fiji can be automated at three levels of complexity:

- **Macro recorder** (`Plugins > Macros > Record...`) — captures your GUI actions as an ImageJ Macro script. The fastest way to start automating a manual workflow.
- **ImageJ Macro Language** — simple scripting for batch operations. Reference: [Built-in Macro Functions](https://imagej.net/ij/developer/macro/functions.html).
- **Jython, Groovy, BeanShell** — for more complex scripts anything the macro language can't express cleanly. See the [Fiji scripting guide](https://imagej.net/scripting/).

Keep scripts in a Git repository — see [GitHub](github.md) for a handy setup to keep track of your script changes.

## Official documentation

- [Fiji website](https://fiji.sc/)
- [ImageJ learning portal](https://imagej.net/learn/)
- [ImageJ wiki](https://imagej.net/)

## Learning resources

### Video

- [NEUBIAS Academy on YouTube](https://www.youtube.com/@NEUBIASAcademy) — webinars on Fiji, plugins, and common workflows.

### Written

- [Getting started with Fiji](https://imagej.net/learn/)
- [Image.sc Forum](https://forum.image.sc/) — primary community support channel for Fiji, ImageJ, and most tools on this page.
