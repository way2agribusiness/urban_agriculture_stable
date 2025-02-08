from rest_framework import serializers
from .models import ATSInfo, ATSContactInfo, ATSIntro, ATSContactProductInfo, ATSSeller, ATSContactProductImages, Contacts, Product,FeaturedListing

class ProductSerializer(serializers.ModelSerializer):
    image = serializers.ImageField(use_url=True)
    exclusive_img = serializers.ImageField(use_url=True)
    class Meta:
        model = Product
        fields = '__all__'

class ATSIntroSerializer(serializers.ModelSerializer):
    class Meta:
        model = ATSIntro
        fields = '__all__'

class ATSSerializer(serializers.ModelSerializer):
    category_image = serializers.ImageField(use_url=True)
    class Meta:
        model = ATSInfo
        fields = '__all__'

class ContactsSerializer(serializers.ModelSerializer):
    class Meta:
        models = Contacts
        fields = '__all__'
    
class ATSContactSerializer(serializers.ModelSerializer):
    contact_company_logo = serializers.ImageField(use_url=True)
    class Meta:
        model = ATSContactInfo
        fields = '__all__'

    def to_representation(self, instance):
        data = super().to_representation(instance)
        if self.context['request'].method == 'POST':
            return data
        else:
            data['category'] = ATSSerializer(instance.category).data
            return data
    
class ATSContactProductSerializer(serializers.ModelSerializer):
    seller = ATSContactSerializer('seller')

    class Meta:
        model = ATSContactProductInfo
        fields = '__all__'
    
class ATSContactProductImagesSerializer(serializers.ModelSerializer):
    seller = ATSContactSerializer('seller')
    seller_product = ATSContactProductSerializer()
    product_image = serializers.ImageField(use_url=True)

    class Meta:
        model = ATSContactProductImages
        fields = '__all__'

class FeaturedListingSerializer(serializers.ModelSerializer):
    featured_img = serializers.ImageField(use_url=True)
    class Meta:
        model = FeaturedListing
        fields = '__all__'