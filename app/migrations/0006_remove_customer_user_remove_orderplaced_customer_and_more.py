# Generated by Django 5.1.4 on 2024-12-15 17:17

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('app', '0005_wishlist'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='customer',
            name='user',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='customer',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='payment',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='product',
        ),
        migrations.RemoveField(
            model_name='orderplaced',
            name='user',
        ),
        migrations.RemoveField(
            model_name='payment',
            name='user',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='product',
        ),
        migrations.RemoveField(
            model_name='wishlist',
            name='user',
        ),
        migrations.DeleteModel(
            name='Cart',
        ),
        migrations.DeleteModel(
            name='Customer',
        ),
        migrations.DeleteModel(
            name='OrderPlaced',
        ),
        migrations.DeleteModel(
            name='Payment',
        ),
        migrations.DeleteModel(
            name='Wishlist',
        ),
    ]
