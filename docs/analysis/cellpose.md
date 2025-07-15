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

https://cellpose.readthedocs.io/en/latest/

![cellpose.png](images/cellpose_01.png)

Install Cellpose with GUI via conda. Check [here](conda.md) to learn how to install conda first.
```
conda create -n cellpose 
conda activate cellpose
pip install cellpose[gui]
```

Run the GUI via command line: ```cellpose``` .   

If you have a GPU with CUDA capabilities and have CUDA installed, pip will install the GPU enable version of pytorch. Then CellPose should work on the GPU. You can check if your GPU is found when starting CellPose via the command line, and also in the GUI it is indicated when the GPU is used. Check [here](https://github.com/MouseLand/cellpose#gpu-version-cuda-on-windows-or-linux) for troubleshooting.   

If you have issues running CellPose on your own PC, please try to make use of one of the image analysis workstations available at the Cell Observatory. Or you can make use of a [HPC](../computing/hpc.md) with a remote desktop environment or setting up X-forwarding.   

Try the latest Cellpose version (CellPose-SAM) online at [HuggingFace](https://huggingface.co/spaces/mouseland/cellpose)
