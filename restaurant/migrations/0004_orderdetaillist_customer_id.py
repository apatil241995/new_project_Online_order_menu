# Generated by Django 3.0.3 on 2021-12-22 08:34

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('restaurant', '0003_orderdetaillist'),
    ]

    operations = [
        migrations.AddField(
            model_name='orderdetaillist',
            name='customer_id',
            field=models.IntegerField(null=True),
        ),
    ]
