# Generated by Django 3.1 on 2020-08-27 08:53

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Contact',
            fields=[
                ('msg_id', models.AutoField(primary_key=True, serialize=False)),
                ('name', models.CharField(max_length=200)),
                ('email', models.CharField(default=' ', max_length=100)),
                ('phone', models.CharField(default='', max_length=60)),
                ('address', models.CharField(default=' ', max_length=1000)),
                ('textarea', models.CharField(max_length=10000)),
            ],
        ),
    ]
