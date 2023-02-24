# pages/urls.py
from django.urls import path
from .views import homePageView, aboutPageView, results, homePost, sarahPageView

urlpatterns = [
    path('', homePageView, name='home'),
    path('about/', aboutPageView, name='about'),
    path('homePost/', homePost, name='homePost'),
    path('sarah/', sarahPageView, name='sarah'),
    path('results/<int:choice>/<str:gmat>/', results, name='results'),
]
