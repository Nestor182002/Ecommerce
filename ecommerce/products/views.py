from django.core.paginator import Paginator
from django.shortcuts import render
from django.views import View
from django.views.generic import DetailView

from products.models import Products

# Create your views here.

class ProductsView(View):

    def get(self, request, *args, **kwargs):
        search = request.GET.get('search',None)
        if search != None:
            producs_list = Products.objects.filter(name__contains=search)
        else:
            producs_list = Products.objects.all()

        paginator_list = Paginator(producs_list, 15) # Show 25 contacts per page.

        page_number = request.GET.get('page')
        products_page = paginator_list.get_page(page_number)
        return  render(request, 'products/productslist.html', {'products_page':products_page})

class DetailProducts(DetailView):
    model=Products
    template_name='products/detailproducts.html'
