# Generated by Django 3.1 on 2020-08-27 12:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0003_auto_20200827_1736'),
    ]

    operations = [
        migrations.RenameField(
            model_name='blogpost',
            old_name='con1',
            new_name='content',
        ),
        migrations.RenameField(
            model_name='blogpost',
            old_name='head1',
            new_name='heading',
        ),
        migrations.AddField(
            model_name='blogpost',
            name='category',
            field=models.CharField(default='', max_length=20),
        ),
        migrations.AddField(
            model_name='blogpost',
            name='subcategory',
            field=models.CharField(default='', max_length=20),
        ),
    ]
