# Generated by Django 4.1.6 on 2023-02-03 15:29

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='City',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
            ],
        ),
        migrations.CreateModel(
            name='Walker',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('email', models.CharField(max_length=155)),
                ('city', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='walkers', to='deshawnapi.city')),
            ],
        ),
        migrations.CreateModel(
            name='Dog',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=155)),
                ('walker', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='dogs', to='deshawnapi.walker')),
            ],
        ),
    ]
