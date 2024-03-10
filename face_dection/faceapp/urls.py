from django.urls import path
from .views import *

urlpatterns=[
    path('compare/',compare_view),
    path('detection/',face_detection),
    path('home/',index)
]