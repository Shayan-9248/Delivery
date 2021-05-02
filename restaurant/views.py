from django.shortcuts import render
from django.views import View
from django.utils.timezone import datetime
from customer.models import (
    MenuItem,
    OrderModel
)

class Dashboard(View):
    template_name = 'restaurant/dashboard.html'

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