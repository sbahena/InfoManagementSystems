# Generated by Django 2.1.5 on 2019-02-13 10:11

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labbyims', '0004_auto_20190213_1108'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='product_unit',
            name='m_units',
        ),
        migrations.AddField(
            model_name='product_unit',
            name='measure_u',
            field=models.CharField(max_length=12, null=True),
        ),
    ]
