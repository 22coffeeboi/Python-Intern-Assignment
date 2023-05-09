from django.urls import path
from .views import CustomerListCreateAPIView, CustomerRetrieveUpdateDestroyAPIView, \
    ProductListCreateAPIView, ProductRetrieveUpdateDestroyAPIView, \
    CustomerProductListCreateAPIView, CustomerProductRetrieveUpdateDestroyAPIView


urlpatterns = [
    path('customers/', CustomerListCreateAPIView.as_view(), name='customer_list_create'),
    path('customers/<int:pk>/', CustomerRetrieveUpdateDestroyAPIView.as_view(), name='customer_retrieve_update')
    ]