from django.urls import include, path

urlpatterns = [
    path('v1/orders', include('src.presentation.stock.urls')),
    path('v1/stocks', include('src.presentation.order.urls')),
]