# Generated by Django 4.0 on 2022-01-17 07:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_order', '0002_alter_order_order_date'),
    ]

    operations = [
        migrations.AddField(
            model_name='order',
            name='price',
            field=models.IntegerField(default=0),
        ),
    ]