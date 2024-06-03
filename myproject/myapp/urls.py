from django.urls import path, include
from rest_framework.routers import DefaultRouter
from .views import BarberoViewSet, ClienteViewSet, ReservaViewSet, UserViewSet

router = DefaultRouter()
router.register(r'barberos', BarberoViewSet)
router.register(r'clientes', ClienteViewSet)
router.register(r'reservas', ReservaViewSet)
router.register(r'users', UserViewSet)

urlpatterns =[
    path('', include(router.urls)),
]
