# Generated by Django 3.2.9 on 2022-05-27 18:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0004_remove_profile_price'),
    ]

    operations = [
        migrations.CreateModel(
            name='About',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('about', models.TextField()),
                ('conclusion', models.CharField(max_length=255)),
            ],
        ),
    ]
