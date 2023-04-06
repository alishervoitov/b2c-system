from django.contrib import admin
from product.models import Category, Product, Comment, Rating, RatingStar

admin.site.register(Category)
admin.site.register(Product)
admin.site.register(Comment)
admin.site.register(Rating)
admin.site.register(RatingStar)