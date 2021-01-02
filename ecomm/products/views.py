from django.shortcuts import render,redirect
from django.http import HttpResponse
from .models import Product
from categories.models import Categories
from django.views import View
# Create your views here.
class Index(View):

    def get(self,request):
        cart = request.session.get('cart')
        prod_id = request.GET.get('details')
        if prod_id:
            try:
                product = Product.objects.get(id = prod_id)
                #print(product)
                if product:
                    return render(request,'details.html',{'product':product})
                else:
                    msg = 'The Page you are Trying to Access is Not Possible'
                    return render(request,'details.html',{'msg':msg})
            except Product.DoesNotExist:
                msg = 'The Page you are Trying to Access is Not Possible'
                return render(request,'details.html',{'msg':msg})
        if not cart:
            request.session['cart'] = {}
        prod = None
        cat = Categories.get_categories()
        category_id = request.GET.get('Category')
        if category_id:
            prod = Product.get_product_by_category(category_id)
        else:
            prod = Product.get_products() 
        #print(cat)
        #print(request.session.get('email'))
        return render(request, 'index.html',{'products' : prod,'categories' : cat})

    def post(self,request):
        prod_id = request.POST.get('prod_id')
        remove = request.POST.get('remove')
        #print(prod_id)
        cart = request.session.get('cart')
        if cart:
            quantity = cart.get(prod_id)
            if quantity:
                if remove:
                    if quantity == 1:
                        cart.pop(prod_id)
                    else:
                        cart[prod_id] = quantity - 1
                else:
                    cart[prod_id] = quantity + 1
            else:
                cart[prod_id] = 1
        else:
            cart = {}
            cart[prod_id] = 1
        request.session['cart'] = cart
        print(request.session['cart'])
        return redirect("home_page")

class Cart(View):

    def get(self,request):
        cart = request.session.get('cart').keys()
        cart_products = Product.get_product_by_ids(cart)
        print(cart_products)
        return render(request,'cart.html',{'products':cart_products})

    def post(self,request):
        pass

class Detail(View):
    def get(self,request):
        pass
    def post(self,request):
        pass
    