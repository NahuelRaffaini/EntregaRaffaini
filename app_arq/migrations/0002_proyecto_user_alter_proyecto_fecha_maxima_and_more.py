# Generated by Django 4.2.5 on 2023-10-04 21:20

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
        ('app_arq', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='proyecto',
            name='user',
            field=models.OneToOneField(null=True, on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='fecha_maxima',
            field=models.DateField(blank=True),
        ),
        migrations.AlterField(
            model_name='proyecto',
            name='link',
            field=models.URLField(blank=True, max_length=256),
        ),
        migrations.AlterField(
            model_name='trabajador',
            name='puesto',
            field=models.IntegerField(choices=[('1', 'Obrero'), ('2', 'Maestro mayor'), ('3', 'Arquitecto'), ('4', 'Ingeniero'), ('5', 'Renderista'), ('6', 'Maquetista'), ('7', 'Otro')]),
        ),
    ]