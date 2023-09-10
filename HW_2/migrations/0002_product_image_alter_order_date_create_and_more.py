# Generated by Django 4.2.4 on 2023-09-03 08:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('HW_2', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='product',
            name='image',
            field=models.ImageField(default=None, upload_to='product_media/'),
        ),
        migrations.AlterField(
            model_name='order',
            name='date_create',
            field=models.DateField(),
        ),
        migrations.AlterField(
            model_name='product',
            name='description',
            field=models.CharField(max_length=100),
        ),
    ]