# Generated by Django 3.2.6 on 2021-11-11 18:35

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('BlogCitas', '0002_auto_20211107_1615'),
    ]

    operations = [
        migrations.CreateModel(
            name='HorariosTrabajo',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hora', models.TimeField()),
            ],
        ),
    ]
