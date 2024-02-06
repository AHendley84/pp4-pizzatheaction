from django.contrib import admin
from .models import Order, OrderLineItem


# Register your models here.
class OrderLineItemAdminInline(admin.TabularInline):
    model = OrderLineItem
    readonly_fields = ('line_item_total',)


class OrderAdmin(admin.ModelAdmin):
    inlines = (OrderLineItemAdminInline,)

    readonly_fields = ('order_number', 'order_date', 
                       'delivery_charge', 'order_total',
                       'grand_total',)
    
    list_display = ('order_number', 'order_date', 'full_name',
                    'order_total', 'delivery_charge',
                    'grand_total',)
    
    ordering = ('-order_date',)

admin.site.register(Order, OrderAdmin)