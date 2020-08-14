from django.conf import settings
from django.contrib.auth import authenticate, login, logout
from django.core.mail import send_mail
from django.http import HttpResponse, HttpResponseRedirect, Http404
from django.shortcuts import render, redirect
from django.urls import reverse
from orders.forms import RegistrationForm

from .models import Itemfororder, Extra, Topping, Orderhistory

names = []
prices = []


def index(request):
    if not request.user.is_authenticated:
        form = RegistrationForm()
        return render(request, 'orders/register.html', {'form': form})
    context = {
        "user": request.user
    }
    return render(request, "orders/user.html", context)


def register_view(request):
    if request.method == 'POST':
        form = RegistrationForm(request.POST)
        if form.is_valid():
            form.save()
            return render(request, "orders/login.html", {"message": "Please Login"})
        else:
            return HttpResponse("Invalid Form!!")

    else:
        form = RegistrationForm()
        return render(request, 'orders/register.html', {'form': form})


def login_view(request):
    username = request.POST.get("username")
    password = request.POST.get("password")
    user = authenticate(request, username=username, password=password)
    if user is not None:
        login(request, user)
        itemfororder = Itemfororder.objects.all()
        context = {
            "itemfororder": itemfororder,
        }
        return render(request, "orders/user.html", context)
    else:
        return render(request, "orders/login.html", {"message": "Invalid credentials."})


def orderlist(request):
    itemfororder = Itemfororder.objects.all()
    context = {
        "itemfororder": itemfororder
    }
    return render(request, "orders/user.html", context)


def item(request, item_id):
    try:
        item = Itemfororder.objects.get(pk=item_id)
    except Itemfororder.DoesNotExist:
        raise Http404("Item does not exist")
    context = {
        "item": item,
        "extra": Extra.objects.all(),
        "topping": Topping.objects.all()
    }
    return render(request, "orders/item.html", context)


def addtocart(request, item_id):
    itemname = Itemfororder.objects.get(pk=item_id)
    price = float(itemname.price)
    extra = []
    if (request.POST.get("extracheese", False)):
        price = price + 0.5
        extra.append("extra cheese")
    if (request.POST.get("mushrooms", False)):
        price = price + 0.5
        extra.append("mushrooms")
    if (request.POST.get("greenpepper", False)):
        price = price + 0.5
        extra.append("green pepper")
    if (request.POST.get("onions", False)):
        price = price + 0.5
        extra.append("onions")
    names.append(itemname.name)
    prices.append(price)
    context = {
        "itemnames": names,
        "prices": prices,
        "total": sum(prices)
    }
    return render(request, "orders/cart.html", context)


def cart(request):
    context = {
        "itemnames": names,
        "prices": prices,
        "total": sum(prices)
    }
    return render(request, "orders/cart.html", context)


def confirm(request):
    context = {
        "total": sum(prices)
    }
    return render(request, "orders/checkout.html", context)


def checkout(request):
    username = request.user.username
    email = request.user.email
    for i in range(len(names)):
        osi = Orderhistory(user=username, itemname=names[i], price=prices[i])
        osi.save()
    context = {
        "total": sum(prices),
        "message": "Your order has been placed"
    }
    send_mail('Order placed', 'Your order has been placed.', settings.EMAIL_HOST_USER,
              [email], fail_silently=False)
    names.clear()
    prices.clear()
    return render(request, "orders/checkout.html", context)


def logout_view(request):
    logout(request)
    return render(request, "orders/login.html", {"message": "Logged out."})
