# Generated by Django 3.2.14 on 2022-08-18 17:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('CW_places', '0003_alter_cwplaces_carwash_place'),
    ]

    operations = [
        migrations.CreateModel(
            name='OrderDetail',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('price', models.FloatField(blank=True, null=True)),
                ('duration', models.IntegerField(blank=True, null=True)),
                ('start_time', models.TimeField(blank=True, null=True)),
                ('carwash_place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='CW_places.cwplaces')),
            ],
            options={
                'db_table': 'order_detail',
                'managed': True,
            },
        ),
    ]