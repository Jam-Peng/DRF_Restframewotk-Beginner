from django.urls import path
from . import views

urlpatterns = [
    path('', views.getRoutes),

    # =================  使用函式 api_view 寫法  ================= # 
    # path('products/', views.getProducts),
    # path('create_product/', views.createProduct),
    # path('products/<str:pk>', views.getOneProduct),

    # =================  使用類別 APIView 寫法  ================= # 
    path('products/', views.ProductList.as_view()),
    path('create_product/', views.ProductCreated.as_view()),
    path('products/<str:pk>', views.GetOneProduct.as_view()),
]
