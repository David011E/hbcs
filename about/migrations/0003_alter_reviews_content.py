# Generated by Django 4.2.9 on 2024-02-13 10:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('about', '0002_reviews_excerpt'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reviews',
            name='content',
            field=models.TextField(max_length=200),
        ),
    ]