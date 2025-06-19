# project2

This repository includes a small Python utility to download multiple CSV files from Google Drive individually and load them with `pandas`.

## Prerequisites

- Python 3.7+
- The [`gdown`](https://github.com/wkentaro/gdown) package for downloading from Google Drive.
- The [`pandas`](https://pandas.pydata.org/) library for handling CSV files.

Install the dependencies using pip:

```bash
pip install gdown pandas
```

## Usage

1. Edit `download_csvs.py` and replace the placeholder `FILE_ID_*` values with the actual Google Drive file IDs for your CSV files.
2. Run the script:

```bash
python download_csvs.py
```

Each file will be downloaded and loaded individually. The script prints the shape of each DataFrame as it is read.
