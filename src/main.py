import requests


app_id = '1506824033451537'
app_secret = 'e0a58b1074b2237e90a152a1f4c156d0'
long_term_user_access_token = 'EAAVacs9AvhEBO8FfsYkE9KFjZByjBqv36u5dQPjPemywZAypkqDr7I1edIx0E6kbBFimICWv9TEWyYrHcvFBmiQtHXPQsY1wU6XufviVV7A9uGxRCIVV7bW8nn1tEY8VA39KachRLvpBET3W3MlAFcdd5SDcZAVEtd8s4qy2NewZBevO9HurufS1'
page_name = 'Extra Secret Page'
post_id = "2553705538124434_2552109628284025" # page#_post#


def main():
    print('Hello, world!')
    user_graph_url = f'https://graph.facebook.com/v13.0/me/accounts?access_token={long_term_user_access_token}'
    response = requests.get(user_graph_url)
    data = response.json()
    print('success')
    page_id = None
    for page in data['data']: # Parses json response
        if page['name'] == page_name:
            page_id = page['id'] # Required in order to check conversations
            page_token = page['access_token'] # Grab Page Access Token (it is temporary!)
            print(page_id)
            print(page_token)
            break


    page_graph_url = f'https://graph.facebook.com/v13.0/{page_id}/conversations?access_token={page_token}'
    response = requests.get(page_graph_url)
    data = response.json()
    print(data['message'])

    url = f'https://graph.facebook.com/v13.0/{post_id}?access_token={page_token}'
    response = requests.get(url)

    if response.status_code == 200: #
        post_data = response.json()

    else:
        print("Failed to retrieve the post")

if __name__ == '__main__':
    main()