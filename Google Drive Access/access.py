# Import necessary libraries
from pydrive.auth import GoogleAuth
from pydrive.drive import GoogleDrive

# Authenticate and create PyDrive client
gauth = GoogleAuth()
gauth.LocalWebserverAuth() # Follow the authentication prompts in the browser
drive = GoogleDrive(gauth)

# Define the shared Google Drive link for the video
link = 'https://drive.google.com/file/d/17_TWGi-6jO8LqXhvEaiRzCdyTn9VIgH4/view?usp=share_link'

# Extract the file ID from the link
file_id = link.split('/')[-2]

# Get the file object from Google Drive
file = drive.CreateFile({'id': file_id})
file.GetContentFile('video.mp4') # Download the video file to the local system
