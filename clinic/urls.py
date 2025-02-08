from django.contrib import admin
from django.urls import path
from django.urls import path, include, re_path
from appagri import urls as appagri_urls
from django.conf.urls.static import static
from django.conf import settings
from django.contrib.sitemaps import views 
from appagri.sitemaps import HomePageSitemap, AboutUsPageSitemap, ContactUsPageSitemap, BlogsPageSitemap, ProductPageSitemap, ProductDetailsPageSitemap, SubProductDetailsPageSitemap, SubProductDetailsReviewPageSitemap, AgritechMartPageSitemap
import os
from django.http import HttpResponse
from django.views import View


sitemaps = {
    'home': HomePageSitemap,
    'aboutus': AboutUsPageSitemap,
    'contact': ContactUsPageSitemap,
	'blogs': BlogsPageSitemap,
	'atm':AgritechMartPageSitemap,
	'products': ProductPageSitemap,
	'productdetails': ProductDetailsPageSitemap,
    'subproductdetails': SubProductDetailsPageSitemap,
	'subproduct-review':SubProductDetailsReviewPageSitemap,
}
class RobotsTxtView(View):
    def get(self, request):
        file_path = os.path.join(settings.BASE_DIR, 'robots.txt')

        try:
            with open(file_path, 'r') as file:
                content = file.read()
        except FileNotFoundError:
            content = ""

        return HttpResponse(content, content_type='text/plain')
urlpatterns = [
    path('admin/', admin.site.urls), 
    path('', include('appagri.urls')),
    path('', include(appagri_urls, namespace="projagri")),
    re_path("", include("allauth.urls")),
	path('sitemap.xml', views.sitemap, {'sitemaps': sitemaps}, name='django.contrib.sitemaps.views.sitemap'),
	path('robots.txt', RobotsTxtView.as_view(), name='robots.txt'),
] + static(settings.MEDIA_URL, document_root=settings.MEDIA_ROOT)
