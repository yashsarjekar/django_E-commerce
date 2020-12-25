from django.shortcuts import render, redirect,HttpResponseRedirect
from django.http import HttpResponse
from django.contrib.auth.hashers import make_password, check_password
from .models import Customer
from django.views import View
# Create your views here.
class Register(View):
    def get(self, request):
        return render(request,'register.html',{})
    
    def post(self, request):
        email = request.POST.get('email')
        password = request.POST.get('password')
        confirm_password = request.POST.get('confirm_password')
        if password != confirm_password:
            err = "Password Does not Match"
            return render(request, 'register.html',{'err':err})
        else:
            email_err = Customer.check_user_exist(email)
            if email_err == True:
                hash_password = make_password(password)
                new_cust = Customer(email=email,password=hash_password)
                new_cust.save()
                success_msg = "Successfully Created Account"
                return render(request, 'register.html',{'success_msg':success_msg})

            else:
                return render(request, 'register.html',{'err':email_err})

    
class Login(View):
    returnURL = None
    def get(self,request):
        Login.returnURL = request.GET.get('return_url')
        return render(request,'login.html',{})
    
    def post(self,request):
        email = request.POST.get("email")
        password = request.POST.get("password")
        try:
            customer = Customer.objects.get(email=email)
            msg = ""
            if customer:
                result = check_password(password,customer.password)
                if result == True:
                    msg = "Authentication Successful"
                    request.session['customer_id'] = customer.id
                    request.session['email'] = customer.email
                    if Login.returnURL:
                        return HttpResponseRedirect(Login.returnURL)
                    else:
                        Login.returnURL = None
                        return redirect('home_page')
                else:
                    msg = "Password Incorrect"
                    return render(request,'login.html',{'err':msg})
            else:
                msg = "User is Not Registered"
                return render(request,'login.html',{'err':msg})
        except Customer.DoesNotExist:
            msg = "User is Not Registered"
            return render(request,'login.html',{'err':msg})
    
def logout(request):
    request.session.clear()
    return redirect('home_page')

