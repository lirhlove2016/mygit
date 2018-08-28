import requests

url = "http://localhost:12306/login"

payload = "{\r\n\t\t\"username\":\"admin\",\r\n\t\t\"password\":\"admin\",\r\n\t\t\"roleID\":\"22\"\r\n}"
headers = {
    'content-type': "application/json",
    'cache-control': "no-cache",
    'postman-token': "3ae3ef24-4944-8b02-6bfb-50b68e7a0471"
    }

response = requests.request("POST", url, data=payload, headers=headers)

print(response.text)
print(response.status_code)
print(response.json())
