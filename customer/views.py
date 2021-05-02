from django.shortcuts import render
from django.views import View
from .models import (
    MenuItem,
    OrderModel
)


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
            'form': form
        }
        return render(request, 'customer/order_confirm.html', context)