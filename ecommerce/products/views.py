from django.core.paginator import Paginator
from django.http import Http404
# views
from django.shortcuts import render
from django.views import View
# dates
import datetime
# models
from products.models import Products,Category,ProductsViewRecentList
# forms


# Create your views here.

class ProductsView(View):
    '''search and pagination'''
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search',None)
        if search != None:
            producs_list = Products.objects.filter(name__contains=search)
        else:
            producs_list = Products.objects.all()

        paginator_list = Paginator(producs_list, 15) # Show 15 products per page.
        page_number = request.GET.get('page')
        products_page = paginator_list.get_page(page_number)
        return  render(request, 'products/productslist.html', {'products_page':products_page})

def DetailProducts(request,pk):
    '''add to models recent products'''
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
        return render(request,'products/recentproducts.html', {'recents': recent})

class ListCategoryProducts(View):
    '''filter of products category'''
    def get(self, request, *args, **kwargs):
        data_cate=request.GET.get('cate',None)
        ordering=request.GET.get('ordering',None)
        #ordering  
        if ordering == 'Asc':
            ordering='id'
        elif ordering == 'Des':
            ordering='-id'
        else:
            ordering='id'

        # obtain day and week
        today = datetime.date.today()
        start_week = today - datetime.timedelta(today.weekday())
        end_week = start_week + datetime.timedelta(7)
        # t=today,s=week,v=more views
        products_filter=Products.objects.all()
        if data_cate != (None or ""):
            if data_cate == 't':
                products_filter=Products.objects.filter(created__day=today.day,created__month=today.month).order_by(ordering)
            elif data_cate == 's':
                products_filter=Products.objects.filter(created__gte=start_week,created__lte=end_week).order_by(ordering)
        else:
            products_filter=Products.objects.all().all().order_by(ordering)

        context={
            'products_list': products_filter,
            'categorys':Category.objects.all()
        }

        return render(request,'category/list_category.html', context)
