from django.shortcuts import render
# accounting_ai/views.py

from django.shortcuts import render
from .models import Transaction, FraudDetection

def transaction_list(request):
    transactions = Transaction.objects.all()
    return render(request, 'accounting_ai/transaction_list.html', {'transactions': transactions})

def fraud_detection(request):
    frauds = FraudDetection.objects.all()
    return render(request, 'accounting_ai/fraud_detection_list.html', {'frauds': frauds})
