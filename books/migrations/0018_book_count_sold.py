# Generated by Django 4.1.6 on 2023-03-10 19:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('books', '0017_author_telegram_account_id'),
    ]

    operations = [
        migrations.AddField(
            model_name='book',
            name='count_sold',
            field=models.IntegerField(default=0),
        ),
    ]
