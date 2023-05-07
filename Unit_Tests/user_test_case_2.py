import requests
import json

url = "https://hyijso7cij.execute-api.us-east-1.amazonaws.com/default/getTemplates"

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Test Case 2: Sports Event
event2 = ["sports",
          "bright",
          "soccer",
          ""]

response2 = requests.post(url, data=json.dumps(event2), headers=headers)
print("Test Case 2: Sports Event\n", response2.text)