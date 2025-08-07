# Python with OMERO

With Python you can interact with OMERO extensively. It is possible to upload data, annotations and ROIs. It is also possible to obtain image data directly as an (e.g. numpy) array so you can do your analysis with the data directly.

For working with OMERO you need to install the OMERO Python API packages.

## Installation
[omero-py](https://omero.readthedocs.io/en/stable/developers/Python.html) - official Python bindings for OMERO

[ezomero](https://thejacksonlaboratory.github.io/ezomero/) - an additional package with convenience functions for working with OMERO in Python

Communication with OMERO via Python requires the OMERO Ice package. Compiling those from scratch can be difficult hence binaries are available for different operating systems and Python versions: <https://www.glencoesoftware.com/blog/2023/12/08/ice-binaries-for-omero.html> . Alternatively it is installable via conda instead of pip.

Create a new virtual or [conda](../../analysis/conda.md) environment and install the required packages. 

### Conda/pip
```bash
conda create -n omero python=3.10
pip install https://github.com/glencoesoftware/zeroc-ice-py-win-x86_64/releases/download/20240325/zeroc_ice-3.6.5-cp310-cp310-win_amd64.whl
pip install ezomero
```

### Pixi
Pixi is a alternative package manager from conda with some useful features. First you need to install pixi, find the instructions [here](https://pixi.sh/latest/installation/#__tabbed_1_2).

```bash
#create a folder where pixi will run from
mkdir omero_python
cd omero_python
pixi init
pixi add python=3.10
pixi add zeroc-ice
pixi add omero-py
pixi add --pypi ezomero
```
This will install the required packages for your system. Now you can run a command in your pixi enviroment with `pixi run` e.g. `pixi run python`. Or you can create a shell with `pixi shell` .

### Notebooks
You can for example use Jupyter notebooks to work with OMERO data.  
Example notebooks that show how you can interact with OMERO can be found here: <https://github.com/Leiden-Cell-Observatory/omero_ipynb>  
And from the OMERO website: [https://omero-guides.readthedocs.io/en/latest/cellprofiler/docs/cellprofiler.html#](https://github.com/ome/training-notebooks)


