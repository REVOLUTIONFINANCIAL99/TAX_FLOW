from django.test import TestCase
# accounting_ai/tests.py

from django.test import TestCase
from .models import Transaction

class TransactionModelTest(TestCase):
    def setUp(self):
        Transaction.objects.create(amount=100.00, description='Test Transaction')

    def test_transaction_str(self):
        transaction = Transaction.objects.get(id=1)
        self.assertEqual(str(transaction), 'Transaction of 100.00 on <date>')
