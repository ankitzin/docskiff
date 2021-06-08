from django.shortcuts import render
from .models import Products

# Create your views here.
def home(request):
    """
    method is displaying the data into index.html file.

    :param
        prods: querylists of Products data

    """
    prods = Products.objects.all()
    return render(request,'index.html', {'prods':prods})