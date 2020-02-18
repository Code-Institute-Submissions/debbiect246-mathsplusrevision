'''
render library imported from django
Product model imported into search app as this will 
be searched for a product.
'''
from django.shortcuts import render
from products.models import Product


# Create your views here.
'''
this function does the search so that when user presses
search button item is found from products model, or nothing is returned if item
is not in product model.
'''


def do_search(request):
    products = Product.objects.filter(name__icontains=request.GET['q'])
    return render(request, "products.html", {"products": products})
