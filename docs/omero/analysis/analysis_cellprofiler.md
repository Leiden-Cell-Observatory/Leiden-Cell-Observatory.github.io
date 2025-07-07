# CellProfiler analyis with OMERO

In old versions of CellProfiler (Version 2) it was possible to directly work with images from OMERO in CellProfiler, but this is no longer available.    
In future versions of CellProfiler a better integration with OMERO is planned. In the meantime, there are the following workflows to work with OMERO data in CellProfiler.

1. Create a file with OMERO image IDs. This can be loaded into CellProfiler. 

```File>Import>File List...```

See this discussion on [image.sc](https://forum.image.sc/t/establish-connection-between-omero-cellprofiler/22438/10) for more information. This creates such a file:

```
URL_DNA,URL_GFP
omero:iid=58134,omero:iid=58038
omero:iid=58135,omero:iid=58039
omero:iid=58136,omero:iid=58040
```
Limitations:
- It won't work well for 3D or multichannel images. You need separate files for each channel on OMERO.

2. Running CellProfiler from within a Jupyter notebook. You can have a look at [this](https://omero-guides.readthedocs.io/en/latest/cellprofiler/docs/cellprofiler.html) guide.
3. Manually export images from OMERO. You can make use of the Fiji/Java or Python API of OMERO to automatically organize the files.

## Uploading CellProfiler results to OMERO
It can be useful to store the output of your CellProfiler analysis in OMERO. In this way you keep the results of your analysis together with the original data. Alternatively you can add a annotation to the dataset in OMERO with a reference where the results are stored. 