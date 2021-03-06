# Generated by Django 3.2.5 on 2021-08-21 06:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('lumi', '0003_auto_20210815_0052'),
    ]

    operations = [
        migrations.CreateModel(
            name='Project',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('project_name', models.CharField(default='', max_length=64)),
            ],
        ),
        migrations.RemoveField(
            model_name='sample',
            name='project_ID',
        ),
        migrations.AddField(
            model_name='sample',
            name='project',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='lumi.project'),
        ),
    ]
