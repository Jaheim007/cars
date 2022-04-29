# Generated by Django 4.0.4 on 2022-04-29 10:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('carapp', '0002_alter_car_description'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='car',
            options={'verbose_name': 'Car', 'verbose_name_plural': 'Cars'},
        ),
        migrations.AddField(
            model_name='car',
            name='image_file',
            field=models.FileField(default=1, upload_to='cars'),
            preserve_default=False,
        ),
    ]