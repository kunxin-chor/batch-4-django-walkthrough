# Generated by Django 2.2.4 on 2020-01-15 11:45

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Catalog', '0002_auto_20200113_1318'),
    ]

    operations = [
        migrations.CreateModel(
            name='Category',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
            ],
        ),
    ]