# CellProfiler analysis with OMERO

In old versions of CellProfiler (Version 2) it was possible to directly work with images from OMERO in CellProfiler, but this is no longer available.    
In future versions of CellProfiler a better integration with OMERO is planned. In the meantime, there are the following workflows to work with OMERO data in CellProfiler.

1. Create a file with OMERO image IDs. This can be loaded into CellProfiler. See this discussion on [image.sc](https://forum.image.sc/t/establish-connection-between-omero-cellprofiler/22438/10) for more information. And this documentation from cellprofiler <https://cellprofiler-manual.s3.amazonaws.com/CPmanual/Help_Other%20Features_Accessing_Images_From_OMERO.html>

For example:
```
omero:iid=58134
omero:iid=58135
omero:iid=58136
```

Or if your channels are in separeted OMERO images:
```
URL_DNA,URL_GFP
omero:iid=58134,omero:iid=58038
omero:iid=58135,omero:iid=58039
omero:iid=58136,omero:iid=58040
```

Then use `File>Import>File List...` to load the file into CellProfiler. If you have multi channel images you can use the `NamesAndTypes` module to extract metadata using `ChannelName` . See this instructions from the CellProfiler [documentation](https://cellprofiler-manual.s3.amazonaws.com/CPmanual/Help_Other%20Features_Accessing_Images_From_OMERO.html).   

!!! note 
    Using OMERO URLs with the Input modules   
    The Images module has a file list panel of all of the image files in a project. This file list supports URLs including OMERO URLs. You can drag URLs from a text document and drop them into the file list. The URLs do not end with image file extensions (like .TIF), so you need to change the "Filter images?" setting to "No filtering" to allow the OMERO URLs to be processed further. You should be able to view the image by double-clicking on it and you should be able to extract plate, well, site and channel name metadata from each image using the "Extract from image file headers" method in the Metadata module (press the "Update Metadata" button after selecting the "Extract from image file headers" method). If your experiment has more than one image channel, you can use the "ChannelName" metadata extracted from the OMERO image to create image sets containing all of your image channels. In the NamesAndTypes module, change the "Assign a name to" setting to "Images matching rules". For the rule criteria, select "Metadata does have ChannelName matching" and enter the name that appears under "Channels" in the OMERO Insight browser. Add additional channels to NamesAndTypes using the "Add another image" button.

Limitations:
- It won't work well for 3D images. You need separate files for each channel on OMERO.

2. Running CellProfiler from within a Jupyter notebook. You can have a look at [this](https://omero-guides.readthedocs.io/en/latest/cellprofiler/docs/cellprofiler.html) guide.
3. Manually export images from OMERO. You can make use of the Fiji/Java or Python API of OMERO to automatically organize the files.

## Uploading CellProfiler results to OMERO
It can be useful to store the output of your CellProfiler analysis in OMERO. In this way you keep the results of your analysis together with the original data. Alternatively you can add a annotation to the dataset in OMERO with a reference where the results are stored. 
