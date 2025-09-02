from rest_framework import generics, permissions, status
from rest_framework.response import Response
from rest_framework.views import APIView
from .models import Wishlist, Product
from .serializers import ProductSerializer

class WishlistView(APIView):
    permission_classes = [permissions.IsAuthenticated]
    
    def get(self, request):
        wishlist_items = Wishlist.objects.filter(user=request.user).select_related('product')
        data = []
        for item in wishlist_items:
            data.append({
                'id': item.id,
                'product': ProductSerializer(item.product).data
            })
        return Response(data)
    
    def post(self, request):
        product_id = request.data.get('product_id')
        try:
            product = Product.objects.get(id=product_id)
            wishlist_item, created = Wishlist.objects.get_or_create(
                user=request.user,
                product=product
            )
            if created:
                return Response({'message': 'Added to wishlist'}, status=status.HTTP_201_CREATED)
            else:
                return Response({'message': 'Already in wishlist'}, status=status.HTTP_200_OK)
        except Product.DoesNotExist:
            return Response({'error': 'Product not found'}, status=status.HTTP_404_NOT_FOUND)
    
    def delete(self, request):
        product_id = request.data.get('product_id')
        try:
            wishlist_item = Wishlist.objects.get(user=request.user, product_id=product_id)
            wishlist_item.delete()
            return Response({'message': 'Removed from wishlist'}, status=status.HTTP_200_OK)
        except Wishlist.DoesNotExist:
            return Response({'error': 'Item not in wishlist'}, status=status.HTTP_404_NOT_FOUND)