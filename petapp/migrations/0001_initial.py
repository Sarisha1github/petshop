# Generated by Django 3.2.7 on 2021-10-01 05:39

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='shop_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('shopname', models.CharField(default='', max_length=50)),
                ('address', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='user_tbl',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('username', models.CharField(default='', max_length=50)),
                ('email', models.CharField(default='', max_length=50)),
                ('password', models.CharField(default='', max_length=50)),
            ],
        ),
    ]
