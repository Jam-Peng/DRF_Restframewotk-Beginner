from django.shortcuts import render
from product_api.models import Product
from django.http import Http404
from .serializers import ProductSerializer

from rest_framework.views import APIView
from rest_framework.decorators import api_view
from rest_framework.response import Response
from rest_framework import status


@api_view(['GET'])
def getRoutes(request):
    routes = [
        'GET api/v1/',
        'GET api/v1/products',
        'POST api/v1/create_product',
        'GET PUT DELETE api/v1/products/:id',

        'POST api/v1/signup/',
        'POST api/v1/login/',
        'GET api/v1/test_view/',
        'POST api/v1/logout/',
    ]
    return Response(routes)

# =================  使用類別 APIView 寫法  ================= # 
# 取得所有產品
class ProductList(APIView):
    def get(self, request):
        products = Product.objects.all()
        serializer = ProductSerializer(products, many=True)
        return Response(serializer.data, status=200)

# 建立產品
class ProductCreated(APIView):
    def post(self, request):
        serializer = ProductSerializer(data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_201_CREATED)
        else:
            return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)

# 取得、更新、刪除單一產品
class GetOneProduct(APIView):
    def get_product_by_pk(self, pk):
        try:
            return Product.objects.get(id=pk)
        except Product.DoesNotExist:
            raise Http404

    def get(self, request, pk):
        product = self.get_product_by_pk(pk)
        serializer = ProductSerializer(product)
        return Response(serializer.data, status=status.HTTP_200_OK)

    def put(self, request, pk):
        product = self.get_product_by_pk(pk)
        serializer = ProductSerializer(product, data=request.data)
        if serializer.is_valid():
            serializer.save()
            return Response(serializer.data, status=status.HTTP_200_OK)
        return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
    def delete(self, request, pk):
        product = self.get_product_by_pk(pk)
        product.delete()
        return Response(status=status.HTTP_204_NO_CONTENT)


# =================  使用函式 api_view 寫法  ================= # 
# 取得所有產品
# @api_view(['GET'])
# def getProducts(request):
#     products = Product.objects.all()
#     serializer = ProductSerializer(products, many=True)
#     return Response(serializer.data, status=200)


# 建立產品
# @api_view(['POST'])
# def createProduct(request):
#     serializer = ProductSerializer(data=request.data)
#     if serializer.is_valid():
#         serializer.save()
#         return Response(serializer.data, status=status.HTTP_201_CREATED)
#     else:
#         return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)


# 取得、更新、刪除單一產品
# @api_view(['GET', 'PUT', 'DELETE'])
# def getOneProduct(request, pk):
#     try:
#         product = Product.objects.get(id=pk)
#     except Product.DoesNotExist:
#         raise Http404

#     if request.method == 'GET':
#         serializer = ProductSerializer(product)
#         return Response(serializer.data, status=status.HTTP_200_OK)

#     if request.method == 'PUT':
#       serializer = ProductSerializer(product, data=request.data)
#       if serializer.is_valid():
#           serializer.save()
#           return Response(serializer.data, status=status.HTTP_200_OK)
#       return Response(serializer.errors, status=status.HTTP_400_BAD_REQUEST)
    
#     if request.method == 'DELETE':
#         product.delete()
#         return Response(status=status.HTTP_204_NO_CONTENT)
