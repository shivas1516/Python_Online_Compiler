from django.urls import path
from .views import index, run_code, code_generation

urlpatterns = [
    path('', index, name='index'),
    path('run_code', run_code, name= 'run_code'),
    path('code_generation', code_generation, name= 'code_generation')
]
