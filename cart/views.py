from django.shortcuts import render, redirect, reverse
from django.contrib import messages

# Create your views here.


def view_cart(request):
    """shows the cart contents page"""
    return render(request, "cart.html")


def add_to_cart(request, id):
    """
    Add a paper to the cart
     try except loop ensures that user can only enter an integer quantity
    """

    try:
        quantity = int(request.POST.get('quantity'))

        cart = request.session.get('cart', {})
        cart[id] = cart.get(id, quantity)

        request.session['cart'] = cart
        return redirect(reverse('view_cart'))

    except ValueError:
        messages.warning(request, "You must chose a quantity for this paper, ")
        messages.warning(
            request, "select the papers tab and choose a quantity to order.")
        return render(request, "cart.html")


def adjust_cart(request, id):
    """
    User can change their mind about the number of papers they want and
    this is changed on the cart
    """

    # post the amount to the cart and show result on screen
    # try except loop means user must select an integer value for the items
    # no other type of value will be accepted

    try:
        quantity = int(request.POST.get('quantity'))
        cart = request.session.get('cart', {})
    except ValueError:
        messages.warning(
            request, "You must chose an ammended quantity for this paper, ")
        messages.warning(
            request, "select a whole number of papers in the amend box please.")
        return render(request, "cart.html")

    ''' checks to see that quantity ordered is greater than 0 then puts items
    into cart ready for checkout then display the cart page with amended order included.
    '''
    if quantity > 0:
        cart[id] = quantity

    else:
        cart.pop(id)

    request.session['cart'] = cart
    return redirect(reverse('view_cart'))
