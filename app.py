from bottle import get, post, request, template
import requests


 


@get("/") # 127.0.0.1
def _():
    try:
        url = "http://127.0.0.1:8529/_api/cursor"
        usersObject = {"query": "FOR user IN users RETURN user"}

        # Make the POST request with the URL and the data
        response = requests.post(url, json=usersObject)

        # Check if the request was successful
        if response.status_code == 201:
            print("Request successful!")
         # Assuming the response contains JSON data, you can parse and print it
            data = response.json()
            print(data)
        else:
             print(f"Request failed with status code: {response.status_code}")


        return "x"
      
    except Exception as ex:
          print(f"Error occurred: {ex}")
          
          return f"{ex}"
    finally:
          print("Finished processing request.")




########################################


@get("/users")
def _():
    return "users from get"



########################################


@post("/users")
def _():
    user_name = request.forms.get("user_name")
    user_last_name = request.forms.get("user_last_name")
    return f"Hi {user_name} {user_last_name}"






########################################


@get("/api/users/1")
def _():
    user = {"id":1 , "user_name":"A"}

    return user