# Generated by Django 3.1.1 on 2020-09-16 05:22

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Portfolio',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('img', models.ImageField(blank=True, null=True, upload_to='')),
                ('title', models.CharField(max_length=20)),
                ('desc', models.CharField(max_length=10)),
            ],
        ),
    ]
