# Generated by Django 4.0 on 2022-01-11 05:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('user_order', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='order',
            name='order_date',
            field=models.DateTimeField(auto_now_add=True, verbose_name='date ordered'),
        ),
    ]
