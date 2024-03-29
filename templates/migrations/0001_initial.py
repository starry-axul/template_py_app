# Generated by Django 4.2.5 on 2023-11-05 18:57

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Template',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.CharField(blank=True, max_length=2)),
                ('version', models.IntegerField()),
                ('title', models.CharField(blank=True, max_length=40)),
                ('body', models.TextField(blank=True, max_length=150)),
                ('placeholders', models.TextField(blank=True, max_length=100, null=True)),
                ('created', models.DateTimeField(auto_now_add=True, verbose_name='date published')),
                ('updated', models.DateTimeField(auto_now=True, verbose_name='date updated')),
            ],
        ),
    ]
