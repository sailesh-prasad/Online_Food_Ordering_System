# restaurant/api/urls.py
from rest_framework.routers import DefaultRouter
from .views import RestaurantViewSet, ProductViewSet, CartViewSet, PaymentViewSet

router = DefaultRouter()
router.register(r'products', ProductViewSet)
router.register(r'carts', CartViewSet)
router.register(r'payments', PaymentViewSet)
router.register(r'restaurants', RestaurantViewSet)

urlpatterns = router.urls
