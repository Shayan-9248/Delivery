from django.shortcuts import render
from django.contrib.auth.mixins import LoginRequiredMixin
from django.views import View
from django.utils.timezone import datetime
from customer.models import (
    MenuItem,
    OrderModel
)
from .mixins import (
    AccessMixin
)

class Dashboard(LoginRequiredMixin, AccessMixin, View):
    template_name = 'restaurant/dashboard.html'
    login_url = 'account:sign-in'

    def get(self, request):
        today = datetime.today()
        orders = OrderModel.objects.filter(
            created__year=today.year,
            created__month=today.month,
            created__day=today.day
        )
        unship_orders = []
        total_revenue = 0
        for order in orders:
            total_revenue += order.price

            if not order.is_shipped:
                unship_orders.append(order)
        
        context = {
            'orders': unship_orders,
            'total_revenue': total_revenue,
            'total_orders': len(orders)
        }
        return render(request, self.template_name, context)


class OrderDetail(View):
    template_name = 'restaurant/detail.html'

    def get(self, request, id):
        order = OrderModel.objects.get(id=id)
        return render(request, self.template_name, {'order': order})
    
    def post(self, request, id):
        order = OrderModel.objects.get(id=id)
        order.is_shipped = True
        order.save()
        return render(request, self.template_name, {'order': order})