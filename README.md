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
    pip install jupyter_tabnine
    jupyter contrib nbextension install --user
    jupyter nbextension install --py jupyter_tabnine --user
    jupyter nbextension enable --py jupyter_tabnine --user
    jupyter serverextension enable --py jupyter_tabnine --user
    ```
5. If at any point you modify the `environment.yaml` and want to update the environment, you can do this with

    ```bash
    conda env update --name spatialdata-workshop --file environment.yaml --prune
    ```

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

    # download some already processed data
    python download.py --data_dir data zarr merfish
    ```

Notes on the data:
- The datasets have been manually processed to reduce the file size, by removing certain data, metadata or reducing some
of the image sizes. Due to the reduced size, the datasets are not representative of the original data, nor of the
technology they have been using to profile them. Therefore, they should not be used for any scientific example or
comparison across technologies.
- The MERFISH dataset is from the Allen Institute prototype MERFISH pipeline, and it is not representative of the new commercial MERFISH technology. We choose the former because it's lightweight and already analyzed.


### Running the notebooks
1. Activate the environment as explained above
    ```bash
    conda activate spatialdata-workshop
    ```
2. Start JupyterLab
    ```bash
    jupyter-lab
    ```

# Events
Here you can find a list of our past workshops, including the respective notebooks and slides.
- 2024/09/09: (Tim Treis) BioTrac Spatial Biology Symposium [notebooks](https://github.com/PMBio/spatialdata-workshops/releases/tag/20240909_biotrac) [slides](https://docs.google.com/presentation/d/1-qf25cEX6CUi5cyi6UpVfGzt8sri_D_CSJtDCcaUCw0/edit?usp=sharing)
- 2024/09/11: (Luca Marconato) scverse conference workshop [notebooks](https://github.com/PMBio/spatialdata-workshops/releases/tag/20240911_scverse_workshop) [slides](https://docs.google.com/presentation/d/1YCzs5vI-D4flw4_8DQZCggoyltKuAvBjte8we7t1NrQ/edit?usp=sharing)
- 2024/09/25: (Wouter-Michiel Vierdag, Luca Marconato) EBI 'Advances in spatial omics' webinar series; (Luca Marconato) FoG Live [notebooks](https://github.com/PMBio/spatialdata-workshops/releases/tag/20240925_ebi_fog_live) [slides](https://docs.google.com/presentation/d/18fL7Gul8HBEkbyGpf1zmHHvZnPplwCPpwJXCJLoJA0Q/edit#slide=id.g2d2bb7b9221_0_0)
- 2024/10/22: (Luca Marconato) BIOINFO 2024, Gyeongju (South Korea) [notebooks]() [slides](https://docs.google.com/presentation/d/1XBRkkdbUiLBx1Ys02px6Z26KF0smf-P8UFrgUXuX2YM/edit#slide=id.g2d2bb7b9221_0_0)

- https://docs.google.com/presentation/d/1XBRkkdbUiLBx1Ys02px6Z26KF0smf-P8UFrgUXuX2YM/edit?usp=sharing
