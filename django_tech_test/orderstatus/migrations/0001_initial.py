# Generated by Django 4.1.2 on 2022-10-19 01:59

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Order',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('order_number', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('item_name', models.CharField(max_length=50)),
                ('status', models.CharField(choices=[('SHIPPED', 'SHIPPED'), ('PENDING', 'PENDING'), ('CANCELLED', 'CANCELLED')], max_length=20)),
                ('order_number', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='order_details', to='orderstatus.order')),
            ],
        ),
    ]
