from rest_framework import serializers
from .models import Order, Product
# these are just copy pasted..check it again

class OrderSerializer(serializers.ModelSerializer):

    class Meta:
        model = Order
        fields = "__all__"
