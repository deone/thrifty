
import requests

def send_request(url, data):
    get_response = requests.get(url)
    post_response = requests.post(
          url,
          data=data,
          headers={"X-CSRFToken": get_response.cookies['csrftoken']},
          cookies=get_response.cookies
        )

    return post_response.json()
