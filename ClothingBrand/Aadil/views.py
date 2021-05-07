from django.shortcuts import render, get_object_or_404
from .models import  Category,Clothing

# Create your views here.
def list_product(request, Clothing_slug = None):
    Category = None 
    Category = Admin.objects.all() 
    Clothing = Product.objects.filter(available=True) 

    if Clothing_slug: 

        Clothing_filter = get_object_or_404(Clothing, slug=Clothing_slug) 
        Clothing = Clothing.filter(category=Clothing_filter)

    return render(request, 'pasal/product/list_product.html',{'hello':Clothing_filter,
                                                                'categories':Category,
                                                                'clothes':Clothing}

