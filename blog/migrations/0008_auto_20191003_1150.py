# Generated by Django 2.2.2 on 2019-10-03 09:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0007_contact'),
    ]

    operations = [
        migrations.AlterField(
            model_name='contact',
            name='photo',
            field=models.ImageField(upload_to='static/img/'),
        ),
    ]