# Generated by Django 4.2.7 on 2023-11-27 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Content',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('contact', models.CharField(max_length=100)),
                ('listing', models.TextField()),
                ('image', models.ImageField(default='default.png', null=True, upload_to='')),
            ],
        ),
    ]
