from django import forms
from .models import Comments,Newone ,KitComponentSelected1,Review, ATSSeller, ATSSellerProductImage, Contacts, kcentercategories, kcentertopic
from django.forms import inlineformset_factory
from django.utils.text import slugify
from django.core.exceptions import ValidationError
from django.utils.safestring import mark_safe
                                                                                            

class ContactForm(forms.ModelForm):
	class Meta:
		model=Contacts
		fields = '__all__'
		exclude = ['date','is_seen']
		labels={
			"comments":"Message"
		}
		widgets = {
			'number':forms.NumberInput(attrs={'type':'number'})
		}

class CommentForm(forms.ModelForm):
    class Meta:
        model = Comments
        fields = ['name','comment']
        widgets = {
            'name': forms.TextInput(attrs={'placeholder': 'Your Name'}),
            'comment': forms.Textarea(attrs={'placeholder': 'Add Comment'}),
        }

class ReviewForm(forms.ModelForm):
	class Meta:
		model = Review
		fields = ['name','whatsapp_no','rating','review','r_image']
		widgets = {
        	'name': forms.TextInput(attrs={'placeholder': 'Enter your Full Name'}),
        	'whatsapp_no': forms.TextInput(attrs={'placeholder': "Enter Your 10-digit Whatsapp Number"}),
        	'review': forms.Textarea(attrs={'placeholder': 'Enter your Feedback about the product'}),
        }
		labels = {
        	'whatsapp_no':"Whatsapp Number",
        	'r_image':"Share your Product Experience (Photo: 2MB max)"
        }

	def getIP(self, request):
		x_forwarded_for = request.META.get('HTTP_X_FORWARDED_FOR')
		if x_forwarded_for:
			ip = x_forwarded_for.split(',')[0]
		else:
			ip = request.META.get('REMOTE_ADDR')
		return ip

	def __init__(self, request, *args, **kwargs):
		ip = self.getIP(request)
		super(ReviewForm, self).__init__(*args, **kwargs)
		existing_reviews = Review.objects.filter(ip_address=ip)
		if existing_reviews.exists():
			first_review = existing_reviews.first()
			self.fields['name'].initial = first_review.name
			self.fields['whatsapp_no'].initial = first_review.whatsapp_no
		self.fields['review'].required = False

class KitComponentSelectedForm(forms.ModelForm):
    class Meta:
        
        model = KitComponentSelected1
        fields = ['customer_name','phone_no','email_id','address']

    def clean_phone_no(self):
        phone_no = self.cleaned_data.get('phone_no')
        if len(str(phone_no)) != 10:
            raise forms.ValidationError(mark_safe("<span style='color:red; font-weight: bold;'>Phone number must be of 10 digits</span>"))
        return phone_no

class CustomPlaceholderTextInput(forms.TextInput):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['style'] = 'font-size: 13px;'

class CustomPlaceholderTextarea(forms.Textarea):
    def __init__(self, *args, **kwargs):
        super().__init__(*args, **kwargs)
        self.attrs['style'] = 'font-size: 13px;'

class ATSSellerForm(forms.ModelForm):
    class Meta:
        model = ATSSeller
        fields = '__all__'
        widgets = {
            'seller_name': CustomPlaceholderTextInput(attrs={'placeholder': 'Enter your Full Name'}),
            'seller_company': CustomPlaceholderTextInput(attrs={'placeholder': "Enter Your 10-digit Whatsapp No."}),
            'seller_email_id': CustomPlaceholderTextInput(attrs={'placeholder': "Enter your Email ID"}),
            'seller_address': CustomPlaceholderTextarea(attrs={'placeholder': "Enter Your Address"}),
            'seller_plan': CustomPlaceholderTextarea(attrs={'placeholder': "Brief about the product planning to sell" }),
        }
        labels = {
            'seller_product_avail':'Products currently available or not in the market? (Tick if yes)',
        }

ATSSellerProductImageFormSet = inlineformset_factory(
    ATSSeller,
    ATSSellerProductImage,
    fields=['seller_product_images'],
    extra=10,
    can_delete=True,
)

class CategoryForm(forms.ModelForm):
    class Meta:
        model = kcentercategories
        fields = ['categories']
        widgets = {
            'categories':forms.Select(attrs={'labels':'Select Category'})
        }
    
    def __init__(self, *args, **kwargs):
        super().__init__(*args,**kwargs)
        category_choices= [(slugify("Select Category"),"Select Category")]
        category_choices += [(category.categories, category.categories) for category in kcentercategories.objects.all()]
        if category_choices:
            self.fields['categories'].widget.choices = category_choices
            
class TopicForm(forms.ModelForm):
    class Meta:
        model = kcentertopic
        fields = ['ktopic']
        widgets = {
            'ktopic':forms.Select(attrs={'labels':'Select Topic'})
        }
        
    def __init__(self, request, *args, **kwargs):
        super().__init__(*args,**kwargs)
        url = request.build_absolute_uri(request.path)
        selected_category = url.split('/')[4]
        topic_choices = [(slugify('Select Topic'), 'Select Topic')]
        topic_choices += [(topic.ktopic_slug, topic.ktopic) for topic in kcentertopic.objects.filter(category__categoriesslug=selected_category)]
        if topic_choices:
            self.fields['ktopic'].widget.choices = topic_choices
class Newform(forms.ModelForm):
     class Meta:
          model = Newone
          fields = '__all__'
          labels = {
               'email': "Email Id",
               'number':'Number'
          }
          widgets = {
               'email': forms.EmailInput(attrs={'placeholder': 'Enter Your Email'}),
               'number': forms.NumberInput(attrs={'placeholder': 'Enter Your Number'})
          }
           