# Generated by Django 3.2.16 on 2023-03-28 16:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('user', '0002_alter_user_role'),
    ]

    operations = [
        migrations.AlterField(
            model_name='user',
            name='role',
            field=models.ForeignKey(default=3, on_delete=django.db.models.deletion.CASCADE, to='user.role'),
        ),
    ]
