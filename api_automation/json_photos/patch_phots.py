import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
payload = {
     
    "title": "reprehenderit est deserunt velit ipsam"
  }

response = requests.patch(url, json=payload)

print(response.json())
print(response.status_code)

assert response.status_code== 200, "Post is not updated"
print("Post is updated successfully")