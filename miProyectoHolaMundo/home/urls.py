from django.urls import path
from .views import home

# Se utilizara para que las urls de home se guarden aqui
# y despues esto se manda a url de admin (el proyecto)
# para mejores practicas.
app_name = 'home'

urlpatterns = [
    path('', home, name='home'),
]
