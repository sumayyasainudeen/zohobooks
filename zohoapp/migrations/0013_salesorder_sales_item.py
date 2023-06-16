# Generated by Django 4.1.7 on 2023-05-30 16:27

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('zohoapp', '0012_account_expense'),
    ]

    operations = [
        migrations.CreateModel(
            name='SalesOrder',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('sales_no', models.CharField(blank=True, max_length=255, null=True)),
                ('reference', models.CharField(blank=True, max_length=255, null=True)),
                ('sales_date', models.DateField(blank=True, max_length=255, null=True)),
                ('ship_date', models.DateField(blank=True, max_length=255, null=True)),
                ('d_method', models.TextField(blank=True, null=True)),
                ('s_person', models.TextField(blank=True, null=True)),
                ('igst', models.TextField(blank=True, max_length=255, null=True)),
                ('cgst', models.TextField(blank=True, max_length=255, null=True)),
                ('sgst', models.TextField(blank=True, max_length=255, null=True)),
                ('t_tax', models.FloatField(blank=True, null=True)),
                ('subtotal', models.FloatField(blank=True, null=True)),
                ('grandtotal', models.FloatField(blank=True, null=True)),
                ('cxnote', models.TextField(blank=True, max_length=255, null=True)),
                ('file', models.ImageField(blank=True, null=True, upload_to='documents')),
                ('terms_condition', models.TextField(blank=True, max_length=255, null=True)),
                ('status', models.TextField(blank=True, max_length=255, null=True)),
                ('customer', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.customer')),
                ('terms', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.payment_terms')),
            ],
        ),
        migrations.CreateModel(
            name='sales_item',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('product', models.TextField(blank=True, max_length=255, null=True)),
                ('quantity', models.IntegerField(blank=True, null=True)),
                ('hsn', models.TextField(blank=True, max_length=255, null=True)),
                ('tax', models.IntegerField(blank=True, null=True)),
                ('total', models.FloatField(blank=True, null=True)),
                ('desc', models.TextField(blank=True, max_length=255, null=True)),
                ('rate', models.TextField(blank=True, max_length=255, null=True)),
                ('sale', models.ForeignKey(blank=True, null=True, on_delete=django.db.models.deletion.CASCADE, to='zohoapp.salesorder')),
            ],
        ),
    ]
