# Generated by Django 4.2.5 on 2023-10-14 08:47

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('product_api', '0002_remove_product_updated_alter_product_created_and_more'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='updated',
            field=models.DateTimeField(auto_now=True),
        ),
        migrations.AlterField(
            model_name='product',
            name='created',
            field=models.DateTimeField(auto_now_add=True),
        ),
    ]
