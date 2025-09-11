---
title: Cellpose
description: Deep learning model for object segmentatation
published: true
date: 2025-03-14T14:45:04.141Z
tags: 
editor: markdown
dateCreated: 2025-03-11T06:28:30.906Z
---

# Cellpose

Cellpose is a generalist deep learning model for cellular segmentation.   
- It can be used via a GUI, in Python or via command line. Also an Fiji plugin is available that can connect to Cellpose to obtain segmentations directly in Fiji. 
- Cellpose can be used to segment cells, nuclei, and other objects in 2D (and 3D) images. 
- The latest version (Cellpose-SAM) works well on a variety of cell types and imaging modalities without the need for retraining. However, Cellpose also allows training of custom models.

Cellpose documentation: [https://cellpose.readthedocs.io/en/latest/](https://cellpose.readthedocs.io/en/latest/)

![cellpose.png](images/cellpose_01.png)

You can try the latest Cellpose version with one of your images here:(CellPose-SAM) online at [HuggingFace](https://huggingface.co/spaces/mouseland/cellpose)

## Installation

### GUI
Cellpose has a GUI, which is running in Python, which allows you to load images, apply the models and visualize the results. Furthermore it has a build-in routine to fine tune the model by allowing you to manually correct annotations and use those annotations to improve the model for your data.

- It is recommended to run Cellpose with GPU (CUDA) for better performance.   
- Installing Cellpose via the command line is necessary. It is best to use a package manager such as pixi or conda to install all dependencies.   
- Read [here](conda.md) to learn how to install conda on your computer first.   

- Then install Cellpose with GUI via conda:
  
```
#create a new conda environment
conda create -n cellpose   

#activate the new environment
conda activate cellpose   

#install cellpose with GUI
pip install cellpose[gui]
```

Run the GUI via command line: ```cellpose``` . You need to activate the environment every time via `conda activate cellpose`   

- If you have a GPU with CUDA capabilities, pip will install the GPU enabled version of pytorch. Then CellPose should work with the GPU. You can check if your GPU is found when starting CellPose via the command line, and also in the GUI it is indicated when the GPU is used. Check [here](https://github.com/MouseLand/cellpose#gpu-version-cuda-on-windows-or-linux) for troubleshooting.   

- If you have issues running CellPose on your own PC, please try to make use of one of the image analysis workstations available at the Cell Observatory. Or you can make use of a [HPC](../computing/hpc.md) with a remote desktop environment or setting up X-forwarding.   

### Fiji plugin
There is an cellpose plugin in Fiji which allows you to use Cellpose directly within the Fiji environment. However this requires a working installation of Cellpose (see instructions above) and its dependencies on your system. The plugin is part of the `PTBIOP` Fiji update site.   
- In Fiji go to `Help > Update`, click on `Manage Update Sites` and add the `PTBIOP` Fiji update site.   
- After restarting Fiji it should be available at `Plugins > BIOP > Cellpose/Omnipose'.   
- You will need to configure the plugin with the path to your Cellpose installation. With 'conda env list' in the terminal, you can find the path to your Cellpose environment. Then, set the path in the Fiji plugin configuration.
- For the latest cellpose model you can set `cpsam` as the `--pretrained model`.

Tip: If you want to convert the cellpose images to ROIs in Fiji you can use the same update site to run `Plugins > BIOP > Image Analysis > ROIs > Label Image to ROIs`.

The update site: [https://wiki-biop.epfl.ch/en/ipa/fiji/update-site](https://wiki-biop.epfl.ch/en/ipa/fiji/update-site)
More information about the plugin: [https://github.com/BIOP/ijl-utilities-wrappers](https://github.com/BIOP/ijl-utilities-wrappers)

### Command line
If you want to process many images (e.g. in a folder), you can also use Cellpose via the command line. You can use the same installation as for the GUI.
More information can be found here: [Cellpose Command Line Interface](https://cellpose.readthedocs.io/en/latest/command.html#command-line-examples)


### Run cellpose on the HPC
If you want to run Cellpose GUI with a GPU you make use of the [Alice](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/37519361/ALICE) cluster. 
There are different ways to do this but one way is to setup a remote desktop session with RDP. Follow the  instructions on the Alice wiki [here](https://pubappslu.atlassian.net/wiki/spaces/HPCWIKI/pages/152731649/Getting+a+remote+desktop+on+ALICE+with+RDP#Connecting-from-Windows) . You can use the MobaXterm application to make it easier to setup the connection.   
What we will do is pull an singularity container image with cellpose. This assures all required tools are available.   

- Start a terminal.

```
#first ceate a folder to save the container image 

mkdir ~/data1/containers/cellpose
cd ~/data1/containers/cellpose

#create an interactive slurm job
salloc -p testing --gres=gpu:1

#this is needed to find the online repository 
apptainer remote add --no-login SylabsCloud cloud.sycloud.io

# pull the image
singularity pull --arch amd64 library://ez82/cellpose/4.0.6:latest
```

Next you can start the container 
```
singularity run --nv 4.0.6_latest.sif
#now open cellpose
cellpose
#GUI opens 😀

```
The next time you can just start a slurm job and run the singularity image .
