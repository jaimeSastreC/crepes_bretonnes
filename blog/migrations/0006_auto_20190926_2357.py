# Generated by Django 2.2.2 on 2019-09-26 21:57

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0005_auto_20190926_0012'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='comment',
            options={'verbose_name': "Commentaire d'article"},
        ),
    ]
