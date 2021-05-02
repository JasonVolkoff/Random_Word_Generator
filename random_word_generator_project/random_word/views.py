from django.shortcuts import render, redirect
from django.utils.crypto import get_random_string

# Create your views here.


def index(request):
    # initialize variables if not in session
    if "counter" not in request.session or "randomWord" not in request.session:
        request.session["counter"] = 0
        request.session["randomWord"] = "Click below for a random string."
    return render(request, 'index.html')


def random_word(request):
    if request.method == "POST":
        # increment counter and assign random string to session
        request.session['counter'] += 1
        request.session['randomWord'] = get_random_string(length=14)
    return redirect('/')


def reset(request):
    # reset session variables
    request.session.flush()
    return redirect('/')
