# Generated by Django 4.1.3 on 2022-11-21 14:47

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('webapp', '0002_remove_issue_type_issuetype_issue_type'),
    ]

    operations = [
        migrations.RenameField(
            model_name='type',
            old_name='type_name',
            new_name='name',
        ),
        migrations.AlterField(
            model_name='issuetype',
            name='type',
            field=models.ForeignKey(on_delete=django.db.models.deletion.PROTECT, related_name='type_issue', to='webapp.type', verbose_name='type_issue'),
        ),
    ]
