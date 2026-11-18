import requests
url = "https://jsonplaceholder.typicode.com/users/1"
response = requests.delete(url)
status_code = response.status_code

# if response.status_code == 200:
#     print("Post is updated ")
# else:
#     print("The request failed with status code: ", status_code)

print(response.json())
print(response.status_code)

assert response.status_code== 200, "Post is not deletedd"
print("Post is deleted successfully")