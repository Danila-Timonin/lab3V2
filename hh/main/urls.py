from django.urls import path
from . import views

urlpatterns = [
    # path('accounts/login/', views.product, name='login'),
    path('profile/', views.profile, name='profile'),
    path('logout/', views.logout_view, name='logout'),
    path('exp', views.exp, name='exp'),
    path('register', views.register, name='register'),
    path('', views.login, name='login'),
    path('visitor', views.index, name='home'),
    path('visitor/create', views.visitor_create, name='visitor_create'),
    path('visitor/<int:pk>/update', views.visitor_update, name='visitor_update'),
    path('visitor/<int:pk>/delete', views.visitor_delete, name='visitor_delete'),
    path('store', views.store, name='store'),
    path('store/create', views.store_create, name='store_create'),
    path('store/<int:pk>/update', views.store_update, name='store_update'),
    path('store/<int:pk>/delete', views.store_delete, name='store_delete'),
    path('product', views.product, name='product'),
    path('product/create', views.product_create, name='product_create'),
    path('product/<int:pk>/update', views.product_update, name='product_update'),
    path('product/<int:pk>/delete', views.product_delete, name='product_delete'),
    path('purchase', views.purchase, name='purchase'),
    path('purchase/create', views.purchase_create, name='purchase_create'),
    path('purchase/<int:pk>/update', views.purchase_update, name='purchase_update'),
    path('purchase/<int:pk>/delete', views.purchase_delete, name='purchase_delete'),
    path('review', views.review, name='review'),
    path('review/create', views.review_create, name='review_create'),
    path('review/<int:pk>/update', views.review_update, name='review_update'),
    path('review/<int:pk>/delete', views.review_delete, name='review_delete'),

]
