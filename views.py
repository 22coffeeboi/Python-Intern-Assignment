from rest_framework import generics, status
from rest_framework.response import Response
from django.utils import timezone
from datetime import timedelta
from .models import Customer, Product, CustomerProduct
from .serializers import CustomerSerializer, ProductSerializer, CustomerProductSerializer


class CustomerListCreateAPIView(generics.ListCreateAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class CustomerRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Customer.objects.all()
    serializer_class = CustomerSerializer


class ProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class ProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = Product.objects.all()
    serializer_class = ProductSerializer


class CustomerProductListCreateAPIView(generics.ListCreateAPIView):
    queryset = CustomerProduct.objects.all()
    serializer_class = CustomerProductSerializer


class CustomerProductRetrieveUpdateDestroyAPIView(generics.RetrieveUpdateDestroyAPIView):
    queryset = CustomerProduct.objects.all()
    serializer_class = CustomerProductSerializer

    def put(self, request, *args, **kwargs):
        instance = self.get_object()
        if instance.created_at < timezone.now() - timedelta(days=60):
            instance.product.is_active = False
            instance.product.save()
        serializer = self.get_serializer(instance, data=request.data, partial=True)
        serializer.is_valid(raise_exception=True)
        self.perform_update(serializer)
        return Response(serializer.data)

