---
title: Segmentation with micro-sam
description: 
published: true
date: 2025-02-05T15:32:44.767Z
tags: 
editor: markdown
dateCreated: 2025-02-05T10:35:00.354Z
---

# Segmentation with micro-sam

Segment Anything for Microscopy or [micro-sam](https://computational-cell-analytics.github.io/micro-sam/micro_sam.html)
is a tool to enable automatic and interactive segmentation of microscopy data.

In order to use the micro-sam toolkit it advisble to use a computer with a decent GPU.

micro-sam can be use to interactively segment images (2D, 3D, time series in napari. It can also be used to fine-tune the Segment Anything model to allow for automatic instance segmentation of your images.

## Installation
It is adviced to install micro-sam in a conda environment. Check [here](conda.md) to install conda.

```bash
conda env create --file environment.yml -n micro-sam
```

```bash
napari
```