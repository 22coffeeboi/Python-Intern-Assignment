# Import necessary Django modules
from django.http import JsonResponse
from django.views.decorators.csrf import csrf_exempt
from datetime import datetime, timedelta
from .models import Customer, Product


# API endpoint for CRUD operations on customer
@csrf_exempt
def customer(request, customer_id=None):
    if request.method == 'GET':
        # Get customer details by ID
        if customer_id:
            try:
                customer = Customer.objects.get(id=customer_id)
                response = {'id': customer.id, 'name': customer.name, 'email': customer.email}
            except Customer.DoesNotExist:
                response = {'error': 'Customer not found'}
        # Get all customers
        else:
            customers = Customer.objects.all()
            response = [{'id': customer.id, 'name': customer.name, 'email': customer.email} for customer in customers]
    elif request.method == 'POST':
        # Create new customer
        data = request.POST
        customer = Customer(name=data['name'], email=data['email'])
        customer.save()
        response = {'id': customer.id, 'name': customer.name, 'email': customer.email}
    elif request.method == 'PUT':
        # Update existing customer
        try:
            customer = Customer.objects.get(id=customer_id)
            data = request.PUT
            customer.name = data['name']
            customer.email = data['email']
            customer.save()
            response = {'id': customer.id, 'name': customer.name, 'email': customer.email}
        except Customer.DoesNotExist:
            response = {'error': 'Customer not found'}
    elif request.method == 'DELETE':
        # Delete customer
        try:
            customer = Customer.objects.get(id=customer_id)
            customer.delete()
            response = {'success': 'Customer deleted successfully'}
        except Customer.DoesNotExist:
            response = {'error': 'Customer not found'}
    else:
        response = {'error': 'Invalid request method'}

    return JsonResponse(response)


# API endpoint for CRUD operations on product
@csrf_exempt
def product(request, product_id=None):
    if request.method == 'GET':
        # Get product details by ID
        if product_id:
            try:
                product = Product.objects.get(id=product_id)
                response = {'id': product.id, 'name': product.name, 'description': product.description, 'active': product.active}
            except Product.DoesNotExist:
                response = {'error': 'Product not found'}
        # Get all products
        else:
            products = Product.objects.all()
            response = [{'id': product.id, 'name': product.name, 'description': product.description, 'active': product.active} for product in products]
    elif request.method == 'POST':
        # Create new product for a customer
        data = request.POST
        try:
            customer = Customer.objects.get(id=data['customer_id'])
            product = Product(name=data['name'], description=data['description'], customer=customer)
            product.save()
            response = {'id': product.id, 'name': product.name, 'description': product.description, 'active': product.active}
        except Customer.DoesNotExist:
            response = {'error': 'Customer not found'}
    elif request.method == 'PUT':
        # Update existing product
        try:
            product = Product.objects.get(id=product_id)
            data = request.PUT
            product.name = data['name']
            product.description = data['description']
            product.active = data['active']
            product.save()
            response = {'id': product.id, 'name': product.name, 'description': product.description, 'active': product.active}
        except Product.DoesNotExist:
            response = {'error': 'Product not found'}
