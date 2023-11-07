# Generated by Django 4.2.5 on 2023-11-05 22:27

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('templates', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='template',
            name='cluster',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterField(
            model_name='template',
            name='type',
            field=models.CharField(blank=True, max_length=20),
        ),
        migrations.AlterUniqueTogether(
            name='template',
            unique_together={('cluster', 'type', 'version')},
        ),
        migrations.RemoveField(
            model_name='template',
            name='title',
        ),
    ]