# Generated by Django 3.2.9 on 2022-05-28 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0008_auto_20220527_2057'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('image', models.ImageField(upload_to='project_image')),
                ('description', models.TextField()),
            ],
        ),
    ]
