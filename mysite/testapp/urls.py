from django.urls import path, include
from .views import *

urlpatterns = [
    path('', test, name='test'),
    path('rubric/<int:pk>', get_rubric, name='rubric'),
    path('listdrop/', listdrop, name='listdrop'),
]
