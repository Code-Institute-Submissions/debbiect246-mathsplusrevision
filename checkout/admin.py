from django.contrib import admin
from .models import Order, OrderLineItem

# register the orderline model which records orders.-->


class OrderLineAdminInline(admin.TabularInline):
    model = OrderLineItem


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineAdminInline, )


admin.site.register(Order, OrderAdmin)
