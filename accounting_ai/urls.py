# accounting_ai/urls.py

from django.urls import path
from .views import transaction_list, fraud_detection

urlpatterns = [
    path('transactions/', transaction_list, name='transaction_list'),
    path('fraud-detection/', fraud_detection, name='fraud_detection'),
]
