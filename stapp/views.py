from django.shortcuts import render
from django.http import HttpResponse
from django.contrib.auth.models import User
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login, logout

from stapp import models as M


def index(request):
    all_stacks = M.Stack.objects.values()
    return render(request, 'index.html', dict(stacks=all_stacks))


# Auth Views #


def signup(request):
    if request.method == "POST":
        try:
            user = User.objects.create_user(
                request.POST['username'],
                request.POST['email'],
                request.POST['password'])
            return HttpResponse('{} Created!'.format(user.username), status=201)
        except Exception:
            return HttpResponse('Error creating user.', status=500)
    else:
        return render(request, 'signup.html')


def login_user(request):
    if request.method == "POST":
        username = request.POST['username']
        password = request.POST['password']
        user = authenticate(username=username, password=password)
        if user is not None:
            if user.is_active:
                login(request, user)
                # Redirect to a success page
                return HttpResponse('Logged in!', status=200)
            else:
                return HttpResponse('This user is disabled.', status=500)
        else:
            return HttpResponse('Invalid Login.', status=401)
    else:
        return render(request, 'login.html')


def logout_user(request):
    logout(request)
    return HttpResponse('Logged out!', status=200)


# Stack Views #


def view_stack(request, stack_name):
    stack = M.Stack.objects.get(name=stack_name)
    ingredients = M.Ingredients.objects.get(stack_id=stack._id)
    return render(
        request,
        'details.html',
        dict(stack=stack, ingredients=ingredients.all_ingredients()))


@login_required
def create_stack(request):
    if request.method == "POST":
        fresh_stack = M.Stack()
        fresh_stack.name = request.POST['name']
        fresh_stack.description = request.POST['description']
        fresh_stack.user_id = '73f8558f-765c-47b3-b2fa-b9d32b5608df'  # for testing
        fresh_stack.save()
        return HttpResponse('Created!', status=201)
    else:
        return render(request, 'create.html')


@login_required
def upvote_stack(request):
    pass


@login_required
def downvote_stack(request):
    pass


@login_required
def favorite_stack(request):
    pass
