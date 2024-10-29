# ai_accounting/scripts.py

import json
from .models import Transaction

def load_transactions_from_json(file_path):
    with open(file_path, 'r') as f:
        data = json.load(f)
        for item in data:
            transaction = Transaction(
                amount=item['amount'],
                transaction_type=item['transaction_type'],
                description=item['description']
            )
            transaction.save()

# Llama a esta función para cargar datos iniciales (solo una vez)
# load_transactions_from_json('path_to_your_data.json')
