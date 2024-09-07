# Workshop: introduction to the SpatialData framework

## Installing the required packages

### Using conda / mamba
We'll be using `conda` or `mamba` (faster) as a package manager here, depending on what is installed on the teaching . This allows to set up the entire environment with a single command.
1. create the conda environment from the `environment.yaml` file

    ```bash
    # it's recommended to use mamba for faster installation, or set libmamba as the default solver
    # conda config --set solver libmamba
    conda env create -f environment.yaml -y

    # alternatively, if you already have a conda environment you'd like to use, you can update it like this
    conda env update --name myenv --file environment.yaml --prune
    ```

2. activate the environment
    ```bash
    conda activate spatialdata-workshop
    ```

3. register the conda environment in Jupyter
    ```bash
    python -m ipykernel install --user --name spatialdata-workshop --display-name "Python (SpatialData Workshop)"
    ```

4. Optionally: Set up auto-completion inside of Jupter Notebooks
    ```bash
    jupyter contrib nbextension install --user
    jupyter nbextension install --py jupyter_tabnine --user
    jupyter nbextension enable --py jupyter_tabnine --user
    jupyter serverextension enable --py jupyter_tabnine --user
    ```
5. If at any point you modify the `environment.yaml` and want to update the environment, you can do this with

    ```bash
    conda env update --name spatialdata-workshop --file environment.yaml --prune
    ```


### Running the notebooks
1. Activate the environment as explained above
    ```bash
    conda activate spatialdata-workshop
    ```
2. Start JupyterLab
    ```bash
    jupyter-lab
    ```

## :warning: **The below steps are only relevant outside of this workshop.** We already took care of this beforehand.

### Downloading the data
1. Activate the environment as explained above
    ```bash
    conda activate spatialdata-workshop
    ```
2. Run the following command to download the data
    ```bash
    # download the raw data
    python download.py --data_dir data raw visium
    python download.py --data_dir data raw visium_hd
    python download.py --data_dir data raw xenium
    ```
