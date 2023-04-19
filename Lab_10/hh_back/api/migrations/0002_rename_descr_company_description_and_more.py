# Generated by Django 4.2 on 2023-04-18 11:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('api', '0001_initial'),
    ]

    operations = [
        migrations.RenameField(
            model_name='company',
            old_name='descr',
            new_name='description',
        ),
        migrations.RenameField(
            model_name='vacancy',
            old_name='descr',
            new_name='description',
        ),
        migrations.AlterField(
            model_name='vacancy',
            name='company',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='api.company'),
        ),
    ]
