# Generated by Django 2.2.28 on 2023-06-22 21:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0002_recette_image'),
    ]

    operations = [
        migrations.CreateModel(
            name='Ingredient',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('ingredient', models.CharField(max_length=200)),
                ('checked', models.BooleanField(default=False)),
                ('recette', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='blog.Recette')),
            ],
        ),
    ]
