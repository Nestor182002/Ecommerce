from django.core.paginator import Paginator
from django.http import Http404
from django.shortcuts import render
from django.views import View
from products.models import ProductsViewRecentList

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

def DetailProducts(request,pk):
    try:
        Product_Detail = Products.objects.get(id=pk)

        if request.user.is_authenticated:
            users=request.user
            if ProductsViewRecentList.objects.filter(recent_user=users,recent_product=Product_Detail,active=True).exists():
                products=ProductsViewRecentList.objects.get(recent_user=users,recent_product=Product_Detail,active=True)
                products.delete()
                ProductsViewRecentList.objects.create(
                recent_user=users,
                recent_product=Product_Detail,
                )
            else:
                ProductsViewRecentList.objects.create(
                recent_user=users,
                recent_product=Product_Detail,
                )

    except Products.DoesNotExist:
        raise Http404("Products does not exist")
    return render(request, 'products/detailproducts.html', {'object': Product_Detail})

class RecentViewProduct(View):

    def get(self, request, *args, **kwargs):
        user=request.user
        recent=ProductsViewRecentList.objects.filter(recent_user=user,active=True)
        return render(request, 'products/recentproducts.html', {'recents': recent})