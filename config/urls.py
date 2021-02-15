from django.contrib import admin
from django.urls import path, include
from . import settings
from django.conf.urls.static import static

urlpatterns = [
    path('shop_admin/', include("shop_admin.urls")),
    path('admin/', admin.site.urls),
    path('accounts/', include("accounts.urls")),
    path('shop/', include("shop.urls")),
    path('cart/', include("cart.urls", namespace="cart")),
    path('', include("main.urls")),
    path('mykurly/', include("mykurly.urls")),
]

urlpatterns += static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)

if settings.DEBUG and 'debug_toolbar' in settings.INSTALLED_APPS:
    import debug_toolbar
    urlpatterns += [
        path('__debug__/', include(debug_toolbar.urls)),
    ]