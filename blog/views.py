from django.shortcuts import render, get_object_or_404
from .models import Blog
from shop.models import Category, Product 

def blog(request):
    blogs = Blog.objects.all()
    return render(request, 'blog.html', {'blogs': blogs})



def blog_detail(request, id):
    blog = get_object_or_404(Blog, id=id)
    categories = Category.objects.all()
    blogs = Blog.objects.all()
    category_id = request.GET.get('category_id')  
    products = Product.objects.all()
    
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=selected_category)
    else:
        selected_category = None

    return render(request, 'blog-detail.html', {
        'blog': blog,
        'categories': categories,
        'selected_category': selected_category,
        'products': products, 
        'blogs': blogs
    })