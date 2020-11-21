from django.urls import path

from .views import ListingView, ListingsView, SerchView

urlpatterns = [
  path('', ListingsView.as_view()),
  path('search', SerchView.as_view()),
  path('<slug>', ListingView.as_view()),
]