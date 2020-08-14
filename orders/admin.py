from django.contrib import admin
from .models import Category, Size, Topping, Extra, Itemfororder, Orderhistory


admin.site.register(Category)
admin.site.register(Size)
admin.site.register(Topping)
admin.site.register(Extra)
admin.site.register(Itemfororder)
admin.site.register(Orderhistory)
