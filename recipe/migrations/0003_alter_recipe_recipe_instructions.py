# Generated by Django 4.1.6 on 2023-07-18 04:36

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('recipe', '0002_recipe_recipe_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='recipe_instructions',
            field=models.CharField(blank=True, max_length=1000, null=True),
        ),
    ]