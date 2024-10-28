from django.urls import path
from .views import transfer_list, home, transfer_assets 
from . import views # Asegúrate de importar todas las vistas necesarias

urlpatterns = [
    path('', home, name='home'),  # Ruta para la vista home
    path('list/', transfer_list, name='transfer_list'),  # Ruta para la lista de transferencias
    path('transfers/', transfer_assets, name='transfers'),  # Ruta para transfer_assets
    path('smartcontracts/', views.smart_contracts, name='smartcontracts'),
    path('accounting-ai/', views.accounting_ai, name='accounting_ai'),
]
