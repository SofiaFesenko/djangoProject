from django.contrib.auth.decorators import login_required
from django.contrib.contenttypes.models import ContentType
from django.http import Http404
from django.shortcuts import render, redirect, get_object_or_404
from django.core.paginator import Paginator
from rest_framework.authentication import SessionAuthentication, BasicAuthentication
from rest_framework.permissions import IsAuthenticated
from rest_framework.renderers import TemplateHTMLRenderer
from rest_framework.response import Response
from rest_framework.views import APIView

from services.file_module.models import File
# from services.products_module.filter import CategoryFilter
from services.products_module.forms import UpdateProductForm
from services.products_module.models import Product, Currency, Category

from django.template.defaulttags import register
from django.core.exceptions import BadRequest


@register.filter
def get_range(value):
    return range(1, value + 1)


def index(request):
    products = Product.objects.all()
    categories = Category.objects.all()
    paginator = Paginator(products, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj, 'pages_count': paginator.num_pages, 'page_number': page_number, 'categories': categories}
    return render(request, 'index.html', context)


@login_required
def get_my_products(request):
    pass
    products = Product.objects.filter(owner=request.user)
    paginator = Paginator(products, 4)

    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)
    context = {'products': page_obj, 'pages_count': paginator.num_pages, 'page_number': page_number}

    return render(request, 'my_products.html', context)


def get_product(request, pk):
    product = get_object_or_404(Product, pk=pk)
    return render(request, 'product.html', context={'product': product, 'is_my_product': True})


@login_required
def create_product(request):
    if request.method == "POST":
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            try:
                currency = get_object_or_404(Currency, pk=int(form.data['currency']))
            except ValueError:
                return BadRequest('invalid currency field')

            file = request.FILES['file']

            product = Product.objects.create(title=form.data['title'],
                                             description=form.data['description'],
                                             price=form.data['price'],
                                             in_stock=True if form.data.get('in_stock', False) else False,
                                             owner=request.user,
                                             currency=currency,
                                             category=form.data['category'])

            File.objects.create(file=file,
                                content_type_id=ContentType.objects.get_for_model(Product).id,
                                object_id=product.pk)

            return redirect('product', pk=product.pk)
    else:
        form = UpdateProductForm()
    currency_list = Currency.objects.all()
    return render(request, 'create_update_product.html', context={'form': form, 'currency_list': currency_list})


@login_required
def update_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    if request.method == 'POST':
        form = UpdateProductForm(request.POST)
        if form.is_valid():
            try:
                currency = get_object_or_404(Currency, pk=int(form.data['currency']))
            except ValueError:
                return BadRequest('Invalid currency field')

            product.title = form.data['title']
            product.description = form.data['description']
            try:
                product.price = float(form.data['price'])
            except ValueError:
                return BadRequest('Invalid price field')

            product.in_stock = True if form.data.get('in_stock', False) else False
            product.currency = currency

            product.save()

            if request.FILES.get('file', False):
                file = request.FILES.get('file')

                File.objects.filter(content_type_id=ContentType.objects.get_for_model(Product).id,
                                    object_id=product.pk).delete()

                File.objects.create(file=file,
                                    content_type_id=ContentType.objects.get_for_model(Product).id,
                                    object_id=product.pk)

            return redirect('product', pk=product.pk)

    form = UpdateProductForm(data={'title': product.title,
                                   'description': product.description,
                                   'price': product.price,
                                   'in_stock': product.in_stock,
                                   'currency': product.currency,
                                   'files': product.files,
                                   'category': product.category})

    currency_list = Currency.objects.all()

    return render(request, 'create_update_product.html', context={'form': form,
                                                                  'product': product,
                                                                  'currency_list': currency_list,
                                                                  'is_my_product': True})


@login_required
def delete_product(request, pk):
    product = get_object_or_404(Product, pk=pk)

    File.objects.filter(content_type_id=ContentType.objects.get_for_model(Product).id,
                        object_id=product.pk).delete()
    product.delete()

    return redirect('my_products')


def product_detail(request, id):
    product = Product.objects.get(id=id)
    context = {'product': product}
    return render(request, 'index.html', context)


class CategoryProducts(APIView):
    renderer_classes = [TemplateHTMLRenderer]
    authentication_classes = [SessionAuthentication, BasicAuthentication]
    permission_classes = [IsAuthenticated]

    def get_objects(self, category):
        # try:
        return Product.objects.filter(category=category)
        # except:
        #     raise Http404

    def get(self, request, category, *args, **kwargs):
        self.products = self.get_objects(category)
        print(self.products)
        return Response({'products': self.products}, template_name='categories.html')
