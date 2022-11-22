# Generated by Django 4.1.3 on 2022-11-17 14:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Status',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('status_name', models.CharField(max_length=50, verbose_name='Status')),
            ],
        ),
        migrations.CreateModel(
            name='Type',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type_name', models.CharField(max_length=50, verbose_name='Type')),
            ],
        ),
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('summary', models.CharField(max_length=300, verbose_name='Summary')),
                ('description', models.TextField(blank=True, max_length=300, null=True, verbose_name='Description')),
                ('updated_at', models.DateTimeField(auto_now=True, verbose_name='Update At')),
                ('created_at', models.DateTimeField(auto_now_add=True, verbose_name='Created At')),
                ('status', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='status', to='webapp.status', verbose_name='Status')),
                ('type', models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type', to='webapp.type', verbose_name='Type')),
            ],
        ),
    ]
