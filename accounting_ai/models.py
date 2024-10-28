# accounting_ai/models.py

from django.db import models

class Transaction(models.Model):
    amount = models.DecimalField(max_digits=10, decimal_places=2)
    date = models.DateTimeField(auto_now_add=True)
    description = models.CharField(max_length=255)

    def __str__(self):
        return f'Transaction of {self.amount} on {self.date}'

class FraudDetection(models.Model):
    transaction = models.ForeignKey(Transaction, on_delete=models.CASCADE)
    is_fraudulent = models.BooleanField(default=False)
    analyzed_at = models.DateTimeField(auto_now_add=True)

    def __str__(self):
        return f'Fraud Detection for transaction {self.transaction.id}: {self.is_fraudulent}'
