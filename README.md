# Workshop: introduction to the SpatialData framework

## Installing the required packages

### Using pip (faster)
1. Create a virtual environment with `venv` or `conda`/`mamba`; then activate it.

    Using `venv` (if you are in the `(base)` conda environment, please use `conda` as explained here below):
    ```bash
    python3 -m venv venv
    source venv/bin/activate
    ```
    Alternative, using `conda`; `conda` is used only to create the environment, `pip` is then used to install the packages:
    ```bash
    conda create -n workshop python=3.10 -y
    conda activate workshop
    ```
2. Install the required packages
    ```bash
    pip install -r requirements.txt
    ```

### Using conda / mamba (safer)
If you get installation errors with `pip`, please try using `conda`/`mamba` instead.
1. create the conda environment from the `environment.yml` file

    Using `mamba`:
    ```bash
    mamba env create -f environment.yml -y
    ```

    Alternative, using `conda`:
    ```bash
    # it's recommended to use mamba for faster installation, or set libmamba as the default solver
    # conda config --set solver libmamba
    conda env create -f environment.yml -y
    ```
2. activate the environment
    ```bash
    conda activate workshop
    ```
3. register the conda environment in Jupyter
    ```bash
    python -m ipykernel install --user --name spatialdata-workshop --display-name "Python (SpatialData Workshop)"
    ```

## Downloading the data
1. Activate the environment as explained above
2. Run the following command to download the data
    ```bash
    # download the raw data
    python download.py --data_dir data raw visium
    python download.py --data_dir data raw visium_hd
    python download.py --data_dir data raw xenium
   
    # download the data already converted to the SpatialData Zarr format
    python download.py --data_dir data zarr visium_hd
    python download.py --data_dir data zarr merfish
    ```

Notes on the data:
- The datasets have been manually processed to reduce the file size, by removing certain data, metadata or reducing some
of the image sizes. Due to the reduced size, the datasets are not representative of the original data, nor of the
technology they have been using to profile them. Therefore, they should not be used for any scientific example or
comparison across technologies.
- The MERFISH dataset is from the Allen Institute prototype MERFISH pipeline, and it is not representative of the new commercial MERFISH technology.

## Running the notebooks
1. Activate the environment as explained above
2. Start JupyterLab
    ```bash
    jupyter-lab
    ```