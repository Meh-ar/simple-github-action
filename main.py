import os
import requests
from datetime import datetime

# Define the URL and directory
url = "https://jsonplaceholder.typicode.com/posts"
directory = "responses"

# Ensure the responses directory exists
if not os.path.exists(directory):
    os.makedirs(directory)

# Get the current timestamp to use in the filename
timestamp = datetime.now().strftime("%Y%m%d_%H%M%S")
filename = os.path.join(directory, f"posts_{timestamp}.json")

# Send the GET request
response = requests.get(url)

# Save the response to a file
with open(filename, 'w') as file:
    file.write(response.text)

print(f"Response saved to {filename}")

