from django.db import models

class Contact(models.Model):
    first_name = models.CharField(max_length=100)
    last_name = models.CharField(max_length=100)
    phone_number = models.CharField(max_length=20, blank=True, null=True)
    email = models.EmailField()
    message = models.TextField()
    created_at = models.DateTimeField(auto_now_add=True)
    
    
    def __str__(self):
        return f"{self.first_name} - {self.message}"
    
    
class ContactInfo(models.Model):
    phone1 = models.CharField("Primary Phone", max_length=20)
    phone2 = models.CharField("Secondary Phone", max_length=20, blank=True, null=True)
    email1 = models.EmailField("Primary Email")
    email2 = models.EmailField("Secondary Email", blank=True, null=True)
    address = models.TextField("Office Address")

    def __str__(self):
        return f"{self.phone1} | {self.email1}"


class GetInTouch(models.Model):
    heading = models.CharField("Heading", max_length=200, default="Get In Touch")
    description = models.TextField("Description", blank=True)
    map_iframe = models.TextField("Google Map Iframe", help_text="Paste the full iframe code here")

    def __str__(self):
        return self.heading
    
class AboutSection(models.Model):
    title = models.CharField(max_length=200)
    description_1 = models.TextField()
    description_2 = models.TextField(blank=True, null=True)
    image_1 = models.ImageField(upload_to='about')
    image_2 = models.ImageField(upload_to='about')
    video_url = models.URLField(blank=True, null=True)
    author_name = models.CharField(max_length=100)
    author_title = models.CharField(max_length=100)

    def __str__(self):
        return "About Section"  


    
    
class HeroSlider(models.Model):
    subtitle = models.CharField(max_length=255)
    title = models.CharField(max_length=255)
    highlight_text = models.CharField(max_length=100, blank=True, null=True)
    description = models.TextField(blank=True, null=True)
    image = models.ImageField(upload_to='sliders')
    order = models.PositiveIntegerField(default=0)
    class Meta:
        ordering = ['order']

    def __str__(self):
        return self.title
    


class Brand(models.Model):
    name = models.CharField(max_length=100)
    logo = models.ImageField(upload_to='brands/')

    class Meta:
        verbose_name = 'Brand'
        verbose_name_plural = 'Brands'
        ordering = ['id']

    def __str__(self):
        return self.name