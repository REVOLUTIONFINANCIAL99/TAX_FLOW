from django.shortcuts import render
from .models import Transfer

def transfer_list(request):
    transfers = Transfer.objects.all()
    return render(request, 'transfers/transfer_list.html', {'transfers': transfers})

def home(request):
    return render(request, 'home.html') # Asegúrate de que la ruta a la plantilla sea correcta

def transfer_assets(request):
    # Lógica para la vista de transferencias de activos
    return render(request, 'transfers/transfer_assets.html')

def smart_contracts(request):
    return render(request, 'transfers/smart_contracts.html')

def accounting_ai(request):
    return render(request, 'your_app/accounting_ai.html')
