import requests

print("Om Sairam")
print("Hello World")

response = requests.post("https://httpbin.org")
print(response.status_code)
print(response.content)
