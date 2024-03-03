# from django.shortcuts import render


# Create your views here.
# these are just copy pasted..check it again
# from rest_framework.response import Response
# from rest_framework.views import APIView
#from rest_framework import generics
from .models import Order
from .serializes import OrderSerializer
from product.models import Product
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from rest_framework.response import Response
from rest_framework.decorators import api_view
# class OrderListView(APIView):
#     def get(self, request):
#         orders = Order.objects.all()
#         serializer = OrderSerializer(orders, many=True)
#         return Response(serializer.data)

# class OrderListView(generics.ListAPIView):
#     queryset = Order.objects.all()
#     serializer_class = OrderSerializer

@csrf_exempt
@api_view(['POST'])
def create(request):
    if request.method== 'POST':
        data={'product':1,'o_qty':2}
        product_id=data['product']
        qty=data['o_qty']

        product =Product.objects.get(p_id=product_id)
        if product:
            # Calculate unit price and total price
            unit_price = product.p_price
            total_price = unit_price *qty
            
            # Create a new order instance
            order = Order.objects.create(
                product=product,
                o_qty=qty,
                unit_price=unit_price,
                total_price=total_price
            )
            order=Order.objects.all()
            data=OrderSerializer(order,many=True)
            return Response(data.data)
        else:
            return Response({'success':False,'message':'order creation failed'})

        

