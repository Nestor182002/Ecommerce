from django.http import response
from django.shortcuts import render
from django.views import View

# Create your views here.

class ProductsView(View):

    def get(self, request, *args, **kwargs):
        return  render(request, 'products/productslist.html', {})
