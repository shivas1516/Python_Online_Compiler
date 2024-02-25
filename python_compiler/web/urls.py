from django.urls import path
from .views import index, run_code

urlpatterns = [
    path('', index, name='index'),
    path('run_code', run_code, name= 'run_code')
]
