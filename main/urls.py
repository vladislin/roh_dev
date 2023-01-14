from django.urls import path

from .views import (
    HomeView,
    ForDilersView,
    NewsView,
    NewsDetailView,
    ProductionView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dilers/', ForDilersView.as_view(), name='dilers'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('production/', ProductionView.as_view(), name='portfolio'),
]