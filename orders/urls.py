from django.urls import path

from . import views

urlpatterns = [
    path("", views.index, name="index"),
    path("register", views.register_view, name="register"),
    path("<int:item_id>", views.item, name="item"),
    path("<int:item_id>/addtocart", views.addtocart, name="addtocart"),
    path("login", views.login_view, name="login"),
    path("orderlist", views.orderlist, name="orderlist"),
    path("logout", views.logout_view, name="logout"),
    path("cart", views.cart, name="cart"),
    path("confirm", views.confirm, name="confirm"),
    path("checkout", views.checkout, name="checkout")
]
