# Generated by Django 4.2.6 on 2024-11-14 08:14

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cloud', '0004_instance_is_active'),
    ]

    operations = [
        migrations.AddField(
            model_name='instance',
            name='is_payment',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='instance',
            name='tranId',
            field=models.CharField(blank=True, max_length=500, null=True),
        ),
    ]
