# Generated by Django 3.2.9 on 2022-06-08 21:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0021_auto_20220608_1427'),
    ]

    operations = [
        migrations.AlterField(
            model_name='about',
            name='dob',
            field=models.CharField(default=1, max_length=255),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name='about',
            name='phone',
            field=models.CharField(max_length=255),
        ),
    ]
