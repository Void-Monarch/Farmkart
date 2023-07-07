from django.db import models
from accounts.models import Account
from store.models import Product

# Create your models here.
class Payment(models.Model):
    user = models.ForeignKey(Account, on_delete=models.CASCADE )
    payment_id = models.CharField(max_length=255)
    Payment_method = models.CharField(max_length=200)
    amount_paid = models.IntegerField()
    status = models.CharField(max_length=200)
    created_on = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.payment_id

class order(models.Model):
    STATUS = ( 
        ("New", "New"),
        ("Accepted", "Accepted"),
        ("Completed"), 'Compleated',
        ("Cancelled", "Cancelled"),
    )

    user = models.ForeignKey(Account, null=True, on_delete=models.CASCADE)
    order_number = models.CharField(max_length=255)
    order_total = models.IntegerField()
    status = models.CharField(max_length=20)
    ip = models.CharField(max_length=100, blank=True)
    created_at = models.DateTimeField(auto_now_add=True, null=True)

    def __str__(self) -> str:
        return self.user.username

class OrderProduct(models.Model):
    order = models.ForeignKey(order, on_delete=models.CASCADE)
    payment = models.ForeignKey(Payment, on_delete=models.SET_NULL, null=True, blank=True)
    user = models.ForeignKey(Account, on_delete=models.CASCADE)
    product = models.ForeignKey(Product, on_delete=models.CASCADE)
    quattity = models.IntegerField()
    product_price = models.IntegerField()
    ordered = models.BooleanField(default=False)
    created_At = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return self.product.product_name

