# Generated by Django 2.2.2 on 2019-09-25 22:12

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_article_slug'),
    ]

    operations = [
        migrations.AlterModelOptions(
            name='categorie',
            options={'ordering': ['nom'], 'verbose_name': "Categorie d'Article"},
        ),
        migrations.AlterField(
            model_name='article',
            name='auteur',
            field=models.CharField(max_length=32),
        ),
        migrations.CreateModel(
            name='Comment',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contenu', models.TextField()),
                ('auteur', models.CharField(max_length=32)),
                ('article', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Article')),
            ],
        ),
    ]
