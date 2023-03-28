# Generated by Django 3.2.16 on 2023-03-28 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('parent', models.CharField(max_length=20, null=True)),
                ('title', models.CharField(max_length=20, null=True)),
                ('meta_title', models.CharField(max_length=20, null=True)),
                ('slug', models.SlugField(default='', null=True)),
                ('content', models.TextField(max_length=50, null=True)),
            ],
        ),
        migrations.CreateModel(
            name='ProductCatergory',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='category.category')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
