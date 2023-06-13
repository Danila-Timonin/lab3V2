from django.contrib import admin
from .models import Visitor, Store, Purchase, Product, Review
# Register your models here.


admin.site.register(Visitor)
admin.site.register(Store)
admin.site.register(Purchase)
admin.site.register(Product)
admin.site.register(Review)

