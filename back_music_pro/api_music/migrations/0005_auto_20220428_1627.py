# Generated by Django 3.1.1 on 2022-04-28 20:27

from django.db import migrations


class Migration(migrations.Migration):

    dependencies = [
        ('api_music', '0004_producto'),
    ]

    operations = [
        migrations.RenameField(
            model_name='categoria',
            old_name='_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='marca',
            old_name='_id',
            new_name='id',
        ),
        migrations.RenameField(
            model_name='modelo',
            old_name='_id',
            new_name='id',
        ),
    ]
