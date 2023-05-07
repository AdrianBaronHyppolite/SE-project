import requests
import json

url = "https://hyijso7cij.execute-api.us-east-1.amazonaws.com/default/getTemplates"

# Set the headers
headers = {
    "Content-Type": "application/json"
}

# Test Case 2: Sports Event with Additional Specifications
event3 = ["sports",
          "bright",
          "soccer",
          ["cart", "newsletter"]]

response3 = requests.post(url, data=json.dumps(event3), headers=headers)
print("Test Case 2: Sports Event\n", response3.text)