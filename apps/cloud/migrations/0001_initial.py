# Generated by Django 4.2.6 on 2024-11-13 17:35

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='AvailabilityZone',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('name', models.CharField(max_length=225)),
                ('lat', models.FloatField()),
                ('lon', models.FloatField()),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceName',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('name', models.CharField(max_length=225)),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='ServiceDetails',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('description', models.CharField(blank=True, max_length=225, null=True)),
                ('size', models.FloatField(blank=True, null=True)),
                ('size_type', models.CharField(blank=True, choices=[('Mb', 'mb'), ('Gb', 'gb'), ('Tb', 'tb')], max_length=10, null=True, verbose_name='Size Type')),
                ('storage_type', models.CharField(blank=True, choices=[('SSD', 'ssd'), ('HDD', 'hdd'), ('NVME', 'nvme')], max_length=10, null=True, verbose_name='Storage Type')),
                ('price', models.FloatField()),
                ('service', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.servicename')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
        migrations.CreateModel(
            name='Instance',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created Time')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Updated Time')),
                ('project_name', models.CharField(max_length=225)),
                ('name', models.CharField(max_length=255)),
                ('description', models.TextField(blank=True, null=True)),
                ('ram', models.CharField(max_length=200)),
                ('cpu', models.CharField(max_length=200)),
                ('storage', models.CharField(max_length=200)),
                ('bandwidth', models.CharField(max_length=200)),
                ('ip', models.CharField(max_length=200)),
                ('user', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
                ('zone', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='cloud.availabilityzone')),
            ],
            options={
                'ordering': ['-created_at', '-updated_at'],
                'abstract': False,
            },
        ),
    ]
