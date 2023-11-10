import requests
import facebook # from facebook-sdk package

from pyfacebook import GraphAPI #What is this and how is it different from other packages?

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

from .forms import FacebookPostForm

access_t = 'EAAVacs9AvhEBO8FfsYkE9KFjZByjBqv36u5dQPjPemywZAypkqDr7I1edIx0E6kbBFimICWv9TEWyYrHcvFBmiQtHXPQsY1wU6XufviVV7A9uGxRCIVV7bW8nn1tEY8VA39KachRLvpBET3W3MlAFcdd5SDcZAVEtd8s4qy2NewZBevO9HurufS1'

# Access token for Page posts: me/accounts --> access token
access_t_page = 'EAAVacs9AvhEBO9jjVbsiR86SrXlccuL3xv7FcpjjrLZB3ne77xZCP2Kgdi6uUVvTC0f1z1UFbUO0aqDrj7X9YCcySSd4DPCk2NUnqvqSnZBcyZBirw2nyPcG6ZANuInlHI9RO6PvslZAa6Q48pZCCnjJmaXTZAlixvDz6A0EX3bDljNIF4k4ZCHgmbx09m6yR3AF8lzKM6fVMY93HrZCZAZCKARKqmoZD'

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
            if response.status_code == 200:
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

