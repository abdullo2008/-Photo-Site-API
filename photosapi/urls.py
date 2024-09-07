from django.urls import path
from .views import *


urlpatterns = [
    # API
    # path('api/v1/', CreateAPIPhoto.as_view()),
    # path('api/v1/<int:pk>/', UpdateDeletePhotoAPIView.as_view()),


    # Site
    path('', ListPhoto, name='index'),
    path('about', about, name='about'),
    path('add/', CreatePhoto.as_view(), name='addphoto'),
    path('update/<int:pk>/', UpdatePhoto.as_view(), name='update'),
    path('delete/<int:pk>/', DeletePhoto.as_view(), name='delete'),
]
