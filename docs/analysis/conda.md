# Python environments

Many bioimage analysis tools (Cellpose, napari, micro-sam, StarDist, CAREamics, ...) are Python packages with conflicting dependencies — especially around PyTorch and CUDA. Installing them all into one Python install quickly breaks. The working approach is an **isolated environment per tool**, managed by a tool that can handle both Python and system dependencies (CUDA libraries, Qt, etc.).

We recommend **pixi** for new setups. **Conda / miniforge** still works and is more widely documented — pick whichever fits your existing habits.

## Pixi (recommended)

[Pixi](https://pixi.sh/) is a cross-platform package manager that combines conda-forge and PyPI packages in a single per-project lockfile. It installs both Python and non-Python dependencies, pins CUDA at the environment level, and gives reproducible installs via `pixi.lock`.

### Install

**Windows (PowerShell)**:

```powershell
iwr -useb https://pixi.sh/install.ps1 | iex
```

**Linux / macOS**:

```bash
curl -fsSL https://pixi.sh/install.sh | sh
```

Restart your terminal afterwards. Other install options: [pixi.sh/dev/installation/](https://pixi.sh/dev/installation/).

### Ready-to-use AI tool environments

The [**Leiden-Cell-Observatory/AI_tools_pixi**](https://github.com/Leiden-Cell-Observatory/AI_tools_pixi) repository provides pre-configured pixi environments for the tools most commonly used here:

- **Cellpose** — Cellpose 4 with GUI (CUDA 12.8)
- **micro-sam** — SAM for microscopy with napari, trackastra, napari-omero (CUDA 12.8)
- **StarDist** — nucleus segmentation (TensorFlow 2.10, CUDA 11.8)
- **Trackastra** — deep-learning tracking (CUDA 12.8)
- **CAREamics** — deep-learning denoising/restoration
- **BiaPy** — training bioimage analysis models

Each folder has its own locked environment, so tools don't interfere with each other.

!!! tip
    These pixi environments are drop-in replacements for the conda environments required by the [BIOP Fiji wrappers](https://github.com/BIOP/ijl-utilities-wrappers) (Cellpose/Omnipose plugin, Spotiflow, etc.) — point the Fiji plugin at the `.pixi/envs/default` folder.

### Typical workflow

```bash
# clone once
git clone https://github.com/Leiden-Cell-Observatory/AI_tools_pixi
cd AI_tools_pixi/cellpose

# first-time install resolves and downloads all dependencies
pixi install

# launch the GUI
pixi run cellpose

# or drop into an interactive shell
pixi shell

# check GPU is available
pixi run test-cuda
```

## Conda

[Conda](https://conda.io/) (via [miniforge](https://github.com/conda-forge/miniforge)) is the long-standing option for Python environment management. Use a fresh environment per tool and avoid installing into the `base` environment.

A detailed walkthrough for setting up miniforge: [Getting started with miniforge and Python (BiAPoL)](https://biapol.github.io/blog/mara_lampert/getting_started_with_miniforge_and_python/readme.html#ref-miniforge-python).

### Typical workflow

```bash
# create and activate an environment
conda create -n cellpose python=3.11
conda activate cellpose

# install the tool
pip install cellpose[gui]
```

!!! tip
    Conda environments don't produce a lockfile by default. For reproducibility, export with `conda env export > environment.yml` or switch to pixi.

## Official documentation

- [pixi documentation](https://pixi.sh/)
- [conda documentation](https://docs.conda.io/)
- [miniforge](https://github.com/conda-forge/miniforge)

## Learning resources

- [AI_tools_pixi](https://github.com/Leiden-Cell-Observatory/AI_tools_pixi) — Leiden Cell Observatory's ready-to-use tool recipes.
- [Pixi Python tutorial](https://pixi.sh/latest/tutorials/python/)
- [BiAPoL conda/miniforge guide](https://biapol.github.io/blog/mara_lampert/getting_started_with_miniforge_and_python/readme.html#ref-miniforge-python)
