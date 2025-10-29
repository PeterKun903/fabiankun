from django.contrib import admin
from django.urls import path
from Peter import views
from django.conf import settings
from django.contrib.auth import views as auth_views
from django.conf.urls.static import static  # ✅ This import is missing
from Peter import mpesa
urlpatterns = [
    path('admin/', admin.site.urls),
    path('', views.productlist, name='productlist'),
    path('add-to-cart/<int:product_id>/', views.add_to_cart, name='add_to_cart'),
    path('product/<int:product_id>/', views.product_details, name='product'),
    path('cart/', views.cart_view, name='cart'),
    path('logout/',auth_views.LogoutView.as_view(next_page='login'),name='logout'),
    path( 'login/', views.signin_view, name='login'),
    path( 'signup/', views.signup_view, name='signup'),
    path('stkpush/', mpesa.lipa_na_mpesa_online,name='stkpush'),
    path('callback', mpesa.stk_callback, name="stk_callback"),
    path('remove_from_cart/<int:pk>/',views.remove_from_cart, name='remove_from_cart'),
]

if settings.DEBUG:
    urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

# ✅ Serve media files during development