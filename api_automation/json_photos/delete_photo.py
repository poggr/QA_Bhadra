import requests
url = "https://jsonplaceholder.typicode.com/posts/1"
response = requests.delete(url)

print(response.json())
print(response.status_code)

assert response.status_code== 200, "request status code in not 200"
print("request successfully")