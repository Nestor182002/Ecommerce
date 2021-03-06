from django.core.paginator import Paginator
from django.http import Http404
# views
from django.shortcuts import redirect, render
from django.urls import reverse
from django.views import View
# dates
import datetime
# models
from products.models import Products,Category,ProductsViewRecentList,ProductsFavorite
# forms


# Create your views here.

class ProductsView(View):
    '''search and pagination'''
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search',None)
        if search != None:
            producs_list = Products.objects.filter(name__contains=search)
        else:
            producs_list = Products.objects.all().order_by('-id')

        paginator_list = Paginator(producs_list, 5) # Show 15 products per page.
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
        if request.user.is_authenticated:
            product_favorite=ProductsFavorite.objects.filter(favorite_user=request.user,favorite_product=Product_Detail)
        else:
            product_favorite=[]
        context={
            'favorites':product_favorite,
            'object': Product_Detail,
        }
    except Products.DoesNotExist:
        raise Http404("Products does not exist")
    return render(request, 'products/detailproducts.html',context)


class RecentViewProduct(View):
    def get(self, request, *args, **kwargs):
        request.session["fav_color"] = "blue"
        user=request.user
        recent=ProductsViewRecentList.objects.filter(recent_user=user,active=True)
        return render(request,'products/recentproducts.html', {'recents': recent})

class ListCategoryProducts(View):
    '''filter of products category'''
    def get(self, request, *args, **kwargs):
        search = request.GET.get('search',None)
        print(search)
        if search == None:
            data_cate=request.GET.get('cate',None)
            ordering=request.GET.get('ordering',None)
            category= request.GET.get('c',None)
            #ordering  
            if ordering == 'Asc':
                ordering='id'
            elif ordering == 'Des':
                ordering='-id'
            else:
                ordering='id'
            # category
            if category != "":
                if Category.objects.filter(id=category).exists() != True:
                    category=Category.objects.all()
            else:
                category=Category.objects.all()

            # obtain day and week
            today = datetime.date.today()
            start_week = today - datetime.timedelta(today.weekday())
            end_week = start_week + datetime.timedelta(7)
            # t=today,s=week,v=more views
            products_filter=Products.objects.all()
            if data_cate != (None or ""):
                if data_cate == 't':
                    products_filter=Products.objects.filter(created__day=today.day,created__month=today.month,categorys__in=category).order_by(ordering)
                elif data_cate == 's':
                    products_filter=Products.objects.filter(created__gte=start_week,created__lte=end_week,categorys__in=category).order_by(ordering)
            else:
                products_filter=Products.objects.filter(categorys__in=category).order_by(ordering)

            context={
                'products_list': products_filter,
                'categorys':Category.objects.all(),
            }

            return render(request,'category/list_category.html', context)
        else:
            producs_list = Products.objects.filter(name__contains=search).order_by('-id')

            context={
                'products_list': producs_list,
                'categorys':Category.objects.all()
            }
            return  render(request,'category/list_category.html',context)

def FavoriteProductPost(request,pk):
    ProductsF=Products.objects.get(pk=pk)
    BoolFav=False
    FavExist=ProductsFavorite.objects.filter(favorite_product=ProductsF,favorite_user=request.user)
    if request.user.is_authenticated:
        if FavExist.exists():
            BoolFav=True
        if BoolFav == False:
            ProductsFavorite.objects.create(favorite_user=request.user,favorite_product=ProductsF)
            return redirect(reverse('detail_products',args=[ProductsF.pk]))
        else:
            FavExist.delete()
            return redirect(reverse('detail_products',args=[ProductsF.pk]))
    else:
        return redirect('/')
    
class FavoriteProductPage(View):

    def get(self, request, *args, **kwargs):
        product_favorite=ProductsFavorite.objects.filter(favorite_user=request.user)
        context={
            'list_favorite':product_favorite,
        }
        return  render(request,'products/FavoriteProducts.html',context)
    def delete(self, request, *args, **kwargs):
        pass