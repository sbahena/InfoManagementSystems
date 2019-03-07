# Generated by Django 2.1.6 on 2019-03-07 12:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('labbyims', '0008_merge_20190307_1303'),
    ]

    operations = [
        migrations.AddField(
            model_name='product_unit',
            name='in_house_no',
            field=models.CharField(blank=True, max_length=255, verbose_name='In House ID'),
        ),
        migrations.AlterField(
            model_name='reserve',
            name='date_res',
            field=models.DateField(verbose_name='reservation date'),
        ),
    ]