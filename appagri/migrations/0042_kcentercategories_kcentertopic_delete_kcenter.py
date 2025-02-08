# Generated by Django 4.2 on 2024-06-24 12:56

import cloudinary.models
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('appagri', '0041_delete_webinfo_alter_atscontactinfo_options_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='kcentercategories',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('categories', models.CharField(max_length=200)),
                ('categoriesslug', models.SlugField(blank=True, null=True, unique=True)),
            ],
            options={
                'verbose_name': 'Enter KCenter Category',
                'verbose_name_plural': 'Enter KCenter Category',
            },
        ),
        migrations.CreateModel(
            name='kcentertopic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ktopic', models.CharField(max_length=200)),
                ('ktopic_slug', models.SlugField(blank=True, null=True, unique=True)),
                ('ktopicimg', cloudinary.models.CloudinaryField(max_length=255)),
                ('ktopictext', models.TextField()),
                ('ktopicintro', models.TextField(default='')),
                ('ktopicconclusion', models.CharField(max_length=1000)),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='appagri.kcentercategories')),
            ],
            options={
                'verbose_name': 'Enter KCenter Category-Specific Topic',
                'verbose_name_plural': 'Enter KCenter Category-Specific Topic',
            },
        ),
        migrations.DeleteModel(
            name='KCenter',
        ),
    ]
