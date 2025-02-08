# Generated by Django 4.2 on 2024-04-24 06:59

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0028_review_r_image_review_review_token_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='ATSContactInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact_name', models.CharField(max_length=500)),
                ('contact_phone', models.CharField(max_length=10)),
                ('contact_email', models.EmailField(max_length=254)),
                ('contact_company_name', models.CharField(max_length=500)),
                ('contact_company_desc', models.TextField(default='')),
            ],
            options={
                'verbose_name': 'z2. Enter ATM Supplier Info',
                'verbose_name_plural': 'z2. Enter ATM Supplier Info',
            },
        ),
        migrations.CreateModel(
            name='ATSInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category_name', models.CharField(max_length=500)),
                ('category_image', cloudinary.models.CloudinaryField(max_length=255)),
                ('category_text', models.TextField()),
            ],
            options={
                'verbose_name': 'z1. Enter ATM Category Info',
                'verbose_name_plural': 'z1. Enter ATM Category Info',
            },
        ),
        migrations.CreateModel(
            name='ATSIntro',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('description', models.TextField()),
            ],
            options={
                'verbose_name': 'z. Enter ATM Introduction',
                'verbose_name_plural': 'z. Enter ATM Introduction',
            },
        ),
        migrations.CreateModel(
            name='ATSSeller',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('seller_name', models.CharField(max_length=500)),
                ('seller_company', models.CharField(max_length=500)),
                ('seller_address', models.TextField()),
                ('seller_email_id', models.EmailField(max_length=254)),
                ('seller_product_avail', models.BooleanField(default=False)),
                ('seller_plan', models.TextField()),
                ('seller_product_images', cloudinary.models.CloudinaryField(default='', max_length=255)),
            ],
            options={
                'verbose_name': 'z4. Get ATM Seller Enquiry',
                'verbose_name_plural': 'z4. Get ATM Seller Enquiry',
            },
        ),
        migrations.CreateModel(
            name='ATSContactProductInfo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product_image', cloudinary.models.CloudinaryField(blank=True, max_length=255, null=True)),
                ('product_name', models.CharField(blank=True, max_length=500, null=True)),
                ('product_desc', models.TextField(blank=True, null=True)),
                ('product_price', models.FloatField(blank=True, null=True)),
                ('seller', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appagri.atscontactinfo')),
            ],
            options={
                'verbose_name': 'z3. Enter ATM Supplier Product Info',
                'verbose_name_plural': 'z3. Enter ATM Supplier Product Info',
            },
        ),
        migrations.AddField(
            model_name='atscontactinfo',
            name='category',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appagri.atsinfo'),
        ),
    ]
