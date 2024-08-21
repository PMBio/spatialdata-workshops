"""
Download 3 portions of public datasets respectively profiled with Visium, Xenium, and Visium HD (raw data format).

Datasets:
---------
1. Visium (Human Glioblastoma)
   - Original source: https://www.10xgenomics.com/datasets/gene-and-protein-expression-library-of-human-glioblastoma-cytassist-ffpe-2-standard

2. Xenium (Human Lung)
   - Original source: https://www.10xgenomics.com/support/software/xenium-onboard-analysis/latest/resources/xenium-example-data

3. Visium HD (Mouse Small Intestine)
   - Original source: https://www.10xgenomics.com/datasets/visium-hd-cytassist-gene-expression-libraries-of-mouse-intestine

Note:
-----
The datasets have been manually processed to reduce the file size, by removing certain data, metadata or reducing some
of the image sizes. Due to the reduced size, the datasets are not representative of the original data, nor of the
technology they have been using to profile them. Therefore, they should not be used for any scientific example or
comparison across technologies."""

import argparse
import os
from pathlib import Path
import subprocess


def main():
    parser = argparse.ArgumentParser(
        description="Download and/or unzip raw spatial data and data in the SpatialData Zarr format."
    )
    parser.add_argument(
        "format",
        choices=["raw", "zarr"],
        help="Specify the data format: 'raw' or 'zarr'.",
    )
    parser.add_argument(
        "technology",
        choices=["visium", "xenium", "visium_hd", "merfish"],
        help="Specify the technology: 'visium', 'xenium', 'visium_hd' or 'merfish'.",
    )
    parser.add_argument(
        "target_folder",
        help="Specify the target folder where the data will be saved.",
    )
    parser.add_argument(
        "--no-download",
        default=False,
        action="store_true",
        help="Whether to download the file (default: True)",
    )
    parser.add_argument(
        "--no-unzip",
        default=False,
        action="store_true",
        help="Whether to unzip the file (default: True)",
    )

    args = parser.parse_args()

    url = "https://s3.embl.de/spatialdata/raw_data/workshop/"
    if args.technology == "visium":
        url += "visium_2.1.0_2_io_subset"
    elif args.technology == "xenium":
        url += "xenium_2.0.0_io_subset"
    elif args.technology == "visium_hd":
        url += "visium_hd_3.0.0_io_subset"
    elif args.technology == "merfish":
        url = "https://s3.embl.de/spatialdata/spatialdata-sandbox/merfish.zip"

    if args.technology != "merfish":
        if args.format == "raw":
            url += ".zip"
        elif args.format == "zarr":
            url += ".zarr.zip"
    else:
        assert args.format == "zarr", "MERFISH data is only available in the SpatialData Zarr format."

    os.makedirs(args.target_folder, exist_ok=True)

    if not args.no_download:
        print(f"Downloading data to {args.target_folder} from {url}")
        command = f"curl {url} --output '{Path(args.target_folder) / Path(url).name}'"
        subprocess.run(command, shell=True, check=True)

    if not args.no_unzip:
        print(f"Unzipping data to {args.target_folder}")
        command = f"unzip -o '{Path(args.target_folder) / Path(url).name}' -d {args.target_folder}"
        subprocess.run(command, shell=True, check=True)


if __name__ == "__main__":
    main()