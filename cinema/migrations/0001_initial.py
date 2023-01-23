# Generated by Django 4.1.5 on 2023-01-23 19:42

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Movie',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=56)),
                ('description', models.CharField(blank=True, max_length=255, null=True)),
                ('duration', models.IntegerField()),
            ],
            options={
                'verbose_name_plural': 'cinemas',
            },
        ),
    ]