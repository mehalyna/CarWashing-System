# Generated by Django 3.2.14 on 2022-08-18 17:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('CW_places', '0002_auto_20220807_1523'),
    ]

    operations = [
        migrations.AlterField(
            model_name='cwplaces',
            name='carwash_place',
            field=models.IntegerField(primary_key=True, serialize=False),
        ),
    ]
