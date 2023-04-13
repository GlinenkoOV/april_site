from django.shortcuts import render,redirect
from .models import Product,Popular,Featured,Bloog,Brand,Unlimited,Home
from .forms import CartForm
# Create your views here.
def main_view(request):
    def main_view(request):
        if request.method == 'POST':
            form_reserve = CartForm(request.POST)
            if form_cart.is_valid():
                form_cart.save()
                return redirect('/')

    products = Product.objects.filter(is_visible=True, is_sale=True)
    populars = Popular.objects.filter(is_visible=True,)
    featured = Featured.objects.filter(is_visible=True)
    blogs = Bloog.objects.filter(is_visible=True)
    brands = Brand.objects.all()
    unlimiteds = Unlimited.objects.filter(is_visible=True)
    homes = Home.objects.filter(is_visible=True)
    form_cart = CartForm()
    return render(request, 'main_page.html', context={
        'products': products,
        'populars': populars,
        'featured': featured,
        'blogs': blogs,
        'brands': brands,
        'unlimiteds': unlimiteds,
        'homes': homes,
        'form_cart': form_cart,
    })