# Generated by Django 5.1.7 on 2025-03-25 10:06

import core.managers
import django.db.models.deletion
import uuid
from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('auth', '0012_alter_user_first_name_max_length'),
    ]

    operations = [
        migrations.CreateModel(
            name='User',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('password', models.CharField(max_length=128, verbose_name='password')),
                ('last_login', models.DateTimeField(blank=True, null=True, verbose_name='last login')),
                ('is_superuser', models.BooleanField(default=False, help_text='Designates that this user has all permissions without explicitly assigning them.', verbose_name='superuser status')),
                ('name', models.CharField(max_length=30, verbose_name='first name')),
                ('lastname', models.CharField(max_length=30, verbose_name='last name')),
                ('alumns_group', models.CharField(blank=True, choices=[('1AI', '1_A_infantil'), ('1BI', '1_B_infantil'), ('1CI', '1_C_infantil'), ('1DI', '1_D_infantil'), ('1EI', '1_E_infantil'), ('2AI', '2_A_infantil'), ('2BI', '2_B_infantil'), ('2CI', '2_C_infantil'), ('2DI', '2_D_infantil'), ('3AI', '3_A_infantil'), ('3BI', '3_B_infantil'), ('3CI', '3_C_infantil'), ('3DI', '3_D_infantil'), ('1AP', '1_A_primaria'), ('1BP', '1_B_primaria'), ('1CP', '1_C_primaria'), ('1DP', '1_D_primaria'), ('2AP', '2_A_primaria'), ('2BP', '2_B_primaria'), ('2CP', '2_C_primaria'), ('3AP', '3_A_primaria'), ('3BP', '3_B_primaria'), ('3CP', '3_C_primaria'), ('4AP', '4_A_primaria'), ('4BP', '4_B_primaria'), ('5AP', '5_A_primaria'), ('5BP', '5_B_primaria'), ('6AP', '6_A_primaria'), ('6BP', '6_B_primaria')], max_length=10, null=True, verbose_name='alumns_group')),
                ('email', models.EmailField(max_length=254, unique=True, verbose_name='email address')),
                ('country', models.CharField(default='Chile', max_length=128, verbose_name='country')),
                ('date_joined', models.DateTimeField(auto_now_add=True, verbose_name='date joined')),
                ('uuid', models.UUIDField(default=uuid.uuid4, editable=False, unique=True)),
                ('is_staff', models.BooleanField(default=False, help_text='Designates wheter the user can log into this admin site.', verbose_name='staff status')),
                ('is_active', models.BooleanField(default=True, verbose_name='active')),
                ('groups', models.ManyToManyField(blank=True, help_text='The groups this user belongs to. A user will get all permissions granted to each of their groups.', related_name='user_set', related_query_name='user', to='auth.group', verbose_name='groups')),
                ('user_permissions', models.ManyToManyField(blank=True, help_text='Specific permissions for this user.', related_name='user_set', related_query_name='user', to='auth.permission', verbose_name='user permissions')),
            ],
            options={
                'verbose_name': 'user',
                'verbose_name_plural': 'users',
            },
            managers=[
                ('objects', core.managers.UserManager()),
            ],
        ),
        migrations.CreateModel(
            name='Alumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('Grupo', models.CharField(choices=[('1AI', '1_A_infantil'), ('1BI', '1_B_infantil'), ('1CI', '1_C_infantil'), ('1DI', '1_D_infantil'), ('1EI', '1_E_infantil'), ('2AI', '2_A_infantil'), ('2BI', '2_B_infantil'), ('2CI', '2_C_infantil'), ('2DI', '2_D_infantil'), ('3AI', '3_A_infantil'), ('3BI', '3_B_infantil'), ('3CI', '3_C_infantil'), ('3DI', '3_D_infantil'), ('1AP', '1_A_primaria'), ('1BP', '1_B_primaria'), ('1CP', '1_C_primaria'), ('1DP', '1_D_primaria'), ('2AP', '2_A_primaria'), ('2BP', '2_B_primaria'), ('2CP', '2_C_primaria'), ('3AP', '3_A_primaria'), ('3BP', '3_B_primaria'), ('3CP', '3_C_primaria'), ('4AP', '4_A_primaria'), ('4BP', '4_B_primaria'), ('5AP', '5_A_primaria'), ('5BP', '5_B_primaria'), ('6AP', '6_A_primaria'), ('6BP', '6_B_primaria')], max_length=3)),
                ('Nombre', models.CharField(max_length=200)),
                ('Fotografia', models.URLField(blank=True, null=True)),
                ('Sexo', models.CharField(choices=[('H', 'Hombre'), ('M', 'Mujer'), ('NA', 'Sin especificar')], max_length=2)),
                ('Observaciones', models.TextField(blank=True, max_length=300, null=True)),
                ('PET_KET', models.CharField(blank=True, choices=[('PET', 'PET'), ('KET', 'KET'), ('None', 'None')], default='', max_length=4)),
                ('Calificaciones', models.JSONField(blank=True, default=dict, null=True)),
                ('Telefono_contacto_padre', models.PositiveIntegerField(blank=True, null=True)),
                ('Nombre_padre', models.CharField(blank=True, max_length=30, null=True)),
                ('Email_padre', models.EmailField(blank=True, max_length=254, null=True)),
                ('Telefono_contacto_madre', models.PositiveIntegerField(blank=True, null=True)),
                ('Nombre_madre', models.CharField(blank=True, max_length=30, null=True)),
                ('Email_madre', models.EmailField(blank=True, max_length=254, null=True)),
                ('Personas_autorizadas_recogida', models.TextField(blank=True, max_length=300, null=True)),
                ('Comedor', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2)),
                ('Alergias', models.TextField(blank=True, max_length=300, null=True)),
                ('IBAN', models.CharField(blank=True, max_length=24, null=True)),
                ('Titular_cuenta', models.CharField(blank=True, max_length=30, null=True)),
                ('Beca_comedor', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2)),
                ('Pagos_pendientes', models.CharField(blank=True, max_length=200, null=True)),
                ('Adhesion_Accede', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2)),
                ('Senal_Accede', models.CharField(choices=[('SI', 'SI'), ('NO', 'NO')], max_length=2)),
                ('Tutor_a', models.ForeignKey(on_delete=django.db.models.deletion.DO_NOTHING, to=settings.AUTH_USER_MODEL)),
            ],
            options={
                'ordering': ['Grupo', 'Nombre'],
            },
        ),
    ]
