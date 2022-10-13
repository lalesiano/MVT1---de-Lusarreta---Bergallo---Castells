# Generated by Django 4.1.2 on 2022-10-12 23:21

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('MVT_App', '0003_rename_persona_humano'),
    ]

    operations = [
        migrations.CreateModel(
            name='Persona',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nombre', models.CharField(max_length=30)),
                ('apellido', models.CharField(max_length=30)),
                ('numero_id', models.IntegerField()),
                ('fecha_ingreso', models.DateField(null=True)),
            ],
        ),
    ]
