# Generated by Django 3.1 on 2020-08-29 12:32

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0004_auto_20200827_1753'),
    ]

    operations = [
        migrations.CreateModel(
            name='Feature',
            fields=[
                ('post_id', models.AutoField(primary_key=True, serialize=False)),
                ('author', models.CharField(default='', max_length=50)),
                ('title', models.CharField(default='', max_length=500)),
                ('heading', models.CharField(default='', max_length=5000)),
                ('content', models.CharField(default='', max_length=50000)),
                ('category', models.CharField(default='', max_length=20)),
                ('subcategory', models.CharField(default='', max_length=20)),
                ('timeStemp', models.DateTimeField(blank=True)),
                ('slug', models.CharField(default='', max_length=100)),
                ('summary', models.CharField(default='', max_length=50000)),
                ('thumbnail', models.ImageField(default='', upload_to='blog/images')),
            ],
        ),
    ]
