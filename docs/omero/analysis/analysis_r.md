# R Analysis with OMERO

A library to connect R with OMERO exists, however it has limited functionality, and it is rather outdated, compared to the Python or Fiji libraries.

A better alternative is to use the Python API/ezomero in Rstudio. 

## Reticulate/ezomero
The [reticulate](https://rstudio.github.io/reticulate/) package makes it easy to run Python in R(studio) and directly work with Python objects inside R scripts.
This makes it possible to use the [ezomero](https://thejacksonlaboratory.github.io/ezomero/ezomero.html) package in R. 
An script and Rmarkdown document showcasing how it can used to work with tables, images, annotations and attachments.
It can be found on the Leiden Cell Observatory github: https://github.com/Leiden-Cell-Observatory/OMERO_scripts/tree/main/R

## romero.gateway

You can find more information here how to install it in Rstudio:
<https://omero-guides.readthedocs.io/en/latest/r/docs/rstudio.html>

Some more details explanations including example notebooks can be found here:
<https://omero-guides.readthedocs.io/en/latest/r/docs/r_walkthrough.html>

