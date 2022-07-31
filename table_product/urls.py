from django.urls import path
from . import views
from .views import GetAllData

app_name = "table_product"
urlpatterns = [
    path('', views.products, name="products"),
    path('get-all-data/', GetAllData.as_view()),
]