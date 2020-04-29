# Generated by Django 3.0.5 on 2020-04-12 21:07

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Car',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('slug', models.SlugField(unique=True)),
                ('maker', models.CharField(max_length=127)),
                ('car_model', models.CharField(max_length=64)),
                ('year', models.IntegerField()),
                ('transmission', models.PositiveSmallIntegerField(choices=[(0, 'Manual'), (1, 'Automatic'), (2, 'Robot')], default=0)),
                ('color', models.CharField(max_length=64)),
            ],
        ),
    ]