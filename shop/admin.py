from django.contrib import admin
from .models import Category, Product, PriceFilter, ProductImage, DealBanner, Banner

@admin.register(Category)
class CategoryAdmin(admin.ModelAdmin):
    list_display = ("name", "image")
    search_fields = ("name",)


class ProductImageInline(admin.TabularInline):
    model = ProductImage
    extra = 1


@admin.register(Product)
class ProductAdmin(admin.ModelAdmin):
    inlines = [ProductImageInline]
    list_display = ("name", "category", "current_price", "old_price", "discount_percent")
    list_filter = ("category",)
    search_fields = ("name",)
    ordering = ("name",)


@admin.register(PriceFilter)
class PriceFilterAdmin(admin.ModelAdmin):
    list_display = ("min_price", "max_price")



@admin.register(DealBanner)
class DealBannerAdmin(admin.ModelAdmin):
    list_display = ("title", "product", "start_time", "end_time", "active")
    actions = ["refresh_daily_deal_action"]

    def refresh_daily_deal_action(self, request, queryset):
        deal = DealBanner.refresh_daily_deal()
        if deal:
            self.message_user(request, f"✅ Deal refreshed with {deal.product.name}")
        else:
            self.message_user(request, "⚠️ No products available or no active banner.")
    refresh_daily_deal_action.short_description = "🎲 Refresh daily deal product"


@admin.register(Banner)
class BannerAdmin(admin.ModelAdmin):
    list_display = ('title', 'badge', 'subtitle', 'current_price', 'old_price', 'order')
    list_editable = ('order',)