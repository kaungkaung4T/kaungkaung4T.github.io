# Generated by Django 3.2.9 on 2022-06-08 21:55

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0022_auto_20220608_1437'),
    ]

    operations = [
        migrations.AddField(
            model_name='about',
            name='github',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='leet',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
        migrations.AddField(
            model_name='about',
            name='linkedin',
            field=models.CharField(blank=True, max_length=255, null=True),
        ),
    ]
