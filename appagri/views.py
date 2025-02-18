
class ProductNotFoundError(Exception):
    """Custom Exception to be raised when no products are found."""
    pass
from django.views.generic import ListView,DetailView
from django.shortcuts import render,redirect
from django.http import HttpResponseRedirect ,HttpResponse
from .models import Main_category,sub_cat,Product1,sess,Newone,ContactNumber,Home_Information ,Highlights, Banner, Blogs, Logo, Brands, ReviewResponse
from .models import SeoPageExtLinks,Comments,Contacts,Credentials,Product, Review, ATSInfo, ATSContactInfo, ATSIntro, ATSContactProductInfo, ATSContactProductImages, ATSSeller, ATSSellerProductImage, ATSRoadmap,FeaturedListing, KCenterTopic
from django.shortcuts import render, get_object_or_404
from .forms import Newform, CommentForm, ReviewForm, KitComponentSelectedForm, ATSSellerForm,ATSSellerProductImageFormSet, ContactForm, CategoryForm,TopicForm
from django.urls import reverse,path
from itertools import groupby
from django.db.models import Count, Avg
import math
import json
from django.http import JsonResponse
from django.views.generic import DetailView
import phonenumbers
from .notifications import send_notification
import uuid
from rest_framework import viewsets
from .serializers import ATSSerializer, ATSContactSerializer, ATSIntroSerializer, ATSContactProductSerializer, ATSContactProductImagesSerializer, ContactsSerializer, ProductSerializer,FeaturedListingSerializer
import requests
import datetime
from django.utils import timezone
from django.utils.text import slugify
from django.contrib.auth.forms import UserCreationForm
from django.contrib.auth.forms import AuthenticationForm
from django.contrib.auth.decorators import login_required
from django.contrib.auth import authenticate, login
from django.contrib.auth.models import User
from .models import KitComponent1,KitComponentSelected1,Subproduct_External_links1,Product
from django.contrib import messages 
def getIP(request):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		return ip

def get_ip_location(ip_address):
    api_key = '388b113bade3497c80d9925299af70b7'
    api_url = f'https://ipgeolocation.abstractapi.com/v1/?api_key={api_key}&ip_address={ip_address}'
    response = requests.get(api_url)
    return response.content

class FeaturedListingViewSet(viewsets.ModelViewSet):
	queryset = FeaturedListing.objects.all()
	serializer_class = FeaturedListingSerializer

def get_location(request):
	if request.method == 'POST':
		data = json.loads(request.body)
		city = data.get('city')
		stateDistrict =data.get('stateDistrict')
		district =data.get('district')
		region = data.get('region')
		request.session['city'] = city
		request.session['region'] = region
		request.session['stateDistrict'] = stateDistrict
		request.session['district'] = district
		return JsonResponse({'success': True})
	return JsonResponse({'success': False})

def category_dir(request,arg):  ## new
	print('received',arg)
	messages.add_message(request,messages.INFO,arg)
	return redirect('appagri:home2')
def home2(request):
    seo = SeoPageExtLinks.objects.all()
    title = ""
    desc = ""
    key = ""
    print('step-1')
    for i in seo:
        if i.page == 'home':
            title = i.meta_title
            desc = i.meta_description
            key = i.keywords
            
    logo = Logo.objects.all()
    brands = Brands.objects.all()
    highlight = Highlights.objects.all()
    banners = Banner.objects.all()
    main_info = Home_Information.objects.all()
    main = Main_category.objects.order_by('order_no')
    sub = sub_cat.objects.order_by()
    arg = None
    print(messages.get_messages(request))
    for i in messages.get_messages(request):
        arg = i
    print('message', arg)
    
    pro_info = Product1.objects.filter(product__name=arg)
    spec_cat = sub_cat.objects.filter(name=arg).first()
    all_product = Product1.objects.all()
    page_t = 0
    if arg is not None:
        page_t = 1
        
    main_categories = []
    max_stars = range(5)
    url = request.build_absolute_uri(request.path)
    
    imp_reviews = Review.objects.filter(is_important=True)
    total_reviews = Review.objects.count()
    
    avg_rating_query = Review.objects.aggregate(avg_rating=Avg('rating'))
    if avg_rating_query['avg_rating'] is not None:
        avg_rating = round(avg_rating_query['avg_rating'], 1)
    else:
        avg_rating = 0.0
        
    percentage5 = int((Review.objects.filter(rating=5).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    percentage4 = int((Review.objects.filter(rating=4).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    percentage3 = int((Review.objects.filter(rating=3).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    percentage2 = int((Review.objects.filter(rating=2).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    percentage1 = int((Review.objects.filter(rating=1).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    
    if request.method == 'POST':
        data = request.POST.get('number')
        if data:
            try:
                val_num = phonenumbers.parse(data, 'IN')
                if not phonenumbers.is_valid_number(val_num) or str(val_num.national_number)[0] not in ['9', '8', '7', '6']:
                    return HttpResponseRedirect(request.path)
                else:
                    city = request.session.get('city')
                    district = request.session.get('district')
                    stateDistrict = request.session.get('stateDistrict')
                    region = request.session.get('region')
                    number = ContactNumber.objects.create(phone_number=data, Time=timezone.now(), city=city, district=district, stateDistrict=stateDistrict, region=region)
                    number.save()
                    return HttpResponseRedirect(request.path)
            except:
                return HttpResponseRedirect(request.path)

    url_featured_listing = request.build_absolute_uri(reverse('appagri:featured_listing-list'))
    response = requests.get(url_featured_listing)
    if response.status_code == 200:
        featured_data = response.json()

    return render(request, 'home3.html', context={
        'canonical': url, 
        'page_t': page_t, 
        'max_stars': max_stars, 
        'main_category': main, 
        'banners': banners, 
        'main_info': main_info,
        'all_product': all_product, 
        'spec_cat': spec_cat, 
        'highlight': highlight, 
        'sub_products': sub, 
        'pro_info': pro_info,
        'logo': logo,
        'brands': brands,
        'title': title,
        'desc': desc,
        'key': key, 
        'categories': sub, 
        'total_review': total_reviews,
        'avg_rating': avg_rating,
        'per5': percentage5,
        'per4': percentage4,
        'per3': percentage3,
        'per2': percentage2,
        'per1': percentage1,
        'imp_reviews': imp_reviews, 
        'featured_data': featured_data
    })

def home(request):
	          
    seo = SeoPageExtLinks.objects.all()
    title = ''
    desc = ''
    key = ''
    
    for i in seo:
        if i.page == 'home':
            title = i.meta_title
            desc = i.meta_description
            key = i.keywords

    logo = Logo.objects.all()
    brands = Brands.objects.all()
    highlight = Highlights.objects.all()
    banners = Banner.objects.all()

    products=[]

    try:
        products = get_products()  # Assume this fetches products from a database
    except ProductNotFoundError:
        pass 
    categories = []

    for i in products:
       
        if hasattr(i, 'sub_cat') and i.sub_cat and i.sub_cat.Main_category not in categories:
            categories.append(i.sub_cat.Main_category)

    
    main_info = Home_Information.objects.all()
    products = Product1.objects.order_by('order_no')

   
    def get_categories_for_products(products):
        categories = []
        for i in products:
            if hasattr(i, 'sub_cat') and i.sub_cat and i.sub_cat.Main_category not in categories:
                categories.append(i.sub_cat.Main_category)
        return categories

   
    categories = get_categories_for_products(products)

    sub_products = sub_cat.objects.order_by('product1', 'id')  # Using the correct model 'sub_cat'
    max_stars = range(5)
    url = request.build_absolute_uri(request.path)
    
    imp_reviews = Review.objects.filter(is_important=True)
    total_reviews = Review.objects.count()
    avg_rating_query = Review.objects.aggregate(avg_rating=Avg('rating'))
    avg_rating = round(avg_rating_query['avg_rating'], 1) if avg_rating_query['avg_rating'] else 0.0
    
    
    percentage5 = int((Review.objects.filter(rating=5).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    percentage4 = int((Review.objects.filter(rating=4).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    percentage3 = int((Review.objects.filter(rating=3).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    percentage2 = int((Review.objects.filter(rating=2).count() / total_reviews) * 100 if total_reviews > 0 else 0)
    percentage1 = int((Review.objects.filter(rating=1).count() / total_reviews) * 100 if total_reviews > 0 else 0)

    # Handling the phone number submission
    if request.method == 'POST':
        data = request.POST.get('number')
        if data:
            try:
                val_num = phonenumbers.parse(data, 'IN')
                if not phonenumbers.is_valid_number(val_num) or str(val_num.national_number)[0] not in ['9', '8', '7', '6']:
                    return HttpResponseRedirect(request.path)
                else:
                    city = request.session.get('city')
                    district = request.session.get('district')
                    stateDistrict = request.session.get('stateDistrict')
                    region = request.session.get('region')
                    number = ContactNumber.objects.create(phone_number=data, Time=timezone.now(),
                                                          city=city, district=district, stateDistrict=stateDistrict, region=region)
                    number.save()
                    return HttpResponseRedirect(request.path)
            except:
                return HttpResponseRedirect(request.path)
    
    # Fetching featured listings from an external API
    url_featured_listing = request.build_absolute_uri(reverse('appagri:featured_listing-list'))
    response = requests.get(url_featured_listing)
    if response.status_code == 200:
        featured_data = response.json()

    return render(request, 'home.html', {
        'canonical': url, 'max_stars': max_stars, 'products': products, 'banners': banners, 'main_info': main_info,
        'highlight': highlight, 'sub_products': sub_products, 'logo': logo, 'brands': brands, 'title': title,
        'desc': desc, 'key': key, 'categories': categories, 'total_review': total_reviews, 'avg_rating': avg_rating,
        'per5': percentage5, 'per4': percentage4, 'per3': percentage3, 'per2': percentage2, 'per1': percentage1,
        'imp_reviews': imp_reviews, 'featured_data': featured_data
    })


def sub_product_details(request, product_category, sub_product_slug):  ## new 
	# return HttpResponse('<h1>Successfully done<h1>')
	print('step1')
	logo = Logo.objects.all()
	sub_product = get_object_or_404(Product1, slug=sub_product_slug)  # SubProduct change 
	print(sub_product)
	seo = Subproduct_External_links1.objects.all()
	title=''
	desc=''
	key=''
	for i in seo:
		if i.subproduct == sub_product:
			title = i.meta_title
			desc = i.meta_desc
			key = i.keywords
	parent = sub_product.product
	url = request.build_absolute_uri(request.path)
	components = []
	prices = []
	total_price = {}
	sum1 = 0.00
	kit_components = KitComponent1.objects.filter(kit=sub_product)
	if request.method == 'POST':
		form = KitComponentSelectedForm(data=request.POST)
		instance = KitComponentSelected1()
		if form.is_valid():
			selected_component_names = request.POST.getlist('selected_components')
			quantity_inputs = request.POST.getlist('quantity')
			quants = []
			for i in quantity_inputs:
				if int(i) != 0:
					quants += [i]
				form_instance = form.save(commit=False)
				for component_name in selected_component_names:
					components += [component_name]
					kit_component = KitComponent1.objects.get(component_name = component_name)
					prices += [kit_component.component_sales_price]
				for n, q, p in zip(selected_component_names, quants, prices):
					total_price[n] = int(q) * float(p)
				for price in total_price:
					sum1 += total_price[price]
				if int(sum1) >= 1000:
					discount_price = sum1 - ((sum1 * 5) /100)
				elif int(sum1) >= 3000:
					discount_price = sum1 - ((sum1 * 6) /100)
				elif int(sum1) >= 5000:
					discount_price = sum1 - ((sum1 * 7) /100)
				else:
					discount_price = sum1
				form_instance.kit = sub_product
			
				form_instance.selected_component = selected_component_names
				form_instance.quantity = quants
				form_instance.total_amount = f'₹. {sum1}'
				form_instance.discount_price = f'₹. {discount_price}'
				form_instance.save()
				print('successfultty saved')
				instance = KitComponentSelected1.objects.get(id=form_instance.id)
				instance_id = instance.id
				return redirect(reverse('appagri:sub_product_bill', args=[product_category, sub_product_slug, instance_id]))
			else:
				form = KitComponentSelectedForm()
			return render(request, 'sub_product_details.html', {'canonical':url, 'sub_product': sub_product, 'logo': logo, 'parent': parent,'title':title,'desc':desc,'key':key,'reviews':reviews,'product_reviews':product_reviews,'total_rate':total_rate,'kit_components':kit_components, 'form':form})  #    changed
	else:
		form = KitComponentSelectedForm()
	reviews = Review.objects.all()
	print('step3')
	try:
		product_reviews = Review.objects.filter(product=sub_product.name, is_approved=True).order_by('-rating')
		total_user = Review.objects.filter(product=sub_product.name, is_approved=True).aggregate(total_count=Count('name'))
		average_rating = product_reviews.aggregate(avg_rating=Avg('rating'))
		if average_rating['avg_rating'] is not None and total_user['total_count'] > 0:
			total_rating = average_rating['avg_rating'] * total_user['total_count']
			total_user_count = total_user['total_count']
			total_rate = total_rating / total_user_count
		else:
			total_rate = None
	except Review.DoesNotExist:
		product_reviews = None
	print('full')
	return render(request, 'sub_product_details.html', {'canonical':url, 'sub_product': sub_product, 'logo': logo, 'parent': parent,'title':title,'desc':desc,'key':key,'reviews':reviews,'product_reviews':product_reviews,'total_rate':total_rate,'kit_components':kit_components,'form':form})   #    changed

def review_view(request, sub_product_product, sub_product_slug):
	url = request.build_absolute_uri(request.path)
	logo = Logo.objects.all()
	sub_product = get_object_or_404(Product1.objects.order_by('order_no'), slug=sub_product_slug) # changed 
	device_ip = getIP(request)
	if request.method == 'POST':
		rating_form = ReviewForm(request, data=request.POST, files=request.FILES)
		print('post render')
		if rating_form.is_valid():
			review = rating_form.save(commit=False)
			review.product = sub_product.name
			review.review_token = uuid.uuid4().hex[:10]
			review.ip_address = device_ip
			review.date = datetime.date.today()
			try:
				parsed_number = phonenumbers.parse(review.whatsapp_no,'IN')
				if not phonenumbers.is_valid_number(parsed_number) and str(parsed_number.national_number)[0] not in ['9', '8', '7', '6']:
					message = 'Invalid Phone number: Must be of 10 digit length and Must start with 9, 8, 7 or 6'
					rating_form = ReviewForm(request, data=request.POST, files=request.FILES)
					return render(request,'product_review.html',{'sub_product_product':sub_product_product,'sub_product_slug':sub_product_slug,'rating_form':rating_form,'sub_product':sub_product,'canonical':url,'message':message,'logo':logo})
				elif str(parsed_number.national_number)[0] not in ['9', '8', '7', '6']:
					message = 'Invalid Phone Number: Must start with 9, 8, 7, or 6'
					rating_form = ReviewForm(request,data=request.POST, files=request.FILES)
					return render(request,'product_review.html',{'sub_product_product':sub_product_product,'sub_product_slug':sub_product_slug,'rating_form':rating_form,'sub_product':sub_product,'canonical':url,'message':message,'logo':logo})
				elif not phonenumbers.is_valid_number(parsed_number):
					message = 'Invalid Phone Number: must be of 10 digit'
					rating_form = ReviewForm(request,data=request.POST, files=request.FILES)
					return render(request,'product_review.html',{'sub_product_product':sub_product_product,'sub_product_slug':sub_product_slug,'rating_form':rating_form,'sub_product':sub_product,'canonical':url,'message':message,'logo':logo})
			except phonenumbers.phonenumberutil.NumberParseException:
				message = 'Invalid Phone number'
				rating_form = ReviewForm(request, data=request.POST, files=request.FILES)
				return render(request,'product_review.html',{'sub_product_product':sub_product_product,'sub_product_slug':sub_product_slug,'rating_form':rating_form,'sub_product':sub_product,'canonical':url,'message':message,'logo':logo})
			review.save()
			instance = Review.objects.get(id=review.id)
			subject = f'UrbanAgricuture.in: {instance.product} review'
			message = f'''Review for {instance.product} from <em style="color:darkblue">urbanagriculture.in</em>.<br>
            	<strong>Customer Name:</strong> {instance.name}<br>
            	<strong>Phone Number: </strong>{instance.whatsapp_no}<br>
            	<strong>Product Rating: </strong>{instance.rating}<br>
            	{'<strong>Review:</strong> ' + instance.review if instance.review else ''}'''
			recipient_list = ['way2agritech@way2agribusiness.com']
			# send_notification(subject, message, recipient_list)
			return redirect(reverse('appagri:sub_product_details-sucess', args=[sub_product_slug]))
		else:
			message = ''
			for field, errors in rating_form.errors.items():
				for error in errors:
					message += f"{error}\n"
			return render(request,'product_review.html',{'sub_product_product':sub_product_product,'sub_product_slug':sub_product_slug,'rating_form':rating_form,'sub_product':sub_product,'canonical':url,'message':message,'logo':logo})
	else:
		rating_form = ReviewForm(request)
		print('rendered')
	return render(request, 'product_review.html',{'sub_product_product':sub_product_product,'sub_product_slug':sub_product_slug,'rating_form':rating_form,'sub_product':sub_product,'canonical':url,'logo':logo})

def review_sucess_view(request, sub_product_slug):
	url = request.build_absolute_uri(request.path)
	logo = Logo.objects.all()
	sub_product = get_object_or_404(Product1.objects.order_by('order_no'), slug=sub_product_slug) # changed 
	return render(request, 'review_sucess.html',{'sub_product':sub_product,'logo':logo, 'canonical':url})

def selected_component_bill(request, product_category, sub_product_slug, instance_id):
	bill = KitComponentSelected1.objects.get(id=instance_id) #  changed 	
	logo = Logo.objects.all()
	j=[]
	qt=[]
	sub_product = get_object_or_404(Product1, slug=sub_product_slug) # changed 
	kit_components = KitComponent1.objects.filter(kit=sub_product) # changed 
	if ',' in bill.selected_component:
		component = str(bill.selected_component).split(',')
		for i in component:
			if '[' in i or ']' in i or "'" in i:
				j += [i.replace('[','').replace(']','').replace("'",'')]
	if ',' in bill.quantity:
		quants = str(bill.quantity).split(',')
		for q in quants:
			if '[' in q or ']' in q or "'" in q:
				qt += [q.replace('[','').replace(']','').replace("'",'')]
	comp = zip(j, qt)
	return render(request, 'sub_product_bill.html', {'bill':bill,'product_category':product_category,'sub_product_slug':sub_product_slug, 'logo':logo, 'sub_product':sub_product,'kit_components': kit_components, 'selected_component':comp, 'selected_quantity':qt})

def product(request):
	logo = Logo.objects.all()
	products = sub_cat.objects.all()  # changed
	url = request.build_absolute_uri(request.path)
	return render(request, 'products.html', {'canonical':url, 'products': products, 'logo': logo})

def get_products():
    return Product.objects.all()
from django.http import Http404
from .models import Product

def product_details(request, product_slug):
    try:
        # Try to retrieve the product by its slug
        product = Product.objects.get(slug=product_slug)
    except Product.DoesNotExist:
        # If the product does not exist, raise a 404 error
        raise Http404("Product not found")
    
    # If the product is found, render the product_detail template
    return render(request, 'product_detail.html', {'product': product})

def blogs(request):
	seo = SeoPageExtLinks.objects.all()
	title=''
	desc=''
	key=''
	for i in seo:
		if i.page == 'video blogs':
			title = i.meta_title
			desc = i.meta_description
			key = i.keywords
	logo = Logo.objects.all()
	blog = Blogs.objects.all()
	if request.method == 'POST':
		comment_form = CommentForm(data=request.POST)
		if comment_form.is_valid():
			comment = comment_form.save(commit=False)
			video_id = request.POST.get('video_id')
			comment.video = get_object_or_404(Blogs, pk=video_id)
			comment.save()
		return HttpResponseRedirect(reverse('appagri:blogs'))
	else:
		comment_form = CommentForm()
	comments = Comments.objects.all().order_by('-id')
	url = request.build_absolute_uri(request.path)
	return render(request, 'blogs.html', {'canonical':url, 'blog': blog, 'logo': logo,'form':comment_form,'comment':comments,'title':title,'desc':desc,'key':key})

def about(request):
	seo = SeoPageExtLinks.objects.all()
	title=''
	desc=''
	key=''
	for i in seo:
		if i.page == 'aboutus':
			title = i.meta_title
			desc = i.meta_description
			key = i.keywords
	logo = Logo.objects.all()
	brands = Brands.objects.all()
	c_images = Credentials.objects.order_by('type_of_image')
	grouped_images = []
	for key, group in groupby(c_images, key=lambda x: x.get_type_of_image_display()):
		grouped_images.append({'type_of_image': key, 'images': list(group)})
	url = request.build_absolute_uri(request.path)
	return render(request,'aboutus.html',{'canonical':url, 'logo':logo,'brands':brands,'grouped_images':grouped_images,'title':title,'desc':desc,'key':key})

def contact(request):
	url = request.build_absolute_uri(request.path)
	highlight = Highlights.objects.all()
	seo = SeoPageExtLinks.objects.filter(page="contactus").first()
	title=seo.meta_title if seo else ''
	desc=seo.meta_description if seo else ''
	key=seo.keywords if seo else ''
	logo = Logo.objects.all()
	if request.method == "POST":
		form = ContactForm(data=request.POST)
		if form.is_valid():
			number = form.cleaned_data['number']
			try:
				parsed_number = phonenumbers.parse(number,'IN')
				if not phonenumbers.is_valid_number(parsed_number) and str(parsed_number.national_number)[0] not in ['9', '8', '7', '6']:
					message = 'Invalid Phone number: Must be of 10 digit length and Must start with 9, 8, 7 or 6'
					form = ContactForm(data=request.POST)
					return render(request, 'contact.html',{'canonical':url,'logo':logo,'title':title,'desc':desc,'key':key,'message':message,'form':form, 'message':message,'highlight':highlight})
				elif str(parsed_number.national_number)[0] not in ['9', '8', '7', '6']:
					message = 'Invalid Phone Number: Must start with 9, 8, 7, or 6'
					form = ContactForm(data=request.POST)
					return render(request, 'contact.html',{'canonical':url,'logo':logo,'title':title,'desc':desc,'key':key,'message':message,'form':form, 'message':message,'highlight':highlight})
				elif not phonenumbers.is_valid_number(parsed_number):
					message = 'Invalid Phone Number: must be of 10 digit'
					form = ContactForm(data=request.POST)
					return render(request, 'contact.html',{'canonical':url,'logo':logo,'title':title,'desc':desc,'key':key,'message':message,'form':form, 'message':message,'highlight':highlight})
			except phonenumbers.phonenumberutil.NumberParseException:
				message = 'Invalid Phone number'
				form = ContactForm(data=request.POST)
				return render(request, 'contact.html',{'canonical':url,'logo':logo,'title':title,'desc':desc,'key':key,'message':message,'form':form, 'message':message,'highlight':highlight})
			main_instance=form.save()
			instance = Contacts.objects.get(id=main_instance.id)
			subject = 'Message from Contact Us of urbanagriculture.in'
			message = f''' Message from <strong>Contact Us</strong> of <em style="color:darkblue">urbanagriculture.in</em><br>
            		<strong>Customer Name: </strong>{instance.name}<br>
                    <strong>Phone number: </strong>{instance.number}<br>
                    <strong>Customer Message: </strong>{instance.comments}'''
			recipient_list = ['way2agritech@way2agribusiness.com']
			send_notification(subject, message, recipient_list)
			redirected_path=reverse('appagri:contactack')
			return redirect(redirected_path)
	else:
		form = ContactForm()
	return render(request, 'contact.html',{'canonical':url,'logo':logo,'title':title,'desc':desc,'key':key,'form':form,'highlight':highlight})

def thankyou(request):
	logo = Logo.objects.all()
	url=request.build_absolute_uri(request.path)
	return render(request,'contactus_thankyou.html',{'logo':logo,'canonical':url})

def BacklinksView(request):
	links_list = SeoPageExtLinks.objects.values_list('backlinks', flat=True)
	links_list = [links.split(',') for links in links_list if links]
	unique_links = [list(set(sublist)) for sublist in links_list]
	return render(request, 'backlinks.html',{'links_list':unique_links})

def kcenter_categories(request):
    seo = SeoPageExtLinks.objects.all()
    title=''
    desc=''
    key=''
    for i in seo:
        if i.page == 'kcenter':
            title = i.meta_title
            desc = i.meta_description
            key = i.keywords
    logo = Logo.objects.all()
    url = request.build_absolute_uri(request.path)
    if request.method == 'POST':
        form = CategoryForm(request.POST) 
        if form.is_valid():
            selected_category = form.cleaned_data['categories']
            return redirect(reverse('appagri:kcenter-category', args=[slugify(selected_category)]))
    else:
        form = CategoryForm()
    return render(request, 'kcenter.html', {'form': form,'logo':logo,'canonical':url,'title':title,'desc':desc,'key':key})

def kcenter_selected_categories(request, category_slug):
    seo = SeoPageExtLinks.objects.all()
    title=''
    desc=''
    key=''
    for i in seo:
        if i.page == 'kcenter':
            title = i.meta_title
            desc = i.meta_description
            key = i.keywords
    logo = Logo.objects.all()
    url = request.build_absolute_uri(request.path)
    if request.method=='POST':
        if 'categories' in request.POST:
            form = CategoryForm(request.POST) 
            if form.is_valid():
                selected_category=form.cleaned_data['categories']
                return redirect(reverse('appagri:kcenter-category', args=[slugify(selected_category)]))
        elif 'ktopic' in request.POST:
            form1 = TopicForm(request,request.POST)
            if form1.is_valid():
                selected_topic=form1.cleaned_data['ktopic']
                return redirect(reverse('appagri:kcenter-topic', args=[category_slug, slugify(selected_topic)]))
    else:
        form=TopicForm(request)
        form1 = CategoryForm()
    return render(request, 'kcenter-topic.html', {'category_slug':category_slug,'form':form, 'form1':form1,'logo':logo,'canonical':url,'title':title,'desc':desc,'key':key})

def kcenter_selected_topic(request, category_slug, topic_slug):
    seo = SeoPageExtLinks.objects.all()
    title=''
    desc=''
    key=''
    for i in seo:
        if i.page == 'kcenter':
            title = i.meta_title
            desc = i.meta_description
            key = i.keywords
    logo = Logo.objects.all()
    url = request.build_absolute_uri(request.path)
    if request.method=='POST':
        if 'categories' in request.POST:
            form = CategoryForm(request.POST) 
            if form.is_valid():
                selected_category=form.cleaned_data['categories']
                return redirect(reverse('appagri:kcenter-category', args=[slugify(selected_category)]))
        elif 'ktopic' in request.POST:
            form1 = TopicForm(request,request.POST)
            if form1.is_valid():
                selected_topic=form1.cleaned_data['ktopic']
                return redirect(reverse('appagri:kcenter-topic', args=[category_slug, slugify(selected_topic)]))
    else:
        form=TopicForm(request)
        form1 = CategoryForm()
    selected_topic = kcentertopic.objects.get(ktopic_slug=topic_slug)
    topic_contents = selected_topic.ktopictext.split('.')
    return render(request, 'kcenter-selected-topic-content.html', {'category_slug':category_slug,'form':form,'topic_slug':topic_slug,'selected_topic':selected_topic,'form1':form1,'logo':logo,'canonical':url,'title':title,'desc':desc,'key':key,'topic_contents':topic_contents})

def ats_view(request):
	logo = Logo.objects.all()
	try:
		roadmap = ATSRoadmap.objects.get(id=1)
	except ATSRoadmap.DoesNotExist:
		roadmap = None
	url = request.build_absolute_uri(request.path)
	url_ats_intro = request.build_absolute_uri(reverse('appagri:atsintro-list'))
	url_ats_info = request.build_absolute_uri(reverse('appagri:atsinfo-list'))
	url_ats_contact = request.build_absolute_uri(reverse('appagri:atscontactinfo-list'))
	response3 = requests.get(url_ats_intro)
	response1 = requests.get(url_ats_info)
	response2 = requests.get(url_ats_contact)
	data = intro = contact_info = None
	if response1.status_code == 200 and response2.status_code == 200 and response3.status_code == 200:
		data = response1.json()
		contact_info = response2.json()
		intro = response3.json()
	if request.method == 'POST':
		if 'select-form2' in request.POST:
			value = request.POST.get('select-form2')
			url = reverse(f"appagri:{value.split('--')[1]}", args=[value.split('--')[2],value.split('--')[3]])
			return redirect(url)
		elif 'form1' in request.POST:
			form = ATSSellerForm(data=request.POST)
			image_formset = ATSSellerProductImageFormSet(data=request.POST, files=request.FILES, instance=ATSSeller())
			if form.is_valid() and image_formset.is_valid():
				phone = form.cleaned_data['seller_company']
				try:
					parsed_number = phonenumbers.parse(phone,'IN')
					if not phonenumbers.is_valid_number(parsed_number) and str(parsed_number.national_number)[0] not in ['9', '8', '7', '6']:
						message = 'Invalid Phone number: Must be of 10 digit length and Must start with 9, 8, 7 or 6'
						form = ATSSellerForm(data=request.POST)
						return render(request, 'ats.html',{'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro,'image_formset':image_formset,'message':message,'canonical':url, 'roadmap':roadmap})
					elif str(parsed_number.national_number)[0] not in ['9', '8', '7', '6']:
						message = 'Invalid Phone Number: Must start with 9, 8, 7, or 6'
						form = ATSSellerForm(data=request.POST)
						return render(request, 'ats.html',{'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro,'image_formset':image_formset,'message':message,'canonical':url,'roadmap':roadmap})
					elif not phonenumbers.is_valid_number(parsed_number):
						message = 'Invalid Phone Number: must be of 10 digit'
						form = ATSSellerForm(data=request.POST)
						return render(request, 'ats.html',{'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro,'image_formset':image_formset,'message':message,'canonical':url,'roadmap':roadmap})
				except phonenumbers.phonenumberutil.NumberParseException:
					message = 'Invalid Phone number'
					form = ATSSellerForm(data=request.POST)
					return render(request, 'ats.html',{'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro,'image_formset':image_formset,'message':message,'canonical':url,'roadmap':roadmap})
				main_instance = form.save()
				image_formset.instance = main_instance
				image_formset.save()
				instance = ATSSeller.objects.get(id=main_instance.id)
				subject = f'{url}: Agritech Mart Seller Enquiry'
				message = f'Agritech Mart Seller Enquiry from {url}. Customer Name: {instance.seller_name}, Phone number: {instance.seller_company} and Address: {instance.seller_address}'
				recipient_list = ['dr.prasannad@way2agribusiness.com']
				send_notification(subject, message, recipient_list)
				return redirect(reverse('appagri:atm-seller-success'))
		else:
			return HttpResponse('none has been submiitted')
	form = ATSSellerForm() 
	image_formset = ATSSellerProductImageFormSet()
	return render(request, 'ats.html', {'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro,'image_formset':image_formset,'canonical':url,'roadmap':roadmap})

def ats_category_company(request, category_slug, company_slug):
	logo = Logo.objects.all()
	try:
		roadmap = ATSRoadmap.objects.get(id=1)
	except ATSRoadmap.DoesNotExist:
		roadmap = None
	url = request.build_absolute_uri(request.path)
	url_ats_intro = request.build_absolute_uri(reverse('appagri:atsintro-list'))
	url_ats_info = request.build_absolute_uri(reverse('appagri:atsinfo-list'))
	url_ats_contact = request.build_absolute_uri(reverse('appagri:atscontactinfo-list'))
	url_ats_contact_product = request.build_absolute_uri(reverse('appagri:atscontactproductinfo-list'))
	url_ats_contact_product_images = request.build_absolute_uri(reverse('appagri:atscontactproductimages-list'))
	response1 = requests.get(url_ats_intro)
	response2 = requests.get(url_ats_info)
	response3 = requests.get(url_ats_contact)
	response4 = requests.get(url_ats_contact_product)
	response5 = requests.get(url_ats_contact_product_images)
	data = intro = None
	if response1.status_code == 200 and response2.status_code == 200 and response3.status_code==200 and response4.status_code==200 and response5.status_code==200:
		intro = response1.json()
		data = response2.json()
		contact_info = response3.json() 
		product_info = response4.json()
		product_images = response5.json()
		product_image_dict = {}
		for image in product_images:
			product_name = image['seller_product']['product_name']
			if product_name not in product_image_dict:
				product_image_dict[product_name] = [image['product_image']]
			else:
				product_image_dict[product_name].append(image['product_image'])
	if request.method == 'POST':
		if 'select-form2' in request.POST:
			category_slug = request.POST.get('selected-category')
			company_slug = request.POST.get('selected-company')
			if category_slug and company_slug:
				url = reverse(f"appagri:ats-category-company", args=[category_slug, company_slug])
				return redirect(url)
		elif 'form1' in request.POST:
			form = ATSSellerForm(data=request.POST)
			image_formset = ATSSellerProductImageFormSet(data=request.POST, files=request.FILES, instance=ATSSeller())
			if form.is_valid() and image_formset.is_valid():
				phone = form.cleaned_data['seller_company']
				try:
					parsed_number = phonenumbers.parse(phone,'IN')
					if not phonenumbers.is_valid_number(parsed_number) and str(parsed_number.national_number)[0] not in ['9', '8', '7', '6']:
						message = 'Invalid Phone number: Must be of 10 digit length and Must start with 9, 8, 7 or 6'
						form = ATSSellerForm(data=request.POST)
						return render(request, 'ats.html',{'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro, 'product_info': product_info,'image_formset':image_formset,'message':message,'canonical':url, 'product_images':product_images,'roadmap':roadmap})
					elif str(parsed_number.national_number)[0] not in ['9', '8', '7', '6']:
						message = 'Invalid Phone Number: Must start with 9, 8, 7, or 6'
						form = ATSSellerForm(data=request.POST)
						return render(request, 'ats.html',{'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro, 'product_info': product_info,'image_formset':image_formset,'message':message,'canonical':url,'product_images':product_images,'roadmap':roadmap})
					elif not phonenumbers.is_valid_number(parsed_number):
						message = 'Invalid Phone Number: must be of 10 digit'
						form = ATSSellerForm(data=request.POST)
						return render(request, 'ats.html',{'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro, 'product_info': product_info,'image_formset':image_formset,'message':message,'canonical':url,'product_images':product_images,'roadmap':roadmap})
				except phonenumbers.phonenumberutil.NumberParseException:
					message = 'Invalid Phone number'
					form = ATSSellerForm(data=request.POST)
					return render(request, 'ats.html',{'form': form, 'data': data, 'logo': logo, 'contact_info': contact_info, 'intro': intro, 'product_info': product_info,'image_formset':image_formset,'message':message,'canonical':url,'product_images':product_images,'roadmap':roadmap})
				main_instance = form.save()
				image_formset.instance = main_instance
				image_formset.save()
				instance = ATSSeller.objects.get(id=main_instance.id)
				subject = f'{url}: Agritech Mart Seller Enquiry'
				message = f'Agritech Mart Seller Enquiry from {url}. Customer Name: {instance.seller_name}, Phone number: {instance.seller_company} and Address: {instance.seller_address}'
				recipient_list = ['dr.prasannad@way2agribusiness.com']
				send_notification(subject, message, recipient_list)
				return redirect(reverse('appagri:atm-seller-success'))
		else:
			return HttpResponse('none has been submiitted')
	form = ATSSellerForm() 
	image_formset = ATSSellerProductImageFormSet()
	return render(request, 'atm-category-company.html', {'category_slug':category_slug,'company_slug':company_slug,'logo':logo,'roadmap':roadmap,'form':form,'image_formset':image_formset,'intro':intro,'data':data,'contact_info':contact_info,'product_info':product_info,'product_images':product_images,'canonical':url,'product_image_dict':product_image_dict})

def newo(request):
	if request.method == "POST":
		form = Newform(request.POST)
		print('hreloeoe')
		if form.is_valid():
			print('yes form is valid only ')
			print(form.cleaned_data['name'])
			fm=form.save(commit=False)
			fm.save()
			return redirect('appagri:newone')
		return render(request, 'new.html', {'form': form})
	form = Newform()
	print('from is rendered')
	return render(request,'new.html',context={'form':form})

@login_required
def list(request):
	mod = Newone.objects.all()
	return render (request,'new.html',context={'mod':mod})

def update(request,id):
	item = get_object_or_404(Newone,id=id)
	if request.method == 'POST':
		form = Newform(request.POST,instance=item)
		if form.is_valid():
			form.save()
			return redirect('appagri:list')
		else:
			return render(request,'new2.html',context={'form':form})
		
	else:
		form = Newform(instance=item)
	return render(request,'new2.html',context={'form':form})

def delete(request,id):
	item = get_object_or_404(Newone,id=id)
	item.delete()
	return redirect('appagri:list')

def front(request):
	if request.method == "POST":
		sav= UserCreationForm(request.POST)
		print("1-done")
		if sav.is_valid():
			request.session['user_id']=request.POST('user_name')
			request.session.set_expiry(300)
			sav.save()
			print('2-done')
			return redirect('appagri:login')
	print('rendered')
	form = UserCreationForm()
	return render(request,'new.html',context={'user':form})
def logni(request):
	# usear = request.session.get('user_id')
	# user = User.objects.get(pk=usear)
	# print("log-",usear)
	# if usear:
	# 	login(request,user)
	# 	return redirect('appagri:profile')
	if request.method == 'POST':
		form=AuthenticationForm(request,request.POST)
		print('1-done')
		if form.is_valid():
			user = form.get_user()
			print(user)
			login(request,user)
			print('2-done')
			return redirect('appagri:profile')
	form = AuthenticationForm()
	print('rendered')
	return render(request,'new3.html',context={'form':form})

def dash(request):
	request.session['user_id']=request.user.username
	ji=request.session['user_id']=request.user.username
	print('jii')
	sess_name = sess(name=ji)
	sess_name.save()
	print(ji)
	request.session.set_expiry(300)
	return render(request,'new4.html')

def seller_enquiry_success_view	(request):
	logo = Logo.objects.all()
	url = request.build_absolute_uri(request.path)
	return render(request, 'ats_seller_enquiry_success.html',{'logo':logo,'canonical':url})

class ATSIntroViewSet(viewsets.ModelViewSet):
	queryset = ATSIntro.objects.all()
	serializer_class = ATSIntroSerializer

class ATSInfoViewSet(viewsets.ModelViewSet):
	queryset = ATSInfo.objects.all()
	serializer_class = ATSSerializer

class ATSContactInfoViewSet(viewsets.ModelViewSet):
	queryset = ATSContactInfo.objects.all()
	serializer_class = ATSContactSerializer

class ATSContactProductInfoViewSet(viewsets.ModelViewSet):
	queryset = ATSContactProductInfo.objects.all()
	serializer_class = ATSContactProductSerializer

class ATSContactProductImagesViewSet(viewsets.ModelViewSet):
	queryset = ATSContactProductImages.objects.all()
	serializer_class = ATSContactProductImagesSerializer


class ProductViewSet(viewsets.ModelViewSet):
    queryset = Product.objects.all()  # The queryset of all products
    serializer_class = ProductSerializer 


class ProductDetailView(DetailView):
    model = Product  # Ensure this points to the correct model
    template_name = 'product_details.html'  # Name of your template for product detail
    context_object_name = 'product'  # The object will be available as 'product' in the template