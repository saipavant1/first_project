import requests

print("Om Sairam")
print("Hello World")

response = requests.get("www.google.com")
print(response.status_code)
print(response.content)
