from django.contrib import admin
from django.urls import path, include

urlpatterns = [
    path("admin/", admin.site.urls),
    path('api/v1/', include('product_api.urls')),
    path('api/v1/', include('auth_api.urls'))
]
