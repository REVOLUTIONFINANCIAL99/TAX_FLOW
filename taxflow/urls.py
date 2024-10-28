from django.contrib import admin
from django.urls import path, include
from transfers.views import home

urlpatterns = [
    path('admin/', admin.site.urls),
    path('accounting_ai/', include('accounting_ai.urls')),
    path('smartcontracts/', include('smartcontracts.urls')),
    path('transfers/', include('transfers.urls')),
    path('', home, name='home'),  # Ruta para la página principal
    # ... otras rutas ...
]
