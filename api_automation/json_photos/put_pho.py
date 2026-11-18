import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {
     "albumId": 1,
    "id": 2,
    "title": "reprehenderit est deserunt velit ipsam"
  }

response = requests.put(url, json=payload)

print(response.json())
print(response.status_code)

assert response.status_code== 200, "Post is not updated"
print("Post is updated successfully")