# Generated by Django 3.2.9 on 2022-06-04 08:48

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('display', '0012_skill_api'),
    ]

    operations = [
        migrations.CreateModel(
            name='SchoolProject',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=225)),
                ('image', models.ImageField(upload_to='project_image')),
                ('uses', models.CharField(max_length=255)),
                ('description', models.TextField()),
            ],
        ),
    ]
