from django.db import models

class User(models.Model):
    username = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=15)
    avatar = models.ImageField(upload_to='avatars/')
    email = models.EmailField()
    address = models.TextField()
    role = models.CharField(max_length=50)

class Category(models.Model):
    title = models.CharField(max_length=100)

class Brand(models.Model):
    logo = models.ImageField(upload_to='brands/')
    title = models.CharField(max_length=100)
    created_date = models.DateTimeField(auto_now_add=True)

class Product(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    cover = models.ImageField(upload_to='products/')
    title = models.CharField(max_length=200)
    category = models.ForeignKey(Category, on_delete=models.CASCADE)
    description = models.TextField()
    price = models.DecimalField(max_digits=10, decimal_places=2)
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
    created_date = models.DateTimeField(auto_now_add=True)
    is_active = models.BooleanField(default=True)

class ProductBrand(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    brand = models.ForeignKey(Brand, on_delete=models.CASCADE)

class Size(models.Model):
    title = models.CharField(max_length=50)

class ProductSize(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    size = models.ForeignKey(Size, on_delete=models.CASCADE)

class Storage(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    size = models.ForeignKey(Size, on_delete=models.CASCADE)
    status = models.CharField(max_length=100)

class Order(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    storage = models.ForeignKey(Storage, on_delete=models.CASCADE)
    quantity = models.PositiveIntegerField()
    created_date = models.DateTimeField(auto_now_add=True)
    send_date = models.DateTimeField(null=True, blank=True)
    order_status = models.CharField(max_length=100)
    is_pay = models.BooleanField(default=False)
