from django.db import models
from django.db import models
from django.contrib.auth.models import User

class Transfer(models.Model):
    user = models.ForeignKey(User, on_delete=models.CASCADE)
    wallet_address = models.CharField(max_length=255)
    receiver_address = models.CharField(max_length=255)
    amount = models.DecimalField(max_digits=20, decimal_places=8)
    created_at = models.DateTimeField(auto_now_add=True)
    updated_at = models.DateTimeField(auto_now=True)

    def __str__(self):
        return f'Transfer {self.id} - {self.amount} from {self.wallet_address} to {self.receiver_address}'
