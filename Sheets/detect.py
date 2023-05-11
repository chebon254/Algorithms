import os
import pandas as pd
from google.oauth2.credentials import Credentials
from googleapiclient.discovery import build
from googleapiclient.errors import HttpError

# Set up the credentials for the Google Drive API.
creds = Credentials.from_authorized_user_file('credentials.json')

# Set up the Google Drive API client.
service = build('drive', 'v3', credentials=creds)

# Set the ID of the folder to check for missing files.
folder_id = 'your_folder_id_here'

# Get a list of all the files in the folder.
query = f"'{folder_id}' in parents"
results = service.files().list(q=query, fields="nextPageToken, files(id, name)").execute()
files = results.get('files', [])

# Create a set of all the file names in the folder.
file_names = set([file['name'] for file in files])

# Read in the Excel sheet containing the links.
df = pd.read_excel('invoice1.xlsx')

# Create a set of all the file names in the Excel sheet.
sheet_names = set(df['Article Document'])

# Check which file names are missing from the folder.
missing_names = sheet_names - file_names

# Print out the missing file names.
if missing_names:
    print(f"The following files are missing from the folder:\n{missing_names}")
else:
    print("No files are missing from the folder.")
