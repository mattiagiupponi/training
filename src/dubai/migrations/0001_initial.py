# Generated by Django 3.2.23 on 2023-12-18 07:52

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='TestModel',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(help_text='This is the name of our field', max_length=255)),
                ('description', models.TextField()),
                ('is_enabled', models.BooleanField(default=False)),
                ('number', models.IntegerField()),
            ],
        ),
    ]
