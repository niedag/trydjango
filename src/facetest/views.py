import requests
import facebook # from facebook-sdk package

from pyfacebook import GraphAPI #What is this and how is it different from other packages?

from django.shortcuts import render
from django.http import HttpResponse
from django.conf import settings

access_t = 'EAAVacs9AvhEBO8FfsYkE9KFjZByjBqv36u5dQPjPemywZAypkqDr7I1edIx0E6kbBFimICWv9TEWyYrHcvFBmiQtHXPQsY1wU6XufviVV7A9uGxRCIVV7bW8nn1tEY8VA39KachRLvpBET3W3MlAFcdd5SDcZAVEtd8s4qy2NewZBevO9HurufS1'
post_id = "2553705538124434_2552109628284025"


def facehome_view(request, *args, **kwargs):
    graph = facebook.GraphAPI(access_token=access_t, version='3.1')
    post = graph.get_object(id=post_id, fields="message")
    # print(post['message'])
    all_posts_ids = ['2553705538124434_2552109628284025',
                     '2553705538124434_2555396167955371',
                     '2553705538124434_2555404161287905']
    field_list = 'id, message, created_time'
    all_posts = graph.get_objects(ids=all_posts_ids, fields="message")

    my_context = {
        "my_text": "This is an example context variable",
        "my_post": post['message'],
        "all_posts": all_posts['message'],
    }
    # graph.put_object("me", "feed", message = "Hello World")

    return render(request, "facetest3.html", my_context)

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

