# Generated by Django 3.2.9 on 2023-02-07 12:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0041_auto_20230207_1905'),
    ]

    operations = [
        migrations.AddField(
            model_name='work_project',
            name='image5',
            field=models.ImageField(blank=True, null=True, upload_to='work_project'),
        ),
        migrations.AddField(
            model_name='work_project',
            name='tech',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
