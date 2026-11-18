import requests
url = "https://jsonplaceholder.typicode.com/albums/1"
payload = {
            "userId": 1,
          "title": "this is automation albums"
  }

response = requests.patch(url, json=payload)

print(response.json())
print(response.status_code)

assert response.status_code== 200, "Post is not updated"
print("Post is updated successfully")