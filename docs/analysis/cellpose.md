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

![cellpose.png](images/cellpose_01.png){.align-center}

install via conda
```
conda create -n cellpose 
conda activate cellpose
pip install cellpose
```

with CUDA GPU:
```
conda create -n cellpose pytorch=1.8.2 cudatoolkit=10.2 -c pytorch-lts
conda activate cellpose
pip install cellpose
```

run gui via command line: ```cellpose```

## Considerations
- 
