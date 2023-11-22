# Generated by Django 4.2.7 on 2023-11-22 16:21

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0002_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Carts',
            fields=[
                ('id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('status', models.CharField(choices=[('active', 'Active'), ('ordered', 'Ordered'), ('pending', 'Pending'), ('abandoned', 'Abandoned')], max_length=20, verbose_name='status')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='created_at')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='updated_at')),
                ('created_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'verbose_name': 'Cart',
                'verbose_name_plural': 'Carts',
            },
        ),
        migrations.CreateModel(
            name='CartItems',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(default=0.0)),
                ('quantity', models.IntegerField(default=0)),
                ('created_at', models.DateTimeField(auto_now=True, verbose_name='created_at')),
                ('cart_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.carts', verbose_name='cart_id')),
                ('product_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products', verbose_name='product_id')),
            ],
            options={
                'verbose_name': 'Cart Item',
                'verbose_name_plural': 'Cart Items',
            },
        ),
    ]
