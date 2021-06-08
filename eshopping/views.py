from django.shortcuts import render
from .models import Products

# Create your views here.
def home(request):
    prod = Products()
    prod.name = "Blue jacket"
    prod.price = 25
    prod.image = 'product1.jpg'

    prod2 = Products()
    prod2.name = "Black Tshirt"
    prod2.price = 30
    prod2.image = 'product2.jpg'

    prod3 = Products()
    prod3.name = "Black Dress"
    prod3.price = 40
    prod3.image = 'product3.jpg'

    prods = Products.objects.all()
    # prods = [prod, prod2, prod3]
    return render(request,'index.html', {'prods':prods})