# Generated by Django 4.1.7 on 2023-05-23 05:01

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0006_auto_20230518_0635'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample_table',
            name='cust_rate',
            field=models.FloatField(),
        ),
    ]