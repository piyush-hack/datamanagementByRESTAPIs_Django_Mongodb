# Generated by Django 3.1.4 on 2021-06-18 20:06

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('tutorials', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='tutorial',
            old_name='description',
            new_name='size',
        ),
        migrations.RemoveField(
            model_name='tutorial',
            name='published',
        ),
        migrations.AddField(
            model_name='tutorial',
            name='toppings',
            field=models.CharField(default='', max_length=200),
        ),
    ]
