
from django.urls import path, include
from .views import product_details,ProductDetailView
from . import views
from rest_framework.routers import DefaultRouter

app_name = 'appagri'

router = DefaultRouter()
router.register(r'ats-intro', views.ATSIntroViewSet, basename='atsintro')
router.register(r'ats-info',views.ATSInfoViewSet, basename="atsinfo")
router.register(r'ats-contact-info',views.ATSContactInfoViewSet, basename="atscontactinfo")
router.register(r'ats-contact-product-info',views.ATSContactProductInfoViewSet, basename="atscontactproductinfo")
router.register(r'ats-contact-product-images',views.ATSContactProductImagesViewSet, basename="atscontactproductimages")
router.register(r'agritech-products-categories', views.ProductViewSet, basename='agritech-products-categories')
router.register(r'featured-listing',views.FeaturedListingViewSet, basename='featured_listing')

urlpatterns = [
	path('api/', include(router.urls)),
    path('f', views.home, name='home'),
    path('new/',views.newo,name='newone'),
    path('front/',views.front,name = 'user'),
    path('product/<int:pk>/', ProductDetailView.as_view(), name='product_detail'),
    path('log/',views.logni,name ='login'),
    path('profile/',views.dash,name ='profile'),
    path('get/',views.list,name='list'),
    path('update/<int:id>',views.update, name="update"),
    path('delete/<int:id>',views.delete,name='delete'),
	path('get-location/',views.get_location, name='get-location'),
	path('aboutus/', views.about, name='aboutus'),
	path('contact/', views.contact, name='contact'),
	path('contact-us-acknowledgement/',views.thankyou,name='contactack'),
	path('blogs/', views.blogs, name='blogs'),
	path('agritech-mart/',views.ats_view, name="ats"),
    path('kcenter/', views.kcenter_view, name="kcenter"),
	path('agritech-mart/<slug:category_slug>/<slug:company_slug>/', views.ats_category_company, name="ats-category-company"),
	path('agritech-mart-seller-enquiry-success/', views.seller_enquiry_success_view,name="atm-seller-success"),
	path('terrace-gardening-products/', views.product, name='product'),
	path('external-links/', views.BacklinksView, name='external-links'),
	path('<str:sub_product_product>/<str:sub_product_slug>/review/',views.review_view, name="review"),
    path('sucessful-review-submission/<str:sub_product_slug>/',views.review_sucess_view, name='sub_product_details-sucess'),
    path('<str:product_category>/<str:sub_product_slug>/', views.sub_product_details, name='sub_product_details'),
    path('<str:product_category>/<str:sub_product_slug>/<int:instance_id>/', views.selected_component_bill, name='sub_product_bill'),
	path('<str:product_slug>/', views.product_details, name='product_details'),
    path('',views.home2,name="home2"),
    path('category/<str:arg>',views.category_dir,name='product_page')
]