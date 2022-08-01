from django.shortcuts import render

from rest_framework.views import APIView
from rest_framework import status
from rest_framework.response import Response
from .models import TableProduct
from .serializers import PruductModelSerializer
# Create your views here.

def products(request):
    products = TableProduct.objects.all()
    return render(request, 'table_product/table_product.html', {
        'products': products
    })

class GetAllData(APIView):
    def get(self, request):
        query = TableProduct.objects.all().order_by('-date')
        serializers = PruductModelSerializer(query, many=True, context={'request': request})
        return Response(serializers.data, status=status.HTTP_200_OK)
