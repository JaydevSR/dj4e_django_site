from django.shortcuts import render
from django.http import HttpResponse


def index(request):
    num_visits = request.session.get('num_visits', 0) + 1
    request.session['num_visits'] = num_visits
    if num_visits > 4:
        del request.session['num_visits']
    resp = HttpResponse('view count=' + str(num_visits) + '<p>Code for dj4e: fb3ea77a<p>')
    resp.set_cookie('dj4e_cookie', 'fb3ea77a', max_age=1000)
    return resp
