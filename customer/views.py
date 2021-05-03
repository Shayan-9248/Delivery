from django.shortcuts import render
from django.views import View
from .models import (
    MenuItem,
    OrderModel
)
from django.http import HttpResponse
from zeep import Client


class Index(View):
    template_name = 'customer/index.html'

    def get(self, request):
        return render(request, self.template_name)


class Order(View):
    def get(self, request):
        # get every item for each context
        appetizers = MenuItem.objects.filter(category__title__icontains='Appetizer')
        drinks = MenuItem.objects.filter(category__title__icontains='Drink')
        main_foods = MenuItem.objects.filter(category__title__icontains='Main Food')
        desserts = MenuItem.objects.filter(category__title__icontains='Dessert')
        context = {
            'appetizers': appetizers,
            'drinks': drinks,
            'main_foods': main_foods,
            'desserts': desserts,
        }
        return render(request, 'customer/order.html', context)
    
    def post(self, request):
        name = request.POST['name']
        email = request.POST['email']
        phone = request.POST['phone']
        address = request.POST['address']
        order_items = {
            'items': []
        }
        items = request.POST.getlist('items[]')
        for item in items:
            menu_item = MenuItem.objects.get(id__contains=int(item))
            item_data = {
                'id': menu_item.id,
                'name': menu_item.name,
                'price': menu_item.price
            }
            order_items['items'].append(item_data)

            price = 0
            item_ids = []
        
        for item in order_items['items']:
            price += item['price']
            item_ids.append(item['id'])

        order = OrderModel.objects.create(
            user=request.user,
            price=price,
            name=name,
            email=email,
            phone=phone,
            address=address
        )
        order.items.add(*item_ids)

        context = {
            'items': order_items['items'],
            'price': price,
            'order': order
        }
        return render(request, 'customer/order_confirm.html', context)


MERCHANT = 'XXXXXXXX-XXXX-XXXX-XXXX-XXXXXXXXXXXX'
client = Client('https://www.zarinpal.com/pg/services/WebGate/wsdl')
description = ""  # Required
mobile = '09123456789'  # Optional
CallbackURL = 'http://localhost:8000/verify/' # Important: need to edit for realy server.


def send_request(request, price, order_id):
    global amount, o_id
    amount = price
    o_id = order_id
    result = client.service.PaymentRequest(MERCHANT, amount, description, request.user.email, mobile, CallbackURL)
    if result.Status == 100:
        return redirect('https://www.zarinpal.com/pg/StartPay/' + str(result.Authority))
    else:
        order = OrderModel.objects.get(id=o_id)
        order.is_paid = True
        order.save()
        return HttpResponse('Error code: ' + str(result.Status))


def verify(request):
    if request.GET.get('Status') == 'OK':
        result = client.service.PaymentVerification(MERCHANT, request.GET['Authority'], amount)
        if result.Status == 100:
            return HttpResponse('Transaction success.\nRefID: ' + str(result.RefID))
        elif result.Status == 101:
            return HttpResponse('Transaction submitted : ' + str(result.Status))
        else:
            return HttpResponse('Transaction failed.\nStatus: ' + str(result.Status))
    else:
        return HttpResponse('Transaction failed or canceled by user')


class History(View):
    template_name = 'customer/history.html'

    def get(self, request):
        orders = OrderModel.objects.filter(user_id=request.user.id)
        return render(request, self.template_name, {'orders': orders})