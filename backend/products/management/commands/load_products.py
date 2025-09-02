from django.core.management.base import BaseCommand
from products.models import Product

class Command(BaseCommand):
    help = 'Load sample products'

    def handle(self, *args, **options):
        products = [
            {
                'name': 'Classic Cotton T-Shirt',
                'description': 'Comfortable 100% cotton t-shirt perfect for everyday wear.',
                'price': 19.99,
                'category': 'T-Shirts',
                'image': 'https://images.unsplash.com/photo-1521572163474-6864f9cf17ab?w=400&h=400&fit=crop',
                'stock': 50,
                'featured': True
            },
            {
                'name': 'Denim Jacket',
                'description': 'Stylish denim jacket with a modern fit.',
                'price': 79.99,
                'category': 'Jackets',
                'image': 'https://images.unsplash.com/photo-1544966503-7cc5ac882d5f?w=400&h=400&fit=crop',
                'stock': 25,
                'featured': True
            },
            {
                'name': 'Slim Fit Jeans',
                'description': 'Premium quality slim fit jeans with stretch comfort.',
                'price': 59.99,
                'category': 'Jeans',
                'image': 'https://images.unsplash.com/photo-1542272604-787c3835535d?w=400&h=400&fit=crop',
                'stock': 30,
                'featured': False
            },
            {
                'name': 'Casual Button Shirt',
                'description': 'Versatile button-up shirt suitable for work or casual wear.',
                'price': 39.99,
                'category': 'Shirts',
                'image': 'https://images.unsplash.com/photo-1596755094514-f87e34085b2c?w=400&h=400&fit=crop',
                'stock': 40,
                'featured': True
            },
            {
                'name': 'Summer Dress',
                'description': 'Light and breezy summer dress perfect for warm weather.',
                'price': 49.99,
                'category': 'Dresses',
                'image': 'https://images.unsplash.com/photo-1595777457583-95e059d581b8?w=400&h=400&fit=crop',
                'stock': 20,
                'featured': True
            },
            {
                'name': 'Hoodie Sweatshirt',
                'description': 'Cozy hoodie sweatshirt for casual comfort.',
                'price': 45.99,
                'category': 'Hoodies',
                'image': 'https://images.unsplash.com/photo-1556821840-3a63f95609a7?w=400&h=400&fit=crop',
                'stock': 35,
                'featured': False
            }
        ]
        
        for product_data in products:
            Product.objects.get_or_create(
                name=product_data['name'],
                defaults=product_data
            )
        
        self.stdout.write('Sample products loaded successfully')