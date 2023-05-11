import pyautogui
import time
import webbrowser

# Replace the link below with the link to the YouTube video you want to capture screenshots from
video_url = "https://youtu.be/reRddCJ3I9Q"

# Open the YouTube video in the default browser
webbrowser.open(video_url)

# Wait for the video to load
time.sleep(10)

# Set the initial screenshot counter to 1
screenshot_counter = 1

# Loop to capture screenshots every 2 minutes
while True:
    # Take a screenshot of the video
    screenshot = pyautogui.screenshot()
    screenshot.save("screenshot" + str(screenshot_counter) + ".png")
    
    # Increment the screenshot counter
    screenshot_counter += 1
    
    # Wait for 2 minutes
    time.sleep(120)
