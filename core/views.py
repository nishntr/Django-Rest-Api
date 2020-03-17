from rest_framework import generics,viewsets
from rest_framework.response import Response
from .models import Product
from rest_framework.views import APIView
from .serializers import ProductSerializer
# from django.views.decorators.csrf import csrf_exempt
# from rest_framework.parsers import JSONParser
# Create your views here.


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer