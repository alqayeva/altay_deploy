from django.db import models
from django.utils import timezone
from datetime import timedelta
import random


class Category(models.Model):
    name = models.CharField(max_length=100)
    image = models.ImageField(upload_to="categories/", blank=True, null=True)

    def __str__(self):
        return self.name


class Product(models.Model):
    category = models.ForeignKey(Category, on_delete=models.CASCADE, related_name="products")
    name = models.CharField(max_length=255)
    primary_image = models.ImageField(upload_to="products/")
    secondary_image = models.ImageField(upload_to="products/", blank=True, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    discount_percent = models.IntegerField(blank=True, null=True)  # e.g., -14%
    description = models.TextField(blank=True, null=True)

    def __str__(self):
        return self.name
    

class DealBanner(models.Model):
    title = models.CharField(max_length=100)
    subtitle = models.CharField(max_length=150, blank=True, null=True)
    button_text = models.CharField(max_length=50, default="Shop now")
    image = models.ImageField(upload_to="deal_banners/")
    start_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    active = models.BooleanField(default=True)

    # Automatically assign a random product for "deal of the day"
    product = models.ForeignKey('Product', on_delete=models.CASCADE, null=True, blank=True)
    start_time = models.DateTimeField(default=timezone.now)
    end_time = models.DateTimeField(blank=True, null=True)

    def __str__(self):
        return f"Deal Banner: {self.title}"

    @staticmethod
    def refresh_daily_deal():
        """Rotates the banner's product once per day automatically."""
        banner = DealBanner.objects.filter(active=True).first()
        if not banner:
            return None

        products = list(Product.objects.all())
        if not products:
            return None

        now = timezone.now()
        product = random.choice(products)
        banner.product = product
        banner.start_time = now
        banner.end_time = now + timedelta(hours=24)
        banner.save()
        return banner


class PriceFilter(models.Model):
    min_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    max_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)

    def __str__(self):
        return f"${self.min_price} - ${self.max_price}"



class ProductImage(models.Model):
    product = models.ForeignKey(Product, on_delete=models.CASCADE, related_name='images')
    image = models.ImageField(upload_to="products/")
    
    def __str__(self):
        return f"Image for {self.product.name}"


class Banner(models.Model):
    BANNER_TYPE_CHOICES = [
        ('badge', 'Badge'),
        ('subtitle', 'Subtitle'),
    ]

    title = models.CharField(max_length=200)
    subtitle = models.CharField(max_length=200, blank=True, null=True)
    badge = models.CharField(max_length=100, blank=True, null=True)
    current_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    old_price = models.DecimalField(max_digits=10, decimal_places=2, blank=True, null=True)
    image = models.ImageField(upload_to='banners/')
    button_text = models.CharField(max_length=50, default='Shop now')
    link = models.URLField(blank=True, null=True)
    order = models.PositiveIntegerField(default=0)

    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
