# Notebooks for the tutorial
The tutorial uses the notebooks available in the current folder.

# Additional notebooks (optional)
In addition to the notebooks available in this folder, other notebooks from the docs are suitable to be used for teaching. A list of them follows.
## Notebooks from `spatialdata-notebooks`

You can download the notebooks directly, or download all the notebooks of `spatialdata-notebooks` via `git clone https://github.com/scverse/spatialdata-notebooks`.
- [Coordinate transformations](https://github.com/scverse/spatialdata-notebooks/blob/main/notebooks/examples/transformations.ipynb)
- [Alignment via landmark annotations, query, aggregation](https://github.com/giovp/spatialdata-sandbox/blob/main/notebooks/czi_demo/xenium_visium.ipynb)

## Noteboks from `napari-spatialdata`
- [`napari-spatialdata` scatterplot widget notebook part 1](https://github.com/fjorka/napari-spatialdata/blob/kmk-scatter-pg/docs/notebooks/scatterwidget.ipynb)
- [`napari-spatialdata` scatterplot widget notebook part 2](https://github.com/fjorka/napari-spatialdata/blob/kmk-scatter-pg/docs/notebooks/scatterwidget_annotation.ipynb)

## Getting the data
Please note that some of optional the notebooks above require the download of additional datasets. Each notebook explains how to download the data. An alternative optional approach is to clone the `spatialdata-sandbox` repository via `git clone https://github.com/giovp/spatialdata-sandbox`. This repository contains several folders, one per dataset, with scripts (or instructions) on how to download the data and convert it to the SpatialData Zarr format.

For instance, the Visium HD subset data used in the notebooks of the `spatialdata-workshop` repository, used a dataset that we denote with `visium_hd_3.0.0_io_subset`. This is a subset of the full dataset available via `spatialdata-sandbox` at this link https://github.com/giovp/spatialdata-sandbox/tree/main/visium_hd_3.0.0_io.
If you are interested in obtaining the full dataset, after cloning the `spatialdata-sandbox` repository, you can simply run the following to obtain both the raw data and the same data converted in the SpatialData Zarr format.
```bash
conda activate spatialdata-workshop
# eventually, a requirements.txt file is present in the dataset folder, if additional packages are needed
cd visium_hd_3.0.0_io
python download.py
python to_zarr.py
```
