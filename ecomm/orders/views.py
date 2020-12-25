from django.shortcuts import render,redirect
from django.views import View
from .models import Order
from products.models import Product
from customers.models import Customer
#from products.middleware.auth import auth_middleware
#from django.utils.decorators import method_decorator
# Create your views here.
class Checkout(View):
    def get(self,request):
        pass
    def post(self,request):
        address = request.POST.get('address')
        mob_no = request.POST.get('mobile')
        cart = request.session.get('cart')
        customer_id = request.session.get('customer_id')
        products = Product.get_product_by_ids(list(cart.keys()))
        for product in products:
            new_order = Order(product = Product(id = product.id),
            customer = Customer(id = customer_id),
            quantity = cart.get(str(product.id)),
            price = product.price,
            address = address,
            mob_no = mob_no,
            )
            new_order.save()
        request.session['cart'] = {}
        return redirect('cart')

class Orders(View):
    #@method_decorator(auth_middleware)
    def get(self,request):
        customer_id = request.session.get('customer_id')
        if customer_id:
            try:
                orders = Order.objects.filter(customer = customer_id).order_by('-datetime')
                print(orders)
                if orders:
                    return render(request,'orders.html',{'orders':orders})
                else:   
                    return render(request,'orders.html',{})
            except Order.DoesNotExist:
                return render(request,'orders.html',{})
    def post(self,request):
        pass