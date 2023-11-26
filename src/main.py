import facebook

def main():
    print('Hello, world!')
    app_id = '1506824033451537'
    app_secret = 'e0a58b1074b2237e90a152a1f4c156d0'
    long_term_user_access_token = 'EAAVacs9AvhEBO8FfsYkE9KFjZByjBqv36u5dQPjPemywZAypkqDr7I1edIx0E6kbBFimICWv9TEWyYrHcvFBmiQtHXPQsY1wU6XufviVV7A9uGxRCIVV7bW8nn1tEY8VA39KachRLvpBET3W3MlAFcdd5SDcZAVEtd8s4qy2NewZBevO9HurufS1'
    page_name = 'Extra Secret Page'

    # Initialize the Graph API with the long-term user access token
    graph = facebook.GraphAPI(access_token=long_term_user_access_token, version="18.0")  # Update with the appropriate version!!!

    # Get the Page ID using the page name through the Graph API
    pages = graph.get_object('me/accounts')['data']
    page_id = None
    for page in pages:
        if page['name'] == page_name:
            page_id = page['id']
            print(page_id)
            break

    if page_id:
        # Get the Page Access Token using the Page ID
        page_info = graph.get_object(id=page_id, fields='access_token')
        page_access_token = page_info['access_token']
        print(f"Page Access Token for {page_name}: {page_access_token}")
    else:
        print(f"Page '{page_name}' not found.")

if __name__ == '__main__':
    main()