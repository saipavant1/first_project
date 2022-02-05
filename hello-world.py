import requests

print("Om Sairam")
print("Hello World")

response = requests.post("https://3.209.99.235/post",verify=False)
print(response.status_code)
print(response.content)
