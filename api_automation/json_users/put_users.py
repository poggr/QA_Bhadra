import requests
url = "https://jsonplaceholder.typicode.com/users/1"
payload =  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bretman",
    "email": "bret@april.biz",
    }

response = requests.put(url, json=payload)
status_code = response.status_code

if response.status_code == 200:
    print("Post is updated ")
else:
    print("The request failed with status code: ", status_code)

print(response.json())
# print(response.status_code)

# assert response.status_code== 200, "Post is not updated"
# print("Post is updated successfully")