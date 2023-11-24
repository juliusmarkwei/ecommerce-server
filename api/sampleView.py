from rest_framework.views import APIView
from rest_framework.response import Response
from django.http import HttpResponse
from .serializers import ProductsSerializer
from .serializers import product_models


class SampleView(APIView):
    def get(self, request):
        products = product_models.Products.objects.all()
        serializer = ProductsSerializer(products, many=True)
        return Response(serializer.data)

    