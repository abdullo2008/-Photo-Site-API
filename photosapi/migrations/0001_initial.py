# Generated by Django 5.1.1 on 2024-09-07 11:49

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='PhotoModel',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=255)),
                ('photo', models.ImageField(upload_to='photos/')),
                ('caption', models.TextField(default='This is picture')),
                ('date_added', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
