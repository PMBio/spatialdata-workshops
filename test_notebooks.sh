#!/bin/bash

# Directory containing the Jupyter notebooks
NOTEBOOK_DIR="notebooks"

# List of notebooks to execute
notebooks=(
  "nb1_spatialdata_objects.ipynb"
  "nb2_static_plotting.ipynb"
  "nb3_interactive_plotting_with_napari.ipynb"
  "nb4_simple_analysis_using_scverse_tools.ipynb"
)

# Function to execute a notebook and print the result
execute_notebook() {
  local notebook_path="$1"
  jupyter nbconvert --to notebook --execute "$notebook_path" --inplace
  if [ $? -eq 0 ]; then
    echo "Successfully executed $notebook_path"
  else
    echo "Error executing $notebook_path"
  fi
}

# Loop over each notebook in the list and execute them in parallel
for notebook in "${notebooks[@]}"; do
  notebook_path="$NOTEBOOK_DIR/$notebook"
  echo "Starting execution of $notebook_path..."
  execute_notebook "$notebook_path" &
done

# Wait for all background processes to finish
wait

echo "All notebooks executed."
