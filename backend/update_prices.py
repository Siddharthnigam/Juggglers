import os
import django
import random

os.environ.setdefault('DJANGO_SETTINGS_MODULE', 'backend.settings')
django.setup()

from products.models import Product

products = Product.objects.all()
for product in products:
    old_price = product.price
    product.price = random.randint(500, 1000)
    product.save()
    print(f'Updated {product.name}: ${old_price} -> Rs.{product.price}')

print(f'\nUpdated {products.count()} products with prices between Rs.500-1000')