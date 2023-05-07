import requests
import json

url = "https://hyijso7cij.execute-api.us-east-1.amazonaws.com/default/getTemplates"

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Test Case 1: Music Event
event1 = ["music",
          "light",
          "concert",
          ""]

response1 = requests.post(url, data=json.dumps(event1), headers=headers)
print("Test Case 1: Music Event\n", response1.text)

