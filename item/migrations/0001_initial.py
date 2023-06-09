# Generated by Django 3.2.16 on 2023-03-28 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('order', '0001_initial'),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Brand',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=20, null=True)),
                ('summary', models.CharField(max_length=20, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('context', models.CharField(max_length=30)),
            ],
        ),
        migrations.CreateModel(
            name='Item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('supplier', models.CharField(max_length=10, null=True)),
                ('store_keeping_unit', models.CharField(max_length=20, null=True)),
                ('mrp', models.DecimalField(decimal_places=4, max_digits=4, null=True)),
                ('discount', models.DecimalField(decimal_places=4, max_digits=4, null=True)),
                ('price', models.DecimalField(decimal_places=4, max_digits=4, null=True)),
                ('quantity', models.SmallIntegerField()),
                ('sold', models.SmallIntegerField()),
                ('available', models.SmallIntegerField()),
                ('defective', models.SmallIntegerField()),
                ('created_by', models.SmallIntegerField()),
                ('updated_by', models.SmallIntegerField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('brand', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='item.brand')),
                ('order', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='order.order')),
                ('product', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.product')),
            ],
        ),
    ]
