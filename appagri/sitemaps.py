from django.contrib.sitemaps import Sitemap
import datetime
from .models import Product, SubProduct
from django.urls import reverse
from django.utils.text import slugify

class HomePageSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0

    def items(self):
        return ['home']  

    def location(self, item):
        return '/'
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)
    
class AboutUsPageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0

    def items(self):
        return ['aboutus']

    def location(self, item):
        return '/aboutus/'
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)
    

class ContactUsPageSitemap(Sitemap):
    changefreq = 'monthly'
    priority = 0.7
    

    def items(self):
        return ['contact']

    def location(self, item):
        return '/contact/' 
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)

class BlogsPageSitemap(Sitemap):
    changefreq = 'weekly'
    priority = 1.0
    

    def items(self):
        return ['blogs']

    def location(self, item):
        return '/blogs/' 
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)

class AgritechMartPageSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    

    def items(self):
        return ['ats']

    def location(self, item):
        return '/agritech-mart/' 
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)

class ProductPageSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    

    def items(self):
        return ['product']

    def location(self, item):
        return '/terrace-gardening-products/' 
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)

class ProductDetailsPageSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    

    def items(self):
        return Product.objects.all()

    def location(self, obj):
        return reverse('appagri:product_details', args=[obj.slug]) 
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)

class SubProductDetailsPageSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    
    def items(self):
        return SubProduct.objects.all()

    def location(self, obj):
        return reverse('appagri:sub_product_details', args=[slugify(obj.product),obj.slug]) 
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)

class SubProductDetailsReviewPageSitemap(Sitemap):
    changefreq = 'daily'
    priority = 1.0
    
    def items(self):
        return SubProduct.objects.all()

    def location(self, obj):
        return reverse('appagri:review', args=[slugify(obj.product),obj.slug]) 
    
    def lastmod(self,obj):
        return datetime.datetime(2024, 5, 1)


    