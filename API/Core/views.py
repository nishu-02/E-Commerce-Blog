from django.shortcuts import render
from django.http import HttpResponse
from .models import Product, Contact, Order, OrderUpdate
from math import ceil
import json

# Create your views here.
def index(request):
    allProds = []
    # products = Product.objects.all()
    # n = len(products)
    # nSlides = n // 4 + ceil((n / 4) - (n // 4))
    # allProds.append([products, range(1, nSlides), nSlides])

    # Displaying the products in the categories
    catprods = Product.objects.values('category', 'product_id')
    cats = {item['category'] for item in catprods} # so this the set means getting the unique categories

    for cat in cats:
        prod = Product.objects.filter(category=cat)
        n = len(prod)
        nSlides = n // 4 + ceil((n / 4) - (n // 4))
        allProds.append([prod, range(1, nSlides), nSlides])

    return render(request, 'Core/index.html', {'allProds': allProds})

def contact(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        phone = request.POST.get('phone')
        desc = request.POST.get('desc')
        print(name, email, phone, desc)

        # Save the data to the database or send an email
        contact = Contact(name=name, email=email, phone=phone, desc=desc)
        contact.save() # saving the data to the database

    return render(request, 'Core/contact.html')

def about(request):
    return render(request, 'Core/about.html')

def tracker(request):

    if request.method == "POST":
        orderId  = request.POST.get('orderId')
        email = request.POST.get('email')

        try:
            order = Order.objects.filter(order_id= orderId, email=email)
            if(len(order) > 0):
                update = OrderUpdate.objects.filter(order_id=orderId)
                updates = []
                for item in update:
                    updates.append({ 'text': item.update_desc, 'time': item.timestamp})
                    response = json.dumps(updates, default=str) # converting the updates to json format or to make it serializable
                return HttpResponse(response)
            else:
                return HttpResponse('{"status":"noitem"}') # if the order is not found
        
        except Exception as e:
            return HttpResponse('{"status":"error"}')

    return render(request, 'Core/tracker.html')

def productView(request, id):
    # Fetch the product using the id
    product = Product.objects.filter(product_id=id)[0]
    print(product)
    return render(request, 'Core/prodview.html', {'product': product}) # inside the '' is the name by which we want to call the product

def checkout(request):

    if request.method == "POST":
        name = request.POST.get('name')
        email = request.POST.get('email')
        address = request.POST.get('address')
        city = request.POST.get('city')
        state = request.POST.get('state')
        zip_code = request.POST.get('zip_code')
        phone = request.POST.get('phone')

        order = Order(name=name, email=email, address=address, city=city, state=state, zip_code=zip_code, phone=phone)
        order.save() # Save the order to the database or send an email
        update = OrderUpdate(order_id = ordeer.order_id, update_desc="The order has been placed")
        update.save()
        thank = True
        id = order.order_id
        return render(request, 'Core/checkout.html', {'thank': thank, 'id': id}) # thank is a boolean variable to show the thank you message

    # return render(request, 'Core/checkout.html')

def search(request):
    return render(request, 'Core/search.html')