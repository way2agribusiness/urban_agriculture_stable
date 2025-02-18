from django.contrib import admin
from .models import ContactNumber, Newone,sess,Banner, Highlights, Home_Information, Blogs, Logo, ATSInfo, ATSContactInfo,ATSContactProductInfo,ATSContactProductImages,ATSIntro,ATSSeller, ATSSellerProductImage, ATSRoadmap
from .models import Brands,Product1, SeoPageExtLinks,Credentials,Comments,Contacts, Review, KCenterTopic
from django.utils.safestring import mark_safe
from django.db import models
from django.forms import TextInput
from  .models import Main_category,sub_cat,Subproduct_External_links1,KitComponent1,KitComponentSelected1,Product1, KitComponentSelected, KitComponent, SubProduct
from .models import SubProduct
from .models import KCenter, KCenterTopic

class Subproduct_External_links1Admin(admin.ModelAdmin):
	list_display = ['meta_title']

class KitComponent1Admin(admin.ModelAdmin):
	list_display = ['kit','component_name','component_quantity']

class KitComponentSelected1Admin(admin.ModelAdmin):
	list_display = ['customer_name','phone_no','kit','get_total_amount','get_discount_price','get_selected_component']

	def get_total_amount(self, obj):
		return mark_safe(f'<strong style="color:brown">{obj.total_amount}</strong>')
	get_total_amount.short_description = 'Total Price'

	def get_discount_price(self, obj):
		return mark_safe(f'<strong style="color: green">{obj.discount_price}</strong>')
	get_discount_price.short_description = 'Discount Price'

	def get_selected_component(self, obj):
		component_with_quantity = {}
		if obj.selected_component is not None and obj.quantity is not None:
			selected_components_list = obj.selected_component.split(',')
			quantities_list = obj.quantity.split(',')
		if len(selected_components_list) != len(quantities_list):
			return '-' 
		for component_no in range(len(selected_components_list)):
			component = selected_components_list[component_no]
			quant = quantities_list[component_no]
			component_with_quantity[component] = quant  
		table = '<table>'
		for key, value in component_with_quantity.items():
			table += f"<tr><td>{key}</td><td>{value}</td></tr>"
		table += '</table>'
		return mark_safe(table) if table != '<table></table>' else '-'
	get_selected_component.short_description = 'Selected Component'


class Main_categoryAdmin(admin.ModelAdmin):
	list_display = ['name','order_no']
	list_editable = ['order_no']

class sub_catAdmin(admin.ModelAdmin):
	list_dispaly = ['name','order_no']

class product1Admin(admin.ModelAdmin):
	list_display=['name','product','order_no']
	ordering = ['product','order_no']
	list_editable = ['product','order_no']
	prepopulated_fields = {'slug':('name',)}

admin.site.register(Subproduct_External_links1,Subproduct_External_links1Admin)
admin.site.register(KitComponent1,KitComponent1Admin)
admin.site.register(KitComponentSelected1,KitComponentSelected1Admin)
admin.site.register(Product1,product1Admin)
admin.site.register(Main_category,Main_categoryAdmin)
admin.site.register(sub_cat,sub_catAdmin)

class sessAdmin(admin.ModelAdmin):
	list_display = ['name']

class NewoneAdmin(admin.ModelAdmin):
	list_display = ['name','number','place','message','email','date','course']

class ContactNumberAdmin(admin.ModelAdmin):
	list_display = ['phone_number','Time','is_seen']

class ContactAdmin(admin.ModelAdmin):
	list_display = ['name','place','number','comments','date','is_seen']

class CredentialAdmin(admin.ModelAdmin):
    list_display=['type_of_image','title']

class CommentAdmin(admin.ModelAdmin):
    list_display=['name','comment','date']

class BlogAdmin(admin.ModelAdmin):
    list_display=['id','blog_heading']


class ReviewAdmin(admin.ModelAdmin):
	list_display = ['product',"review_token",'name','rating','review','is_approved','whatsapp_no']
	list_editable = ['is_approved','rating']
	search_fields = ['product']


class ATSContactProductImagesInline(admin.StackedInline):
      model = ATSContactProductImages
      extra = 1

class ATSContactProductInfoInline(admin.StackedInline):
      model = ATSContactProductInfo
      extra = 1
      
class ATSContactInfoAdmin(admin.ModelAdmin):
      inlines = [ATSContactProductInfoInline, ATSContactProductImagesInline]
      list_display = ['category','contact_company_name','contact_name','contact_email']

class ATSSellerProductImageInline(admin.StackedInline):
      model=ATSSellerProductImage
      extra=0
      
class ATSSellerAdmin(admin.ModelAdmin):
	inlines=[ATSSellerProductImageInline]
	list_display = ['seller_name','seller_company','seller_email_id']

class ATSInfoAdmin(admin.ModelAdmin):
      list_display = ['category_name']
      prepopulated_fields={'category_slug':('category_name', )}

class KCenterTopicInline(admin.TabularInline):
    model = KCenterTopic
    extra = 1  # One extra blank row for topics

class KCenterCategoriesAdmin(admin.ModelAdmin):
    list_display = ['title', 'display_categories']  # Adjusted to display custom method
    prepopulated_fields = {'slug': ('title',)}

    def display_categories(self, obj):
        # Returns a comma-separated list of category names
        return ", ".join([category.name for category in obj.categories.all()])
    display_categories.short_description = 'Categories'  # Display name in admin

    inlines = [KCenterTopicInline]  # Add KCenterTopicInline here



class KCenterTopicAdmin(admin.ModelAdmin):
    list_display = ['display_category', 'ktopic', 'ktopic_slug', 'ktopicintro']
    prepopulated_fields = {'ktopic_slug': ('ktopic',)}

    def display_category(self, obj):
        # Return the category name or 'No Category' if the topic has no category
        return obj.category.name if obj.category else 'No Category'
    display_category.short_description = 'Category'  # Disp

class KitComponentInline(admin.TabularInline):
    model = KitComponent1
    extra = 1
    fields = ['kit', 'component_name', 'component_quantity']  # Display specific fields


@admin.register(SubProduct)
class SubProductAdmin(admin.ModelAdmin):
    inlines = [KitComponentInline]
    list_display = ['name', 'product', 'sales_price', 'mrp']

class KitComponentSelectedInline(admin.TabularInline):
    model = KitComponentSelected1
    readonly_fields = ('total_amount', 'discount_price')
    extra = 0

@admin.register(KitComponentSelected)
class KitComponentSelectedAdmin(admin.ModelAdmin):
    list_display = ['customer_name', 'kit', 'total_amount', 'created_at']
    list_filter = ['created_at']
    search_fields = ['customer_name', 'phone_no']

admin.site.register(Logo)
admin.site.register(Banner)
admin.site.register(Home_Information)
admin.site.register(Highlights)

admin.site.register(Blogs,BlogAdmin)
admin.site.register(Brands)
admin.site.register(SeoPageExtLinks)
admin.site.register(Credentials,CredentialAdmin)
admin.site.register(Comments,CommentAdmin)
admin.site.register(Contacts,ContactAdmin)
admin.site.register(Review, ReviewAdmin)

admin.site.register(ATSIntro)
admin.site.register(ATSInfo, ATSInfoAdmin)
admin.site.register(ATSContactInfo, ATSContactInfoAdmin)
admin.site.register(ATSSeller, ATSSellerAdmin)
admin.site.register(ATSRoadmap)
admin.site.register(KCenter, KCenterCategoriesAdmin)
admin.site.register(KCenterTopic, KCenterTopicAdmin)
admin.site.register( ContactNumber, ContactNumberAdmin)
admin.site.register(Newone,NewoneAdmin)
admin.site.register(sess,sessAdmin)