#Creating posts
import requests
url = "https://jsonplaceholder.typicode.com/photos"
payload = {
     "albumId": 1,
    "id": 1,
    "title": "this is automation phots",
    "url": "https://picsum.photos/seed/1/600",
    "thumbnailUrl": "https://picsum.photos/seed/1/150"
  }


response = requests.post(url, json=payload)
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