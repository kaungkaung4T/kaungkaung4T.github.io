# Generated by Django 3.2.9 on 2023-02-03 16:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0032_about_work'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='work_url',
            field=models.URLField(blank=True, null=True),
        ),
    ]
