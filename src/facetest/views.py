import requests
import facebook # from facebook-sdk package

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from django.shortcuts import redirect

from .forms import FacebookPostForm
from .forms import FacebookMessageForm

# TODO: Auto update access_t_page with access_t (long-term) ALSO work on parsing cURL responses for conversations, acess tokens, etc.

app_id = '1506824033451537'
app_secret = 'e0a58b1074b2237e90a152a1f4c156d0'

long_term_user_access_token = 'EAAVacs9AvhEBO8FfsYkE9KFjZByjBqv36u5dQPjPemywZAypkqDr7I1edIx0E6kbBFimICWv9TEWyYrHcvFBmiQtHXPQsY1wU6XufviVV7A9uGxRCIVV7bW8nn1tEY8VA39KachRLvpBET3W3MlAFcdd5SDcZAVEtd8s4qy2NewZBevO9HurufS1'
page_name = 'Extra Secret Page'
#page_token = 'EAAVacs9AvhEBOzPD0VmeXihXwpEv0Be2YdZBR7XAqAfdUBrZC69Lwn567QlxBZC5E45OyEOkYPsz3it2d9JBNK1nZAYise5Hfi6I8AgNGp2A6zB5ZBaDbg9e7yvy91IT7a1H5FtPJc5BJw1aUZBsnKgyWmvGMPkFZBFYW8wpw5a4R8ZBYOFCG0DDZCepQOpbfbedus579rfdsCJ0ZAOXxadLPuxDUZD'
page_token = None

post_id = "2553705538124434_2552109628284025" # page#_post
page_id = "155168831017376"

post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)


def facemsg_view(request):
    refresh_page_token()
    recipient_id = "7254791501239920"
    url = f"https://graph.facebook.com/v18.0/{page_id}/messages"
    message_id = "t_2565001643661490-oSnFgY4Gw"
    if request.method == 'POST':
        msgform = FacebookMessageForm(request.POST)
        if msgform.is_valid():
            msg = msgform.cleaned_data['text']

            data = {
                'recipient': {'id': recipient_id },
                'messaging_type': 'RESPONSE',
                'message': {'text': msg},
                'access_token': page_token,
            }

            response = requests.post(url, json = data)
            if response.status_code == 200: # Successful response retrieval status code
                print("success!")
                msgform = FacebookMessageForm()
            else:
                print(response.text)
                print("An error has occured")
    else:
        msgform = FacebookMessageForm()

    context = {
        "msgform": msgform,
    }
    return render(request, 'facetest/facebook-msg.html', context)


def facetest_view(request): #only handles post requests with facepost name
    if request.method == 'POST':
        postform = FacebookPostForm(request.POST)
        if postform.is_valid():
            text = postform.cleaned_data['text']
            #age_token = setPageToken()
            payload = {
                'message': text,
                'access_token': page_token
            }

            response = requests.post(post_url, data = payload)
            if response.status_code == 200: # Successful response retrieval status code
                print("success!")
                postform = FacebookPostForm()
            else:
                print(response.text)
                print("An error has occured")
    else:
        postform = FacebookPostForm()
        print(request.POST)

    context = {
        "postform": postform,
    }
    return render(request, 'facetest/facebook-post.html', context)

def spam_msg_test():
    for i in range(10):
        data = {
            'recipient': {'id': recipient_id},
            'messaging_type': 'RESPONSE',
            'message': {'text': msg + str(i)},
            'access_token': page_token,
        }

def spam_post_test(requests,custom_message, spamNum):
    for i in range(spamNum):
        text = 'spam message ' + str(i+1) + " " + custom_message
        payload = {
            'message': text,
            'access_token': access_t_page,
        }
        requests.post(post_url, data = payload)
        print("success")
    print('script complete')


# Two ways of getting a single post (requires the post ID)

def display_my_facebook_post(request, *args, **kwargs): # Using chatGTP - USES python-facebook-api and cURL (request/transfer data over URL)
    # https://pypi.org/project/python-facebook-api

    url = f'https://graph.facebook.com/v13.0/{post_id}?access_token={long_term_user_access_token}'
    response = requests.get(url)

    if response.status_code == 200: #
        post_data = response.json()
        context = {
            'post_data': post_data,
        }
        return render(request, 'facebook_post.html', context)
    else:
        return HttpResponse("Failed to retrieve the post")

def refresh_page_token():
    user_graph_url = f'https://graph.facebook.com/v13.0/me/accounts?access_token={long_term_user_access_token}'
    response = requests.get(user_graph_url)
    data = response.json()
    page_id = None
    for page in data['data']:  # Parses json response
        if page['name'] == page_name:
            page_id = page['id']  # Required in order to check conversations
            page_token = page['access_token']  # Grab Page Access Token (it is temporary!)
            break
