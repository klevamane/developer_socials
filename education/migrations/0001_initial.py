# Generated by Django 2.2 on 2019-04-15 11:19

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Education',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('instution_name', models.CharField(max_length=100)),
                ('degree', models.CharField(blank=True, max_length=100, null=True)),
                ('location', models.CharField(max_length=200)),
                ('_from', models.DateField(blank=True, null=True)),
                ('to', models.DateField(blank=True, null=True)),
                ('created_at', models.DateField(auto_now_add=True)),
                ('updated_at', models.DateField(auto_now=True)),
            ],
        ),
    ]
