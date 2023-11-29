# Generated by Django 4.2.7 on 2023-11-29 15:01

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('cart', '0001_initial'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('product', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='carts',
            name='created_by',
            field=models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='cart_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cart.carts', verbose_name='cart'),
        ),
        migrations.AddField(
            model_name='cartitems',
            name='product_id',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='product.products', to_field='title', verbose_name='product'),
        ),
        migrations.AlterUniqueTogether(
            name='carts',
            unique_together={('id', 'created_by')},
        ),
        migrations.AlterUniqueTogether(
            name='cartitems',
            unique_together={('cart_id', 'product_id')},
        ),
    ]
