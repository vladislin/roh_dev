from django.urls import path

from .views import (
    HomeView,
    ForDilersView,
    NewsView,
    NewsDetailView,
    PortfolioView,
)

urlpatterns = [
    path('', HomeView.as_view(), name='home'),
    path('dilers/', ForDilersView.as_view(), name='dilers'),
    # path('success/', contact_us, name='success'),
    path('news/', NewsView.as_view(), name='news'),
    path('news/<int:pk>/', NewsDetailView.as_view(), name='news-detail'),
    path('production/', PortfolioView.as_view(), name='portfolio'),
]