# Generated by Django 4.1.5 on 2023-01-19 23:50

import ckeditor.fields
from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('recipes', '0007_alter_recipe_instructions'),
    ]

    operations = [
        migrations.AlterField(
            model_name='recipe',
            name='instructions',
            field=ckeditor.fields.RichTextField(),
        ),
    ]
