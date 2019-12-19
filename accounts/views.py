from django.shortcuts import render, redirect, HttpResponseRedirect
from django.contrib import messages, auth
from django.urls import reverse
from .forms import UserLoginForm, UserRegistrationForm
from django.template.context_processors import csrf
from django.contrib.auth.decorators import login_required
from checkout.models import OrderLineItem
from products.models import Product
from accounts.models import UserProfile
from checkout.models import Order


# Create your views here.

def all_products(request):
    products = Product.objects.all()
    return render(request, "products.html", {"products": products})


def index(request):
    """A view that displays the index page"""
    return render(request, "index.html")


def logout(request):
    """A view that logs the user out and redirects back to the index page"""
    auth.logout(request)
    messages.success(request, 'You have successfully logged out')
    return redirect(reverse('index'))


def login(request):
    """A view that manages the login form"""
    if request.method == 'POST':
        # user_form = UserLoginForm(request.POST)
        login_form = UserLoginForm(request.POST)
        # if user_form.is_valid():
        if login_form.is_valid():
            # log in the user
            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password'])
            if user:
                auth.login(user=user, request=request)
                messages.error(
                    request, " Welcome you have successfully logged in")
                return redirect(reverse('index'))
            else:
                # user_form.add_error(
                login_form.add_error(
                    None, "Your username or password are incorrect")
    else:
        # user_form = UserLoginForm()
        login_form = UserLoginForm()

    args = {'login_form': login_form}
    return render(request, 'login.html', args)


@login_required
def profile(request):
    """A view that displays the profile page of a logged in user"""
    user = request.user
    if user.is_authenticated:
        ''' get the list of items that the user has purchased.'''
        profile = UserProfile.objects.get(user=user)
        orders = Order.objects.filter(userprofile=profile)
        orders = OrderLineItem.objects.all()

        print(orders)

    return render(request, 'profile.html', {'orders': orders})


def register(request):
    """A view that manages the registration form"""
    if request.method == 'POST':
        user_form = UserRegistrationForm(request.POST)
        if user_form.is_valid():
            user_form.save()

            user = auth.authenticate(username=request.POST['username'],
                                     password=request.POST['password1'])

            if user:
                auth.login(user=user, request=request)
                messages.success(request, "You have successfully registered")
                return redirect(reverse('index'))

            else:
                messages.error(request, "unable to log you in at this time!")
    else:
        user_form = UserRegistrationForm()

    args = {'user_form': user_form}
    return render(request, 'register.html', args)
