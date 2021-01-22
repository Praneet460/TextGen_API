from django.urls import path, include
from .views import TextGenView

urlpatterns = [
    path('', TextGenView.as_view(), name="textgen_view")
]