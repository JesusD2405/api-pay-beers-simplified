from django.urls import path
from ..base.ViewWrapper import ViewWrapper
from .views import OrderView

# The API URLs are now determined automatically by the router.
# Additionally, we include the login URLs for the browsable API.
urlpatterns = [
	path('', ViewWrapper.as_view(view_factory=OrderView), name='order-list'),
]