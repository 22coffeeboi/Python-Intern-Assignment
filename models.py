from django.db import models


class Customer(models.Model):
    name = models.CharField(max_length=100)
    email = models.EmailField()
    phone = models.CharField(max_length=20)
    address = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    name = models.CharField(max_length=100)
    price = models.DecimalField(max_digits=8, decimal_places=2)
    description = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

    def __str__(self):
        return self.name


class CustomerProduct(models.Model):
    customer = models.ForeignKey(Customer, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    created_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f"{self.customer.name} - {self.product.name}"


//A tool like Postman can be used to send requests to the endpoints defined in the urls.py file and see the responses.
//Creates a new customer by sending a POST request to http://127.0.0.1:8000/customers/ with the following JSON data in the request body:
//{
    "name": "Aab El Roi",
    "email": "aabelroisimon@gmail.com",
    "phone": "9074721757",
    "address": "Kochi"
}
//In return receives a response with a JSON object containing the customer details, including the id field:
//{
    "id": 1,
    "name": "Aab El Roi",
    "email": "aabelroisimon@gmail.com",
    "phone": "9074721757",
    "address": "Kochi"
}

//This is how each time the database value gets incremented on the count of 1 that is the return id.
//Can then use the customer ID to add products to the customer or update the customer details.

