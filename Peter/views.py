from django.shortcuts import render, get_object_or_404, redirect
from .models import Product
from django.contrib.auth import login
from django.contrib.auth.decorators import login_required
from django.contrib import messages
from django.contrib.auth import authenticate,login
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth import login, authenticate
from django.contrib.auth.forms import UserCreationForm, AuthenticationForm
from django.contrib import messages


def productlist(request):
    clothes = Product.objects.filter(category__name="clothes")
    watches = Product.objects.filter(category__name="watches")

    return render(request, 'index.html', {
        "clothes": clothes,
        "watches": watches
    })

def add_to_cart(request, product_id):
    product = get_object_or_404(Product, pk=product_id)
    cart = request.session.get('cart', {})
    key = str(product_id)

    if key in cart:
        cart[key]['quantity'] += 1
    else:
        cart[key] = {
            'name': product.name,
            'image': product.image.url,
            'price': float(product.price),
            'quantity': 1,
        }

    request.session['cart'] = cart
    return redirect('productlist')

def cart_view(request):
    cart = request.session.get('cart', {})
    total=sum(item['price']* item['quantity'] for item in cart.values())
    return render(request, 'items.html', { 
            "cart":cart, "total":total})
    
def product_details(request, product_id):
        product = get_object_or_404(Product, pk=product_id)
        return render( request, 'prodetails.html',{
                "product":product  })
@login_required
def profile(request):
    return render(request, "profile_list.html", {"user": request.user})

def signup_view(request):
    if request.method == 'POST':
        form = UserCreationForm(request.POST)
        if form.is_valid():
            user = form.save()
            login(request, user)
            messages.success(request, "Account created successfully!")
            return redirect("productlist")  # Replace with your homepage
        else:
            messages.error(request,"Enter  valid username")
    else:
        form = UserCreationForm()
    return render(request, 'sign-up.html', {'form': form})

def signin_view(request):
    if request.method == 'POST':
        username = request.POST.get("username")
        password = request.POST.get("password")
        user = authenticate(request, username=username, password=password)
        if user is not None:
            login(request, user)
            return redirect("productlist")
        else:
            messages.error(request, "invalid username or password")
            return render(request,"sign.html")
    return render(request,"sign.html")

def get_cart_total(request):
    cart = request.session.get('cart', {})
    total = sum(item['price'] * item['quantity'] for item in cart.values())
    return total

def remove_from_cart(request, pk):
    cart = request.session.get('cart', {})
    pk = str(pk)  # convert to string since session keys are strings

    if pk in cart:
        if cart[pk]['quantity'] > 1:
            cart[pk]['quantity'] -= 1
        else:
            del cart[pk]

    request.session['cart'] = cart
    return redirect('cart_view')
