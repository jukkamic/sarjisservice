# Generated by Django 4.0.4 on 2023-02-21 19:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Comic',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('display_name', models.CharField(max_length=100)),
                ('display_source', models.CharField(max_length=100)),
                ('date_publish', models.DateField(blank=True, null=True)),
                ('title', models.TextField(blank=True, null=True)),
                ('alt', models.TextField(blank=True, null=True)),
                ('perm_link', models.TextField()),
                ('img_url', models.TextField(null=True)),
                ('prev_link', models.TextField(null=True)),
                ('prev_id', models.IntegerField(null=True)),
                ('next_link', models.TextField(null=True)),
                ('next_id', models.IntegerField(null=True)),
                ('img_file', models.TextField(null=True)),
            ],
        ),
    ]
