'''
all django bits imported here so that checkout app can run.
render, login, messages, django.contrib.auth libraries imported.
Then order form and order line item are imported from the checkouy
forms and models. Finally stripe is imported together with the user
profile and models from the product app.
'''

from django.shortcuts import render, get_object_or_404, reverse, redirect
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from .forms import MakePaymentForm, OrderForm
from .models import OrderLineItem, Order
from django.conf import settings
from django.utils import timezone
from products.models import Product
from accounts.models import UserProfile
import stripe

# Create your views here.
stripe.api_key = settings.STRIPE_SECRET

'''decorator for checkout - controls what happens when user checks out items.
So if checkout request is valie then it is posted to orders model and
payment can be made by the user via stripe.  If the order is not valid then
an error message is shown indicating that there is a problem with the credit
card used.  All orders are saved with a date stamp and users are shown details of
each order made via the product app.
'''


@login_required()
def checkout(request):
    if request.method == "POST":
        order_form = OrderForm(request.POST)
        payment_form = MakePaymentForm(request.POST)

        if order_form.is_valid() and payment_form.is_valid():

            order = order_form.save(commit=False)
            order.date = timezone.now()
            order.save()
            # creates new instance of Order, and attaches the logged in user profile to it

            cart = request.session.get('cart', {})
            total = 0
            for id, quantity in cart.items():
                product = get_object_or_404(Product, pk=id)
                total += quantity * product.price
                order_line_item = OrderLineItem(
                    order=order,
                    product=product,
                    quantity=quantity
                )
                order_line_item.save()

            try:
                customer = stripe.Charge.create(
                    amount=int(total * 100),
                    currency="EUR",
                    description=request.user.email,
                    card=payment_form.cleaned_data['stripe_id']
                )
            except stripe.error.CardError:
                messages.error(request, "Your card was declined!")

            if customer.paid:
                messages.error(request, "You have successfully paid")
                request.session['cart'] = {}
                return redirect(reverse('products'))
            else:
                messages.error(request, "Unable to take payment")
        else:
            print(payment_form.errors)
            messages.error(
                request, "We were unable to take a payment with that card!")
    else:
        payment_form = MakePaymentForm()
        order_form = OrderForm()

    return render(request, "checkout.html", {"order_form": order_form, "payment_form": payment_form, "publishable": settings.STRIPE_PUBLISHABLE})
