
# accounting_ai/admin.py

from django.contrib import admin
from .models import Transaction, FraudDetection

@admin.register(Transaction)
class TransactionAdmin(admin.ModelAdmin):
    list_display = ('amount', 'date', 'description')

@admin.register(FraudDetection)
class FraudDetectionAdmin(admin.ModelAdmin):
    list_display = ('transaction', 'is_fraudulent', 'analyzed_at')
