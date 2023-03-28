# Generated by Django 3.2.16 on 2023-03-28 15:09

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('user', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(max_length=10, null=True)),
                ('status', models.CharField(max_length=20, null=True)),
                ('sub_total', models.IntegerField(null=True)),
                ('item_discount', models.DecimalField(decimal_places=4, max_digits=4, max_length=10, null=True)),
                ('tax', models.DecimalField(decimal_places=4, max_digits=4, max_length=10, null=True)),
                ('shipping', models.DecimalField(decimal_places=4, max_digits=4, max_length=10, null=True)),
                ('order_total', models.DecimalField(decimal_places=4, max_digits=4, max_length=10, null=True)),
                ('promo', models.CharField(max_length=30, null=True)),
                ('discount', models.DecimalField(decimal_places=4, max_digits=4, max_length=10, null=True)),
                ('grand_total', models.DecimalField(decimal_places=4, max_digits=4, max_length=10, null=True)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('updated_at', models.DateTimeField(auto_now=True)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='user.user')),
            ],
        ),
    ]
