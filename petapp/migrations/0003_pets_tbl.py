# Generated by Django 3.2.7 on 2021-10-01 07:19

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('petapp', '0002_auto_20211001_1154'),
    ]

    operations = [
        migrations.CreateModel(
            name='pets_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('category', models.CharField(default='', max_length=50)),
                ('name', models.CharField(default='', max_length=50)),
                ('gender', models.CharField(default='', max_length=50)),
                ('age', models.CharField(default='', max_length=50)),
                ('colour', models.CharField(default='', max_length=50)),
                ('description', models.CharField(default='', max_length=50)),
                ('price', models.CharField(default='', max_length=50)),
                ('file', models.FileField(upload_to='')),
            ],
        ),
    ]
