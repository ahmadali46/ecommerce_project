# Generated by Django 3.2 on 2022-06-02 11:55

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import emp.models


class Migration(migrations.Migration):

    dependencies = [
        ('emp', '0002_alter_product_user'),
    ]

    operations = [
        migrations.AlterField(
            model_name='product',
            name='user',
            field=models.ForeignKey(default=emp.models.MyUser, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
    ]
