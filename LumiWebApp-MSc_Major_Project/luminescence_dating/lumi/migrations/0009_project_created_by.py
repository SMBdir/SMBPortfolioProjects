# Generated by Django 3.2.5 on 2021-08-31 22:08

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumi', '0008_rename_sample_id_sample_sample_name'),
    ]

    operations = [
        migrations.AddField(
            model_name='project',
            name='created_by',
            field=models.CharField(default='', max_length=64),
        ),
    ]
