from django.shortcuts import render
from rest_framework.views import APIView
from .serializers import *
from rest_framework.response import Response
from rest_framework import status
from .models import *
from rest_framework.decorators import api_view
from rest_framework import generics
from .models import *
from rest_framework import viewsets
from rest_framework_simplejwt.tokens import RefreshToken
from rest_framework_simplejwt.views import TokenObtainPairView
from rest_framework.permissions import IsAdminUser, IsAuthenticated
from django.http import HttpResponse

# Create your views here.

class ProductAPI(APIView):
    permission_classes = [IsAuthenticated]
    def post(self, request):
        try:
            serializer = ProductSerializer(data=request.data)
            if serializer.is_valid():
                serializer.save()
                return Response({"msg":"Success", "data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
            return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    
    def get(self, request, product_id=None):
        try:
            if product_id:
                product = Product.objects.get(id=product_id)
                serializer = ProductSerializer(product)
                return Response({"msg":"Success", "data":serializer.data}, status=status.HTTP_200_OK)
            
            else:
                products = Product.objects.all()
                serializer = ProductSerializer(products, many=True)
                return Response({"msg":"Success", "data":serializer.data}, status=status.HTTP_200_OK)
                
        except Exception as e:
                    return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
            
    def put(self, request, product_id):
            try:
                if product_id:
                    product = Product.objects.get(id=product_id)
                    serializer = ProductSerializer(product, data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg":"Success", "data":serializer.data}, status=status.HTTP_200_OK)
            except Exception as e:
                return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
            
    def delete(self, request, product_id):
                try:
                    if product_id:
                        product = Product.objects.get(id=product_id)
                        product.delete()
                        return Response({"msg":"Success"}, status=status.HTTP_200_OK)
                except Exception as e:
                    return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
                
@api_view(["POST", "GET"])                
def ProductFunAPI(request, product_id = None):
    if request.method == 'POST':
        try:
                    serializer = ProductSerializer(data=request.data)
                    if serializer.is_valid():
                        serializer.save()
                        return Response({"msg":"Success", "data":serializer.data}, status=status.HTTP_200_OK)
        except Exception as e:
                    return Response(str(e),status=status.HTTP_400_BAD_REQUEST)
    
    elif request.method == 'GET':
        try:
                    if product_id:
                        product = Product.objects.get(id=product_id)
                        serializer = ProductSerializer(product)
                        return Response({"msg":"Success", "data":serializer.data}, status=status.HTTP_200_OK)
                    
                    else:
                        products = Product.objects.all()
                        serializer = ProductSerializer(products, many=True)
                        return Response({"msg":"Success", "data":serializer.data}, status=status.HTTP_200_OK)
                        
        except Exception as e:
                            return Response({"error":str(e)},status=status.HTTP_400_BAD_REQUEST)
        
        
class GenAPIOne(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
class GenAPITwo(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class ViewsetAPI(viewsets.ModelViewSet):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer
    
    
class SignupAPI(APIView):
    def post(self, request):
        try:
            serializer = SignupSerializer(data=request.data)
            if serializer.is_valid():
                user = serializer.save()
                refresh = RefreshToken.for_user(user)
                access = refresh.access_token
                return Response({'msg':"Success", "data":serializer.data, 'refresh':str(refresh), 'access':str(access)}, status=status.HTTP_200_OK)
            else:
                return Response({"msg":serializer.errors}, status=status.HTTP_400_BAD_REQUEST)
        except Exception as e:
            return Response({'error':str(e)}, status=status.HTTP_400_BAD_REQUEST)
        
        
class LoginAPI(TokenObtainPairView):
    serializer_class = LoginSerializer
    
    
# import requests

# def get_data_dummy(request):
#     res = requests.get('https://jsonplaceholder.typicode.com/users')
#     result = res.json()
#     print(result)
#     return HttpResponse("Hello")