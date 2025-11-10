from django.shortcuts import render
from .models import Contact,GetInTouch,ContactInfo, AboutSection,HeroSlider, Brand
from blog.models import Blog
from django.utils import timezone
from shop.models import Product, Category, DealBanner, Banner


# Create your views here.
def home(request):
    sliders = HeroSlider.objects.all()
    blogs = Blog.objects.all().order_by('-date_posted')[:3]
    products = Product.objects.all()[:4]
    categories = Category.objects.all()[:6]

    banner = DealBanner.objects.filter(active=True).first()
    remaining_seconds = 0
    if banner and banner.end_time:
        remaining_seconds = int((banner.end_time - timezone.now()).total_seconds())
        if remaining_seconds <= 0:
            banner = DealBanner.refresh_daily_deal()
            remaining_seconds = int((banner.end_time - timezone.now()).total_seconds())

    banners = Banner.objects.all()[:2]

    context = {
        "sliders": sliders,
        "blogs": blogs,
        "products": products,
        "categories": categories,
        "banner": banner,
        "remaining_seconds": remaining_seconds,
        "banners": banners,  
    }
    return render(request, "home.html", context)




def about(request):
    about = AboutSection.objects.first()
    brands = Brand.objects.all()

    context = {
        'about': about,
        'brands': brands,
    }
    return render(request, 'about.html', context)


def error(request):
    return render(request, "error.html")

def contact_view(request):
    if request.method == 'POST':
        first_name = request.POST.get('firstname')
        last_name = request.POST.get('lastname')
        phone_number = request.POST.get('number')
        email = request.POST.get('email')
        message = request.POST.get('message')

        Contact.objects.create(
            first_name=first_name,
            last_name=last_name,
            phone_number=phone_number,
            email=email,
            message=message
        )
    contact_info = ContactInfo.objects.first()
    get_in_touch = GetInTouch.objects.first()

      
    return render(request, 'contact.html',{'contact_info': contact_info, 'get_in_touch': get_in_touch})

def faq(request):
    return render(request, "faq.html")

def privacy_policy(request):
    return render(request, "privacy_policy.html")