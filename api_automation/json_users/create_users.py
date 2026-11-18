#Creating posts
import requests
url = "https://jsonplaceholder.typicode.com/users"
payload =  {
    "id": 1,
    "name": "Leanne Graham",
    "username": "Bret",
    "email": "Sincere@april.biz",
    "address": {
      "street": "Kulas Light",
      "suite": "Apt. 556",
      "city": "Gwenborough",
      "zipcode": "92998-3874",
      "geo": {
        "lat": "-37.3159",
        "lng": "81.1496"
      }
    },
    "phone": "1-770-736-8031 x56442",
    "website": "hildegard.org",
    "company": {
      "name": "Romaguera-Crona",
      "catchPhrase": "Multi-layered client-server neural-net",
      "bs": "harness real-time e-markets"
    }
  }

# headers = {
#     "Authorization": "token sdkjfhaiuejdkskfdjklkaf"
# }

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