from django.urls import path
from . import views

urlpatterns = [
    path('textUtils/', views.textUtils, name='textUtils'),
    path('', views.index, name='index'),
    path('home', views.home, name='home'),
    path('about', views.about, name='about'),
    path('wishlist', views.wishlist, name='wishlist'),
    path('addtocart', views.addtocart, name='addtocart'),
    path('buynow', views.buynow, name='buynow'),

    # path('', views.index, name='index'),
    # path('analyze', views.analyze, name='analyze')
]
