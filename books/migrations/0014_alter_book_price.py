# Generated by Django 4.1.6 on 2023-02-22 19:50

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0013_book_is_archived_alter_book_authors_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='book',
            name='price',
            field=models.FloatField(null=True),
        ),
    ]
