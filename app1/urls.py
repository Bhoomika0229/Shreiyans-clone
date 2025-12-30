from django.urls import path
from . import views

urlpatterns = [

    # ---------- HOME ----------
    path('', views.home, name='home'),

    # ---------- AUTH ----------
    path('signin/', views.signin, name='signin'),
    path('signup/', views.signup, name='signup'),

    # ---------- COURSE ----------
    path('course/<int:course_id>/', views.course_detail, name='course_detail'),
   
    # ---------- CART (CRUD) ----------
    path('cart/', views.cart_view, name='cart'),
    path('cart/add/<int:course_id>/', views.add_to_cart, name='add_to_cart'),
    path('cart/remove/<int:course_id>/', views.remove_from_cart, name='remove_from_cart'),

    # ---------- GOOGLE LOGIN (dummy) ----------
    path('google/', views.google_login, name='google'),
]
