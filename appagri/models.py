from django.db import models
from django.utils.html import format_html
from cloudinary.models import CloudinaryField
from django.utils.text import slugify
from django.core.exceptions import ValidationError


class ContactNumber(models.Model):
	phone_number = models.CharField(max_length=20)
	Time= models.DateTimeField(null=True)
	is_seen=models.BooleanField(null=True) 
	city = models.CharField(max_length=100, null=True, blank=True)
	remarks = models.CharField(max_length=500,null=True, blank=True)
	district=models.CharField(max_length=20,null=True)
	stateDistrict=models.CharField(max_length=20,null=True)
	region=models.CharField(max_length=20,null=True)
    
	def __str__(self):
		return self.phone_number

	class Meta:
		verbose_name = 'Contact Number'
		verbose_name_plural = 'Contact Number'


class SeoPageExtLinks(models.Model):
	PAGES = (('home','Home'),
             ('aboutus','About Us'),
             ('contactus','Contact Us'),
             ('video blogs','Video Blogs'),
             ('agritech mart','Agritech Mart'),
             ('kcenter','K Center'))
	page = models.CharField(max_length=50, choices=PAGES)
	meta_title = models.CharField(max_length=255, null=True, blank=True)
	meta_description = models.TextField(null=True, blank=True)
	keywords = models.TextField(null=True, blank=True)
	backlinks = models.TextField(null=True, blank=True)

	def __str__(self):
		return self.page

	class Meta:
		verbose_name = 'Enter SEO Content Page Wise'
		verbose_name_plural = 'Enter SEO Content Page Wise'

class Logo(models.Model):
	image = CloudinaryField()
	alt = models.CharField(max_length=500, default='', blank=True)
	name = models.CharField(max_length=255)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = 'Upload Website Logo'
		verbose_name_plural = 'Upload Website Logo'

class Banner(models.Model):
	image = CloudinaryField()
	alt = models.CharField(max_length=500, default='', blank=True)
	link = models.CharField(max_length=500, default='')

	class Meta:
		verbose_name = 'Upload Banner Images'
		verbose_name_plural = 'Upload Banner Images'

class Highlights(models.Model):
	image = CloudinaryField()
	alt = models.CharField(max_length = 500, default='')
	link = models.CharField(max_length=255, blank=True, null=True)
	text1 = models.CharField(max_length=255, blank=True, null=True)

	def __str__(self):
		return self.alt

	class Meta:
		verbose_name = 'Enter Cross Promotion Content'
		verbose_name_plural = 'Enter Cross Promotion Content'

class Home_Information(models.Model):
	imageone = CloudinaryField()
	imagetwo = CloudinaryField()
	imagethree = CloudinaryField()
	alt = models.CharField(max_length = 500, default='', blank=True)
	hedding = models.CharField(max_length=255)
	information = models.TextField()
	Kannada_text = models.TextField(default='')

	def __str__(self):
		return self.hedding

	class Meta:
		verbose_name = 'Enter Website Introduction'
		verbose_name_plural = 'Enter Website Introduction'

class Brands(models.Model):
	image = CloudinaryField()
	alt = models.CharField(max_length=255, default='', blank=True)

	def __str__(self):
		return self.alt

	class Meta:
		verbose_name = 'Home & About Us: Upload Collaboration Images'
		verbose_name_plural = 'Home & About Us: Upload Collaboration Images'

class Credentials(models.Model):
	CATEGORY = (('awards','Awards'),
                ('media coverages','Media Coverages'),
                ('approvals and licenses','Approvals and Licenses'))
	image = CloudinaryField()
	alt = models.CharField(max_length=255, default='', blank=True)
	title = models.CharField(max_length=255,null=True)
	type_of_image = models.CharField(max_length=255,choices=CATEGORY,null=True)

	class Meta:
		verbose_name = 'Upload Credential Images'
		verbose_name_plural = 'Upload Credential Images'

class Blogs(models.Model):
	image = CloudinaryField()
	alt = models.CharField(max_length=500, default='', blank=True)
	blog_heading = models.CharField(max_length=255,default='')
	blog_description = models.TextField(default='')
	date = models.DateTimeField(auto_now=True)
	embed_url = models.TextField(default='')
	video_heading = models.CharField(max_length=255,default='')
	video_description = models.TextField(default='')

	class Meta:
		verbose_name = 'Post Blogs'
		verbose_name_plural = 'Post Blogs'

class KCenter(models.Model):
    title = models.CharField(max_length=500, null=True)
    image = CloudinaryField(null=True, blank=True)
    alt = models.CharField(max_length=500, default='', blank=True)
    text1 = models.CharField(max_length=1000, null=True, blank=True)
    text2 = models.CharField(max_length=1000, null=True, blank=True)
    text3 = models.CharField(max_length=1000, null=True, blank=True)
    text4 = models.CharField(max_length=1000, null=True, blank=True)
    text5 = models.CharField(max_length=1000, null=True, blank=True)
    text6 = models.CharField(max_length=1000, null=True, blank=True)
    text7 = models.CharField(max_length=1000, null=True, blank=True)
    text8 = models.CharField(max_length=1000, null=True, blank=True)
    text9 = models.CharField(max_length=1000, null=True, blank=True)
    text10 = models.CharField(max_length=1000, null=True, blank=True)

    def __str__(self):
        return self.title

    class Meta:
        verbose_name = 'Enter KCenter Details'
        verbose_name_plural = 'Enter KCenter Details'
    
class KCenterTopic(models.Model):  # Renamed to follow proper naming convention
    ktopic = models.CharField(max_length=200)
    ktopic_slug = models.SlugField(unique=True, blank=True, null=True)
    ktopicimg = CloudinaryField()
    alt = models.CharField(max_length=110, null=True, blank=True)
    ktopicintro = models.TextField(default='')
    text1 = models.CharField(max_length=1000, null=True, blank=True)
    text2 = models.CharField(max_length=1000, null=True, blank=True)
    text3 = models.CharField(max_length=1000, null=True, blank=True)
    text4 = models.CharField(max_length=1000, null=True, blank=True)
    text5 = models.CharField(max_length=1000, null=True, blank=True)
    text6 = models.CharField(max_length=1000, null=True, blank=True)
    text7 = models.CharField(max_length=1000, null=True, blank=True)
    text8 = models.CharField(max_length=1000, null=True, blank=True)
    ktopicconclusion = models.CharField(max_length=1000)

    def __str__(self):
        return f'{self.ktopic}'

    class Meta:
        verbose_name = 'Enter KCenter Category-Specific Topic'
        verbose_name_plural = 'Enter KCenter Category-Specific Topic'

class Product(models.Model):
	CHOICES = (('Terrace Gardening','Terrace Gardening'),('Irrigation Solutions', 'Irrigation Solutions'))
	category = models.CharField(max_length=200,null=True,choices=CHOICES,blank=True)
	meta_title = models.CharField(max_length=500,null=True,blank=True)
	meta_description = models.TextField(null=True, blank=True)
	keywords = models.TextField(null=True, blank=True)
	backlinks = models.TextField(null=True, blank=True)
	order_no = models.IntegerField(null=True,blank=True)
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, blank=True, null=True)
	image = CloudinaryField()
	alt = models.CharField(max_length=500, default='', blank=True)
	pinfo = models.TextField(null=True,blank=True)
	Highlight_image1 = CloudinaryField(null=True,blank=True)	
	text1 = models.CharField(max_length=255, null=True,blank=True)
	Highlight_image2 = CloudinaryField(null=True,blank=True)
	text2 = models.CharField(max_length=255, null=True,blank=True)
	Highlight_image3 = CloudinaryField(null=True,blank=True)
	text3 = models.CharField(max_length=255, null=True,blank=True)
	date = models.DateTimeField(auto_now=True)
	background_gif = models.CharField(max_length=2000, default='', null=True, blank=True)
	exclusive_img = CloudinaryField(default='',null=True,blank=True)
	exclusive_img_alt = models.CharField(max_length=500, null=True,blank=True)
	exclusive_highlight_text = models.CharField(max_length=500, default='',null=True,blank=True)

	class Meta:
		ordering = ['order_no']
		verbose_name = 'Enter Product Categories Data'
		verbose_name_plural = 'Enter Product Categories Data'	

	def __str__(self):
		return self.name

class SubProduct(models.Model):
	product = models.ForeignKey(Product, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)	
	slug = models.SlugField(unique=True, blank=True, null=True)
	order_no = models.IntegerField(null=True,blank=True)	
	spimage = CloudinaryField()
	alt = models.CharField(max_length=500, default='', blank=True)
	sales_price = models.DecimalField(max_digits=10, decimal_places=2)
	mrp = models.DecimalField(max_digits=10, decimal_places=2)
	spinfo = models.TextField(null=True,blank=True)
	quantity = models.CharField(max_length=255,null=True)
	description = models.TextField(null=True,blank=True)
	rateing = models.DecimalField(max_digits=10, decimal_places=0, null=True,blank=True)
	Key_1 = models.CharField(max_length=255, null=True, blank=True)
	Value_1 = models.CharField(max_length=255, null=True, blank=True)
	Key_2 = models.CharField(max_length=255, null=True, blank=True)
	Value_2 = models.CharField(max_length=255, null=True, blank=True)
	Key_3 = models.CharField(max_length=255, null=True, blank=True)
	Value_3 = models.CharField(max_length=255, null=True, blank=True)
	Key_4 = models.CharField(max_length=255, null=True, blank=True)
	Value_4 = models.CharField(max_length=255, null=True, blank=True)
	Key_5 = models.CharField(max_length=255, null=True, blank=True)
	Value_5 = models.CharField(max_length=255, null=True, blank=True)
	Key_6 = models.CharField(max_length=255, null=True, blank=True)
	Value_6 = models.CharField(max_length=255, null=True, blank=True)
	Key_7 = models.CharField(max_length=255, null=True, blank=True)
	Value_7 = models.CharField(max_length=255, null=True, blank=True)
	Key_8 = models.CharField(max_length=255, null=True, blank=True)
	Value_8 = models.CharField(max_length=255, null=True, blank=True)
	Key_9 = models.CharField(max_length=255, null=True, blank=True)
	Value_9 = models.CharField(max_length=255, null=True, blank=True)
	Key_10 = models.CharField(max_length=255, null=True, blank=True)
	Value_10 = models.CharField(max_length=255, null=True, blank=True)
	Key_11 = models.CharField(max_length=255, null=True, blank=True)
	Value_11 = models.CharField(max_length=255, null=True, blank=True)
	Key_12 = models.CharField(max_length=255, null=True, blank=True)
	Value_12 = models.CharField(max_length=255, null=True, blank=True)
	Key_13 = models.CharField(max_length=255, null=True, blank=True)
	Value_13 = models.CharField(max_length=255, null=True, blank=True)
	Key_14 = models.CharField(max_length=255, null=True, blank=True)
	Value_14 = models.CharField(max_length=255, null=True, blank=True)
	Key_15 = models.CharField(max_length=255, null=True, blank=True)
	Value_15 = models.CharField(max_length=255, null=True, blank=True)

	def total(self):
		if self.sales_price > 0:
			return int(abs(100 - ((self.mrp / self.sales_price) * 100)))
		else:
			return 0

	def __str__(self):
		return self.name

	def save(self, *args, **kwargs):
		if not self.slug:
			self.slug = slugify(self.name)
		super(SubProduct, self).save(*args, **kwargs)

	class Meta:
		verbose_name = 'Enter Products Data'
		verbose_name_plural = 'Enter Products Data'
class Subproduct_External_links(models.Model):
    subproduct = models.ForeignKey(SubProduct, on_delete=models.CASCADE, related_name='subproduct_external_links')
    meta_title = models.CharField(max_length=100)
    meta_desc = models.TextField()
    keywords = models.TextField()
    external_links = models.TextField()

    class Meta:
        verbose_name = 'Enter Products SEO Contents'
        verbose_name_plural = 'Enter Products SEO Contents'
class KitComponent(models.Model):
    kit = models.ForeignKey(SubProduct, on_delete=models.CASCADE)
    component_name = models.CharField(max_length=500)
    component_image = CloudinaryField()
    component_sales_price = models.DecimalField(max_digits=10, decimal_places=2)
    component_mrp = models.DecimalField(max_digits=10, decimal_places=2)
    component_quantity = models.PositiveIntegerField(default=1)  # Changed to Integer
    is_available = models.BooleanField(default=True)  # Added availability flag

    @property
    def discount_percentage(self):
        return int(100 - ((self.component_sales_price / self.component_mrp) * 100))

    def __str__(self):
        return f"{self.component_name} (${self.component_sales_price})"

    class Meta:
        verbose_name = "Flexi Kit Component"
        verbose_name_plural = "Flexi Kit Components"

class KitComponentSelected(models.Model):
    kit = models.ForeignKey(SubProduct, on_delete=models.CASCADE)
    selected_component = models.ForeignKey(KitComponent, on_delete=models.CASCADE)  # Changed to ForeignKey
    quantity = models.PositiveIntegerField(default=1)  # Changed to Integer
    customer_name = models.CharField(max_length=500, default='')
    phone_no = models.CharField(max_length=10, default='')
    email_id = models.EmailField(default='')
    address = models.TextField(default='')
    total_amount = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)  # Changed to Decimal
    discount_price = models.DecimalField(max_digits=10, decimal_places=2, default=0.00)
    created_at = models.DateTimeField(auto_now_add=True)  # Added for tracking

    def save(self, *args, **kwargs):
        # Auto-calculate prices
        self.total_amount = self.selected_component.component_sales_price * self.quantity
        self.discount_price = (
            self.selected_component.component_mrp - 
            self.selected_component.component_sales_price
        ) * self.quantity
        super().save(*args, **kwargs)

    def __str__(self):
        return f"{self.quantity}x {self.selected_component.component_name}"

    class Meta:
        verbose_name = "User Selected Kit Products"
        verbose_name_plural = "User Selected Kit Products"

class Review(models.Model):
	RATING_CHOICES = [
        (5, '★★★★★'),
        (4, '★★★★'),
        (3, '★★★'),
        (2, '★★'),
        (1, '★'), 
    ]
	name = models.CharField(max_length=500)
	whatsapp_no = models.CharField(max_length=10, default='')
	rating = models.IntegerField(choices=RATING_CHOICES)
	review = models.TextField(null=True, blank=True)
	r_image = CloudinaryField(blank=True, default='')
	product = models.CharField(max_length=500)
	is_approved = models.BooleanField(default=False)
	review_token =  models.CharField(editable=False, unique=True, max_length=10, default='')
	ip_address = models.CharField(max_length=500, default='')
	is_important = models.BooleanField(default=False)
	date=models.DateField(null=True, blank=True)
	
	class Meta:
		verbose_name = "Get User's Product Reviews"
		verbose_name_plural = "Get User's Product Reviews"

class ReviewResponse(models.Model):
	review = models.ForeignKey(Review, on_delete = models.CASCADE)
	response_text = models.TextField()

	def __str__(self):
		return self.review.review_token

	class Meta:
		verbose_name = "Admin Response to User's Reviews"
		verbose_name_plural = "Admin Response to User's Reviews"
    
class Comments(models.Model):
	video = models.ForeignKey(Blogs, on_delete=models.CASCADE, related_name='comments',null=True)
	name = models.CharField(max_length=255,null=True)
	comment = models.CharField(max_length=500,null=True)
	date = models.DateField(auto_now=True)

	class Meta:
		verbose_name = "Get Comments for Blogs"
		verbose_name_plural = "Get Comments for Blogs"

class Contacts(models.Model):
	name = models.CharField(max_length=255)
	number = models.CharField(max_length=10,null=True)
	place=models.CharField(max_length=255,default='')
	comments = models.TextField(null=True)
	date = models.DateTimeField(auto_now=True)
	is_seen=models.BooleanField(null=True)

	def __str__(self):
		return self.name

	class Meta:
		verbose_name = "Get User Messages"
		verbose_name_plural = "Get User Messages"

class ATSIntro(models.Model):
	title = models.CharField(max_length=500)
	description = models.TextField()

	class Meta:
		verbose_name = 'Enter ATM Introduction'
		verbose_name_plural = 'Enter ATM Introduction'

class ATSInfo(models.Model):
	category_name = models.CharField(max_length=500)
	category_slug = models.SlugField(unique=True, blank=True, null=True)
	category_image = CloudinaryField()
	category_text = models.TextField()

	def __str__(self):
		return self.category_name
	
	class Meta:
		verbose_name = 'Global Agritech & ATM: Enter Category Info'
		verbose_name_plural = 'Global Agritech & ATM: Enter Category Info'

class ATSContactInfo(models.Model):
	category = models.ForeignKey(ATSInfo, on_delete=models.CASCADE)
	contact_name = models.CharField(max_length=500)
	contact_phone = models.CharField(max_length=10)
	contact_email = models.EmailField()
	contact_company_name = models.CharField(max_length=500)
	contact_company_desc = models.TextField(default='')
	contact_company_logo = CloudinaryField(default='')
	contact_company_link = models.CharField(max_length=500, default='')

	def __str__(self):
		return f'{self.contact_name} - {self.category.category_name}'
	
	class Meta:
		verbose_name = 'Enter ATM Supplier Info'
		verbose_name_plural = 'Enter ATM Supplier Info'

class ATSContactProductInfo(models.Model):
	seller = models.ForeignKey(ATSContactInfo, on_delete=models.CASCADE)
	product_name = models.CharField(max_length=500, null=True, blank=True)
	product_desc = models.TextField(null=True, blank=True)
	product_price = models.FloatField(null=True, blank=True)

	def __str__(self):
		return f'{self.seller.category.category_name} - {self.seller.contact_company_name} - {self.product_name}'

	class Meta:
		verbose_name = 'Enter ATM Supplier Product Info'
		verbose_name_plural = 'Enter ATM Supplier Product Info'

class ATSContactProductImages(models.Model):
	seller = models.ForeignKey(ATSContactInfo, on_delete=models.CASCADE, default='')
	seller_product = models.ForeignKey(ATSContactProductInfo, on_delete=models.CASCADE)
	product_image = CloudinaryField(default='')

	def __str__(self):
		return f'{self.seller.contact_company_name} - {self.seller_product.product_name}'

	class Meta:
		verbose_name = 'Enter ATM Supplier Product Images'
		verbose_name_plural = 'Enter ATM Supplier Product Images'

class ATSSeller(models.Model):
	seller_name = models.CharField(max_length=500)
	seller_company = models.CharField(max_length=500)
	seller_address = models.TextField()
	seller_email_id = models.EmailField()
	seller_product_avail = models.BooleanField(default=False)
	seller_plan = models.TextField()

	class Meta:
		verbose_name = 'Get ATM Seller Enquiry & Feedback'
		verbose_name_plural = 'Get ATM Seller Enquiry & Feedback'

class ATSSellerProductImage(models.Model):
	seller = models.ForeignKey(ATSSeller, on_delete=models.CASCADE)
	seller_product_images = CloudinaryField()

class ATSRoadmap(models.Model):
	roadmap_title = models.CharField(max_length=500)
	ppt = CloudinaryField()
	alt = models.CharField(max_length=500, default='')

	class Meta:
		verbose_name = 'ATM: Enter Roadmap Details'
		verbose_name_plural = 'ATM: Enter Roadmap Details'

class FeaturedListing(models.Model):
	featured_img = CloudinaryField()
	featured_alt = models.CharField(max_length=500)
	
	class Meta:
		verbose_name = 'Upload Featured Listing Images'
		verbose_name_plural = 'Upload Featured Listing Images'

class Newone(models.Model):
	course = (
		('python','python'),
		('sql','sql'),
		('django','django')
		   )
	name = models.CharField(max_length=20,blank=False,null=False)
	number = models.IntegerField(blank=False,null=False)
	place = models.CharField(max_length=30,blank=True,null=True)
	message = models.CharField(max_length=40,null=True,blank=True)
	email = models.EmailField(max_length=50,blank=False,null=False)
	date = models.DateField(auto_now=True)
	course = models.CharField(max_length=20,choices=course,default='python')

	def __str__(self):
		return self.name
	
	def clean(self):
		if self.number < 18:
			raise ValidationError({'number':'number must be 18 above............... '})
		
		if not self.name.startswith('A'):
			raise ValidationError({'name':'Name should start with A not with other character !! '})
	
	class Meta:
		verbose_name = 'New data'
		verbose_name_plural = 'New data'

class sess(models.Model):
	name = models.CharField(max_length=30,null=True,blank=True)
	
	def __str__(self):
		return self.name
	class Meta:
		verbose_name = 'session_data'
		verbose_name_plural ='session_data'



class Main_category(models.Model):
	CHOICES = (('Terrace Gardening','Terrace Gardening'),)
	category = models.CharField(max_length=200,null=True,choices=CHOICES,blank=True)
	name = models.CharField(max_length=255)
	order_no = models.IntegerField(null=True,blank=True)
	
	class Meta:
		ordering = ['order_no']
		verbose_name = 'Enter_Main_category'
		verbose_name_plural = 'Enter_Main_category'	

	def __str__(self):
		return self.name

class sub_cat(models.Model):
	cat = models.ForeignKey(Main_category,on_delete=models.CASCADE)
	name = models.CharField(max_length=100)
	order_no = models.IntegerField(null=True,blank=True)
	meta_title = models.CharField(max_length=500,null=True,blank=True)
	meta_description = models.TextField(null=True, blank=True)
	keywords = models.TextField(null=True, blank=True)
	backlinks = models.TextField(null=True, blank=True)
	slug = models.SlugField(unique=True, blank=True, null=True)
	image = models.ImageField(max_length=100,null=True)
	alt = models.CharField(max_length=500, default='', blank=True)
	pinfo = models.TextField(null=True,blank=True)
	Highlight_image1 = models.ImageField(max_length=100,null=True)
	text1 = models.CharField(max_length=255, null=True,blank=True)
	Highlight_image2 = models.ImageField(max_length=100,null=True)
	text2 = models.CharField(max_length=255, null=True,blank=True)
	Highlight_image3 = models.ImageField(max_length=100,null=True)
	text3 = models.CharField(max_length=255, null=True,blank=True)
	date = models.DateTimeField(auto_now=True)
	background_gif = models.CharField(max_length=2000, default='', null=True, blank=True)
	exclusive_img = models.ImageField(max_length=100,null=True)
	exclusive_img_alt = models.CharField(max_length=500, null=True,blank=True)
	exclusive_highlight_text = models.CharField(max_length=500, default='',null=True,blank=True)

	def __str__(self):
		return self.name
	
	class Meta:
		ordering = ['order_no']
		verbose_name ="Enter_Sub_category"
		verbose_name_plural = "Enter_Sub_category"

class Product1(models.Model):
	product = models.ForeignKey(sub_cat, on_delete=models.CASCADE)
	name = models.CharField(max_length=255)
	slug = models.SlugField(unique=True, blank=True, null=True)
	order_no = models.IntegerField(null=True,blank=True)
	spimage = models.ImageField(max_length=100,null=True)
	alt = models.CharField(max_length=500, default='', blank=True)
	sales_price = models.DecimalField(max_digits=10, decimal_places=2)
	mrp = models.DecimalField(max_digits=10, decimal_places=2)
	spinfo = models.TextField(null=True,blank=True)
	quantity = models.CharField(max_length=255,null=True)
	description = models.TextField(null=True,blank=True)
	rateing = models.DecimalField(max_digits=10, decimal_places=0, null=True,blank=True)
	Key_1 = models.CharField(max_length=255, null=True, blank=True)
	Value_1 = models.CharField(max_length=255, null=True, blank=True)
	Key_2 = models.CharField(max_length=255, null=True, blank=True)
	Value_2 = models.CharField(max_length=255, null=True, blank=True)
	Key_3 = models.CharField(max_length=255, null=True, blank=True)
	Value_3 = models.CharField(max_length=255, null=True, blank=True)
	Key_4 = models.CharField(max_length=255, null=True, blank=True)
	Value_4 = models.CharField(max_length=255, null=True, blank=True)
	Key_5 = models.CharField(max_length=255, null=True, blank=True)
	Value_5 = models.CharField(max_length=255, null=True, blank=True)
	Key_6 = models.CharField(max_length=255, null=True, blank=True)
	Value_6 = models.CharField(max_length=255, null=True, blank=True)
	Key_7 = models.CharField(max_length=255, null=True, blank=True)
	Value_7 = models.CharField(max_length=255, null=True, blank=True)
	Key_8 = models.CharField(max_length=255, null=True, blank=True)
	Value_8 = models.CharField(max_length=255, null=True, blank=True)
	Key_9 = models.CharField(max_length=255, null=True, blank=True)
	Value_9 = models.CharField(max_length=255, null=True, blank=True)
	Key_10 = models.CharField(max_length=255, null=True, blank=True)
	Value_10 = models.CharField(max_length=255, null=True, blank=True)
	Key_11 = models.CharField(max_length=255, null=True, blank=True)
	Value_11 = models.CharField(max_length=255, null=True, blank=True)
	Key_12 = models.CharField(max_length=255, null=True, blank=True)
	Value_12 = models.CharField(max_length=255, null=True, blank=True)
	Key_13 = models.CharField(max_length=255, null=True, blank=True)
	Value_13 = models.CharField(max_length=255, null=True, blank=True)
	Key_14 = models.CharField(max_length=255, null=True, blank=True)
	Value_14 = models.CharField(max_length=255, null=True, blank=True)
	Key_15 = models.CharField(max_length=255, null=True, blank=True)
	Value_15 = models.CharField(max_length=255, null=True, blank=True)

	def __str__(self):
		return self.name
	
	class Meta:
		verbose_name = "Enter_Product data"
		verbose_name_plural = "Enter_Product data"


class Subproduct_External_links1(models.Model):
	subproduct = models.ForeignKey(Product1,on_delete=models.CASCADE,related_name='subproduct_external_links')
	meta_title = models.CharField(max_length=100)
	meta_desc = models.TextField()
	keywords = models.TextField()
	external_links = models.TextField()

	class Meta:
		verbose_name = 'Enter Products SEO Contents---1'
		verbose_name_plural = 'Enter Products SEO Contents---1'

class KitComponent1(models.Model):
	kit = models.ForeignKey(Product1, on_delete=models.CASCADE)
	subproduct = models.ForeignKey(SubProduct, on_delete=models.CASCADE,null=True,blank=True)  
	component_name = models.CharField(max_length=500)
	component_image = CloudinaryField()
	component_sales_price = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	component_mrp = models.DecimalField(max_digits=10, decimal_places=2, null=True, blank=True)
	component_quantity = models.CharField(max_length=255,null=True, blank=True)

	class Meta:
		verbose_name = "Enter Flexi Kits Product details---1"
		verbose_name_plural = "Enter Flexi Kits Product details---1"   

class KitComponentSelected1(models.Model):
	kit = models.ForeignKey(Product1, on_delete=models.CASCADE)
	selected_component = models.CharField(max_length=500)
	quantity = models.CharField(max_length=255, default='')
	customer_name = models.CharField(max_length=500, default='')
	phone_no = models.CharField(max_length=10, default='')
	email_id = models.EmailField(default='')
	address = models.TextField(default='')
	total_amount = models.CharField(max_length=10, default='0.00')
	discount_price = models.CharField(max_length=10, default='0.00')

	class Meta:
		verbose_name = "Get User Selected Kit Products---1"
		verbose_name_plural = "Get User Selected Kit Products---1"