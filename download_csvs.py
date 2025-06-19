import pandas as pd
import gdown

# List of Google Drive file IDs for each CSV
# Replace with your actual file IDs
file_ids = [
    'FILE_ID_1',
    'FILE_ID_2',
    'FILE_ID_3',
]

# Download each CSV individually and read into a DataFrame
for file_id in file_ids:
    url = f'https://drive.google.com/uc?id={file_id}'
    output = f'{file_id}.csv'

    # Download the file from Google Drive
    gdown.download(url, output, quiet=False)

    # Read the CSV into a DataFrame
    df = pd.read_csv(output)
    print(f'Loaded {output} with shape: {df.shape}')

