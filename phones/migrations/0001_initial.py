# Generated by Django 5.2.3 on 2025-06-20 07:56

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Phone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=50)),
                ('price', models.IntegerField()),
                ('image', models.CharField(max_length=1000)),
                ('release_date', models.DateField()),
                ('lte_exists', models.BooleanField(default=True)),
                ('slug', models.SlugField(max_length=1000, unique=True)),
            ],
        ),
    ]
