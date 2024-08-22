import requests
import json
from datetime import datetime

# URL to send the GET request to
url = "https://jsonplaceholder.typicode.com/posts"

# Send GET request
response = requests.get(url)

# Check if the request was successful
if response.status_code == 200:
    # Get the JSON data
    data = response.json()

    # Create a filename with the current timestamp
    filename = f"responses/posts_{datetime.now().strftime('%Y%m%d_%H%M%S')}.json"

    # Write the data to a file in JSON format
    with open(filename, 'w') as file:
        json.dump(data, file, indent=4)
else:
    print(f"Failed to retrieve data. Status code: {response.status_code}")

