from django.urls import path, include
from .views import *
from rest_framework.routers import DefaultRouter

router = DefaultRouter()
router.register('product', ViewsetAPI)


urlpatterns = [
    path('products', ProductAPI.as_view()),
    path('product/<int:pk>', ProductAPI.as_view()),
    # path('', include(router.urls)),
    path('signupp', SignupAPI.as_view()),
    path('user/token/obtain/', LoginAPI.as_view()),
    path('get_dummy', get_data_dummy)
]
