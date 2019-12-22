from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """A View that renders the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """Add a quantity of the specified product to the cart"""
    try:
        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', {})
        cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except ValueError:
        messages.error(request, "You must chose a quantity for this paper, ")
        messages.error(
            request, "select the papers tab and choose a quanity to order.")
        return render(request, "cart.html")


def adjust_cart(request, id):
    """
    Adjust the quantity of the specified product to the specified
    amount
    """
    quantity = int(request.POST.get('quantity'))
    cart = request.session.get('cart', {})

    if quantity > 0:
        cart[id] = quantity

    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
