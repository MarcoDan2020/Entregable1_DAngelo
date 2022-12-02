# Generated by Django 4.1.3 on 2022-12-01 23:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('Contribuyente', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Concepto_Ingreso',
            fields=[
                ('id_concepto', models.AutoField(primary_key=True, serialize=False)),
                ('descripcion', models.CharField(max_length=30, verbose_name='Concepto')),
                ('remunerativo', models.BooleanField()),
            ],
            options={
                'ordering': ['-descripcion'],
            },
        ),
        migrations.AlterField(
            model_name='contribuyente',
            name='empleador',
            field=models.BooleanField(verbose_name='Es Empleador'),
        ),
    ]
