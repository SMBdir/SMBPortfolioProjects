# Generated by Django 3.2.5 on 2021-09-09 19:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('lumi', '0012_sample_created_by'),
    ]

    operations = [
        migrations.AlterField(
            model_name='sample',
            name='Altitude_m',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='De_Gy',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Depth_m',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Etch_depth_max_um',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Etch_depth_min_um',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='External_K',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='External_Rb_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='External_Th_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='External_U_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='External_δK',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='External_δRb_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='External_δTh_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='External_δU_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Grain_size_max_um',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Grain_size_min_um',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Internal_K',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Internal_Rb_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Internal_Th_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Internal_U_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Internal_δK',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Internal_δRb_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Internal_δTh_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Internal_δU_ppm',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Latitude',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Longitude',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Overburden_density',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_defined_δḊc',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_defined_Ḋc',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_external_δḊα',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_external_δḊβ',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_external_δḊγ',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_external_Ḋα',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_external_Ḋβ',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_external_Ḋγ',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_internal_δḊr',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='User_internal_Ḋr',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='Water_content',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='a_value',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='δDe_Gy',
            field=models.FloatField(blank=True, default=-1, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='δDepth_m',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='δOverburden_density',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='δWater_content',
            field=models.FloatField(default=0, null=True),
        ),
        migrations.AlterField(
            model_name='sample',
            name='δa_value',
            field=models.FloatField(blank=True, default=0, null=True),
        ),
    ]
