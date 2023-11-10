import requests
import facebook # from facebook-sdk package

from pyfacebook import GraphAPI #What is this and how is it different from other packages?

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import FacebookPostForm

# TODO: Auto update access_t_page with access_t (long-term) ALSO work on parsing cURL responses for conversations, acess tokens, etc.

access_t = 'EAAVacs9AvhEBO8FfsYkE9KFjZByjBqv36u5dQPjPemywZAypkqDr7I1edIx0E6kbBFimICWv9TEWyYrHcvFBmiQtHXPQsY1wU6XufviVV7A9uGxRCIVV7bW8nn1tEY8VA39KachRLvpBET3W3MlAFcdd5SDcZAVEtd8s4qy2NewZBevO9HurufS1'

# Access token for Page posts: me/accounts --> access token
access_t_page = 'EAAVacs9AvhEBO16KR2ZCzg1k1ZB7hoAsAxZBhtVwFRCHMiCnHo17kG0keomsLkVQVRudKVZAYbfwD9wbq08jLPbAMNLx9q8ZA8j9Y8QaMruzZCMjZC7o4JLXvmgbWFBgANzbkQDpZA7PmLuLkcKQ6SJNDjJ4YZA22DvmZBQa7cdL1V77MBvEtw3HGnE5Nv1y43EaNSL7PuaxJREbekFr4VulXxuCml'

post_id = "2553705538124434_2552109628284025" # page#_post#
page_id = "155168831017376"
post_url = 'https://graph.facebook.com/{}/feed'.format(page_id)

def facepost_view(request):
    if request.method == 'POST':
        postform = FacebookPostForm(request.POST)
        if postform.is_valid():
            text = postform.cleaned_data['text']
            payload = {
                'message': text,
                'access_token': access_t_page
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
    context = {
        "postform": postform,
    }
    return render(request, 'facetest/facebook-post.html', context)

def spam_post_test(custom_message, spamNum):
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

def facetest_view(request, *args, **kwargs):
    graph = facebook.GraphAPI(access_token=access_t, version='3.1')
    post = graph.get_object(id=post_id, fields="message")
    print(post['message'])

    my_context = {
        "post": post,
        "my_text": "This is an example context variable",
        "my_post": post['message'],
    }
    # graph.put_object("me", "feed", message = "Hello World")

    return render(request, "facetest/facetest.html", my_context)

def display_my_facebook_post(request, *args, **kwargs): # Using chatGTP - USES python-facebook-api and cURL (request/transfer data over URL)
    # https://pypi.org/project/python-facebook-api

    url = f'https://graph.facebook.com/v13.0/{post_id}?access_token={access_t}'
    response = requests.get(url)

    if response.status_code == 200: #
        post_data = response.json()
        context = {
            'post_data': post_data,
        }
        return render(request, 'facebook_post.html', context)
    else:
        return HttpResponse("Failed to retrieve the post")

