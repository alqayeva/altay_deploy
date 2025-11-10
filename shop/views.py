from django.shortcuts import render, get_object_or_404
from django.core.paginator import Paginator
from .models import Category, Product

def shop(request, category_id=None):
    categories = Category.objects.all()
    products = Product.objects.all()

    # Filter by category
    if category_id:
        selected_category = get_object_or_404(Category, id=category_id)
        products = products.filter(category=selected_category)
    else:
        selected_category = None

    # Filter by price
    min_price = request.GET.get("filter.v.price.gte")
    max_price = request.GET.get("filter.v.price.lte")
    if min_price:
        products = products.filter(current_price__gte=min_price)
    if max_price:
        products = products.filter(current_price__lte=max_price)

    # Filter by search query
    search_query = request.GET.get("q")
    if search_query:
        products = products.filter(name__icontains=search_query)

    # Sort products
    sort_option = request.GET.get("sort", "price")
    if sort_option == "price":
        products = products.order_by("current_price")
    elif sort_option == "alphabet":
        products = products.order_by("name")
    elif sort_option == "latest":
        products = products.order_by("-id")

    # Pagination
    paginator = Paginator(products, 6)
    page_number = request.GET.get('page')
    page_obj = paginator.get_page(page_number)

    context = {
        "categories": categories,
        "products": page_obj,  
        "selected_sort": sort_option,
        "selected_category": selected_category,
        "search_query": search_query,  
    }
    return render(request, "shop.html", context)




def product_details(request, id):
    product = get_object_or_404(Product, id=id)
    related_products = Product.objects.filter(category=product.category).exclude(id=product.id)[:6]
    images = product.images.all()  
    
    return render(request, "product_details.html", {"product": product,"related_products": related_products,"images": images,})


