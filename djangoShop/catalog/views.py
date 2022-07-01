import json
from django.views.generic import ListView
from django.views.generic.detail import DetailView
from catalog.models import Product, Gallery
from card.forms import CartAddProductForm
from django.http import JsonResponse
from django.core import serializers
from django.core.paginator import Paginator
from django.db.models import Q


class ProductView(ListView):
    model = Product
    paginate_by = 1
    template_name = "catalog/product.html"
    context_object_name = 'product_list'
    queryset = Product.objects.all()



    # def sorting_price_text(self, text):
    #     self.queryset = Product.objects.order_by(text)
    #     data = {}
    #     return JsonResponse(data, safe=False)
    #
    # def sorting_price_number(self, number):
    #     self.queryset = Product.objects.filter(price__gt=number-50, price__lte=number)
    #     data = {}
    #     return JsonResponse(data, safe=False)

    # def get_context_data(self, **kwargs):
    #     context = super().get_context_data(**kwargs)
    #     product = Product.objects.get(id=1)
    #     images = product.gallery_set.all()[:1]
    #     context['images'] = images
    #     return context


# def sort(request):
#     print(1)
#     number_sort = request.POST['number']
#     print(number_sort)
#     if number_sort == 1:
#         queryset = Product.objects.order_by('-price')
#         data = serializers.serialize("json", queryset)
#         print(queryset)
#         return JsonResponse(data, safe=False)
#     elif number_sort == -1:
#         queryset = Product.objects.order_by('price')
#         data = serializers.serialize("json", queryset)
#         print(queryset)
#         return JsonResponse(data, safe=False)
#     elif number_sort is None:
#         queryset = Product.objects.all()
#         data = serializers.serialize("json", queryset)
#         return JsonResponse(data, safe=False)
#     else:
#         min = int(number_sort)-50
#         max = int(number_sort)+50
#         queryset = Product.objects.filter(price__gt=min, price__lte=max)
#         data = serializers.serialize("json", queryset)
#         return JsonResponse(data, safe=False)


class ProductDetailView(DetailView):
    model = Product
    pk_url_kwarg = 'product_id'
    template_name = "catalog/product-detail.html"
    context_object_name = 'product_detail'

    def get_context_data(self, **kwargs):
        context = super().get_context_data(**kwargs)
        products = Product.objects.all()[:8]
        context['products'] = products
        context['selector_colors'] = Product.objects.filter(title=self.get_object().title)
        context['cart_product_form'] = CartAddProductForm()
        return context


class FilterProductView(ProductView):

    def get_queryset(self):
        data = self.request.GET
        print(data)
        queryset = Product.objects.all()
        if 'price_text_sort' in data:
            queryset = queryset.order_by(self.request.GET['price_text_sort'])

        if 'price_interval_sort' in data:
            queryset = queryset.filter(price__gt=int(self.request.GET['price_interval_sort'])-50,
                                        price__lte=int(self.request.GET['price_interval_sort']))

        if 'category_sort' in data:
            queryset = queryset.filter(categories__name__in=[self.request.GET['category_sort'], ])

        if 'between_sort_min' in data and 'between_sort_max' in data:
            queryset = queryset.filter(price__gt=int(self.request.GET['between_sort_min']),
                                        price__lte=int(self.request.GET['between_sort_max']))

        if 'title_sort' in data:
            queryset = queryset.filter(title__icontains=self.request.GET['title_sort'])
            print(self.request.GET['title_sort'])
        print(queryset)

        return queryset

    def get(self, request, *args, **kwargs):
        data = self.request.GET
        print(data)
        number_page = self.request.GET["number_page"]
        change_sort = self.request.GET.get("change_sort", False)
        queryset = self.get_queryset()
        p = Paginator(queryset, 1)
        num_pages = p.num_pages
        print(num_pages)
        if bool(change_sort) is True:
            number_page = 1
        page = p.page(number_page)
        page_queryset = page.object_list
        has_previous = page.has_previous()
        has_next = page.has_next()
        if has_next:
            next_page_number = page.next_page_number()
            previous_page_number = -1
        elif has_previous:
            next_page_number = -1
            previous_page_number = page.previous_page_number()
        elif has_next and has_previous:
            next_page_number = page.next_page_number()
            previous_page_number = page.previous_page_number()
        else:
            previous_page_number = -1
            next_page_number = -1
        json1 = serializers.serialize("json", page_queryset)
        data = json.loads(json1)
        if len(queryset) > 0:
            k = 0
        else:
            k = 1

        for product in page_queryset:
            img = product.gallery.all()[:1]
            data[k]['fields']['img'] = str(img[0].image)
            data[k]['get_absolute_url'] = str(product.get_absolute_url())
            k += 1
            try:
                data[k-1]['num_pages'] = str(num_pages)
                data[k-1]['next_page_number'] = str(next_page_number)
                data[k-1]['previous_page_number'] = str(previous_page_number)
                data[k-1]['number_page'] = str(number_page)
            except:
                data={}
        return JsonResponse(data, safe=False)
