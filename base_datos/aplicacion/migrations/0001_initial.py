# Generated by Django 4.1.2 on 2022-11-12 20:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='AereoPuerto',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('direccion', models.CharField(max_length=255)),
                ('codigo_postal', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'aereoPuerto',
                'verbose_name_plural': 'aereoPuertos',
                'db_table': 'aereoPuerto',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Asiento',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('Fila', models.CharField(max_length=1)),
                ('primera_clase', models.BooleanField(default=False)),
                ('Asiento', models.CharField(max_length=2)),
                ('disponible', models.BooleanField(default=False)),
                ('costo', models.FloatField(default=0)),
            ],
            options={
                'verbose_name': 'asiento',
                'verbose_name_plural': 'asientos',
                'db_table': 'asiento',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Avion',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('folio', models.CharField(max_length=14)),
                ('cap_max_pasajeros', models.IntegerField(default=0)),
                ('cap_max_equipaje_kilos', models.FloatField(default=0)),
                ('escalas', models.BooleanField(default=False)),
                ('salida', models.DateField(auto_now_add=True)),
                ('llegada', models.DateField(auto_now_add=True)),
                ('filas', models.IntegerField(default=0)),
                ('columnas', models.IntegerField(default=0)),
                ('estado', models.CharField(max_length=255)),
                ('destino_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.aereopuerto')),
                ('origen_id', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.aereopuerto')),
            ],
            options={
                'verbose_name': 'avion',
                'verbose_name_plural': 'aviones',
                'db_table': 'avion',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Pais',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('clave', models.CharField(max_length=255)),
                ('pais', models.CharField(max_length=255)),
            ],
            options={
                'verbose_name': 'pais',
                'verbose_name_plural': 'paises',
                'db_table': 'pais',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Piloto',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre_completo', models.CharField(max_length=255)),
                ('edad', models.IntegerField(default=22)),
                ('experiencia', models.CharField(max_length=255)),
                ('total_vuelos', models.IntegerField(default=0)),
            ],
            options={
                'verbose_name': 'piloto',
                'verbose_name_plural': 'pilotos',
                'db_table': 'piloto',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Usuario',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('nombre', models.CharField(max_length=255)),
                ('apellido_paterno', models.CharField(max_length=255)),
                ('apellido_materno', models.CharField(max_length=255)),
                ('correo', models.CharField(max_length=255)),
                ('username', models.CharField(max_length=255)),
                ('password', models.CharField(max_length=255)),
                ('empleado', models.BooleanField(default=False)),
            ],
            options={
                'verbose_name': 'usuario',
                'verbose_name_plural': 'usuarios',
                'db_table': 'usuario',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Escalas',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('salida', models.DateField(auto_now_add=True)),
                ('llegada', models.DateField(auto_now_add=True)),
                ('aereoPuerto', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.aereopuerto')),
                ('avion', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.avion')),
            ],
            options={
                'verbose_name': 'escala',
                'verbose_name_plural': 'escalas',
                'db_table': 'escala',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Equipaje',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('peso_total', models.FloatField(default=0)),
                ('costo_extra', models.FloatField(default=0)),
                ('consecutivo', models.IntegerField(default=0)),
                ('asiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.asiento')),
            ],
            options={
                'verbose_name': 'equipaje',
                'verbose_name_plural': 'equipajes',
                'db_table': 'equipaje',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Ciudad',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('clave', models.CharField(max_length=255)),
                ('ciudad', models.CharField(max_length=255)),
                ('pais', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.pais')),
            ],
            options={
                'verbose_name': 'ciudad',
                'verbose_name_plural': 'ciudades',
                'db_table': 'ciudad',
                'ordering': ['-id'],
            },
        ),
        migrations.CreateModel(
            name='Boleto',
            fields=[
                ('deleted', models.DateTimeField(editable=False, null=True)),
                ('deleted_by_cascade', models.BooleanField(default=False, editable=False)),
                ('id', models.BigAutoField(primary_key=True, serialize=False)),
                ('folio', models.CharField(max_length=14)),
                ('fecha_hora_compra', models.DateTimeField(auto_now_add=True)),
                ('sub_total', models.FloatField(default=0)),
                ('iva', models.FloatField(default=0)),
                ('total', models.FloatField(default=0)),
                ('asiento', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.asiento')),
                ('usuario', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.usuario')),
            ],
            options={
                'verbose_name': 'boleto',
                'verbose_name_plural': 'boletos',
                'db_table': 'boleto',
                'ordering': ['-id'],
            },
        ),
        migrations.AddField(
            model_name='avion',
            name='piloto',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.piloto'),
        ),
        migrations.AddField(
            model_name='asiento',
            name='avion',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.avion'),
        ),
        migrations.AddField(
            model_name='aereopuerto',
            name='ciudad',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='+', to='aplicacion.ciudad'),
        ),
    ]
