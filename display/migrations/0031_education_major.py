# Generated by Django 3.2.9 on 2022-08-28 16:37

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0030_education_tran'),
    ]

    operations = [
        migrations.AddField(
            model_name='education',
            name='major',
            field=models.CharField(blank=True, max_length=225, null=True),
        ),
    ]
