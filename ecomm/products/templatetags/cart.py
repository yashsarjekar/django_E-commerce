from django import template

register = template.Library()

@register.filter(name='is_in_cart')
def is_in_cart(product,cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return True
    return False

@register.filter(name='cart_count')
def cart_count(product,cart):
    keys = cart.keys()
    for key in keys:
        if int(key) == product.id:
            return cart.get(key)
    return False

@register.filter(name='total_price')
def total_price(product,cart):
    return product.price * cart_count(product,cart)

@register.filter(name="total")
def total(products,cart):
	sum = 0
	for product in products:
		sum += total_price(product,cart)
	return "₹"+str(sum) 
@register.filter(name="currency")
def currency(number):
	return "₹"+str(number)  

@register.filter(name="multiply")
def multiply(number1,number2):
	return number1 * number2