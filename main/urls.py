from django.urls import path
from . import views

urlpatterns = [
    path('/', views.home, name='home'),
    path('dilers/', views.dilers, name='dilers'),
    path('success/', views.contact_us, name='success'),
    path('all_news/', views.ShowNewsView.as_view(), name='news'),
    path('news/<int:pk>/', views.NewsDetailView.as_view(), name='news-detail'),
    path('production/', views.portfolio_view, name='portfolio'),
]