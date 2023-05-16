from django.shortcuts import render
from rest_framework.decorators import api_view
from rest_framework import serializers
from rest_framework.response import Response
from .models import Product


def Product_view(request):
    context = {}
    return render(request, 'product/product.html', context=context)


@api_view(["GET"])
def HomeProductApi(request):
    products = Product.objects.all()
    serializer = HomeProductSerializer(products, many=True)
    return Response(serializer.data)


class HomeProductSerializer(serializers.ModelSerializer):
    class Meta:
        model = Product
        fields = [
            'id',
            'name',
            'price',
            'image',
        ]
