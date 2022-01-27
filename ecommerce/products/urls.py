from django.urls import path
from django.views.generic import TemplateView

urlpatterns = [
    path('inicio/', TemplateView.as_view(template_name="base/base.html")),
    path('inicio2/', TemplateView.as_view(template_name="products/products.html")),
]