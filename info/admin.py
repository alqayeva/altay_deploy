from django.contrib import admin
from .models import Contact, ContactInfo, AboutSection,HeroSlider, Brand
from .models import GetInTouch
# Register your models here.


class ContactAdmin(admin.ModelAdmin):
    list_display = ('first_name', 'last_name', 'email', 'phone_number', 'created_at')
    search_fields = ('first_name', 'last_name', 'email')
    
class ContactInfoAdmin(admin.ModelAdmin):
    list_display = ('phone1', 'phone2', 'email1', 'email2', 'address')
    
class GetInTouchAdmin(admin.ModelAdmin):
    list_display = ('heading', 'description')
    
admin.site.register(Contact,ContactAdmin)
admin.site.register(ContactInfo, ContactInfoAdmin)
admin.site.register(GetInTouch, GetInTouchAdmin)


admin.site.register(AboutSection)


@admin.register(HeroSlider)
class HeroSliderAdmin(admin.ModelAdmin):
    list_display = ('title', 'order')
    ordering = ('order',)


@admin.register(Brand)
class Brand(admin.ModelAdmin):
    list_display = ('id', 'name', 'logo')