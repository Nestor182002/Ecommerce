from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View

from products.models import Products

# Create your views here.

class ProductsView(View):

    def get(self, request, *args, **kwargs):
        producs_list = Products.objects.all()
        paginator_list = Paginator(producs_list, 10) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        products_page = paginator_list.get_page(page_number)
        return  render(request, 'products/productslist.html', {'products_page':products_page})
