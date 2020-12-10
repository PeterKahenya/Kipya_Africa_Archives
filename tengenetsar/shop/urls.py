from .views import *
from django.urls import path


urlpatterns = [
	path('',ProductsListView.as_view()),
	path('products/<uuid:pk>/',ProductDetailView.as_view()),
	path('products/<uuid:pk>/add_to_cart',AddToCartView.as_view()),
	path('products/categories/<uuid:pk>/',CategoryView.as_view()),
	path('orders',OrderListView.as_view()),
	path('orders/<uuid:order_id>/checkout',CheckOutView.as_view()),
	path('orders/<uuid:order_id>/track',TrackShipment.as_view()),
	path('orders/<uuid:order_id>/<uuid:product_id>/remove',RemoveProduct.as_view())
]