#Creating posts
import requests
url = "https://jsonplaceholder.typicode.com/posts"
payload = {
    "userId": 1,
    "id": 1,
    "title": "API Automation",
    "body": "This is automation"
  }

headers = {
    "Authorization": "token sdkjfhaiuejdkskfdjklkaf"
}

response = requests.post(url, json=payload, headers= headers)
# status_code = response.status_code

# if response.status_code == 201:
#     print("Post is created ")
# else:
#     print("The request failed with status code: ", status_code)

print(response.json())
print(response.status_code)

assert response.status_code== 201, "Post not created"
print("Post is created successfully")

# & "$env:LOCALAPPDATA\Microsoft\WindowsApps\python3.13.exe" -m pip install numpy pandas matplotlib