# -*- coding: utf-8 -*-
# Generated by Django 1.9.7 on 2016-06-27 14:07
from __future__ import unicode_literals

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.TextField()),
                ('text', models.TextField()),
                ('runtime', models.IntegerField(null=True)),
                ('is_paid', models.BooleanField()),
                ('min_age', models.IntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Image',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('url', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Membership',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('role', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Person',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('full_name', models.TextField()),
            ],
        ),
        migrations.CreateModel(
            name='Place',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('type', models.TextField()),
                ('title', models.TextField()),
                ('lat', models.FloatField(null=True)),
                ('lon', models.FloatField(null=True)),
            ],
        ),
        migrations.CreateModel(
            name='Session',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('time', models.DateTimeField()),
                ('event', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Event')),
                ('place', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Place')),
            ],
        ),
        migrations.CreateModel(
            name='Tag',
            fields=[
                ('word', models.TextField(primary_key=True, serialize=False)),
            ],
        ),
        migrations.AddField(
            model_name='place',
            name='events',
            field=models.ManyToManyField(through='app.Session', to='app.Event'),
        ),
        migrations.AddField(
            model_name='place',
            name='gallery',
            field=models.ManyToManyField(to='app.Image'),
        ),
        migrations.AddField(
            model_name='place',
            name='persons',
            field=models.ManyToManyField(through='app.Membership', to='app.Person'),
        ),
        migrations.AddField(
            model_name='place',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
        migrations.AddField(
            model_name='membership',
            name='person',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='app.Person'),
        ),
        migrations.AddField(
            model_name='membership',
            name='place',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='members', to='app.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='gallery',
            field=models.ManyToManyField(to='app.Image'),
        ),
        migrations.AddField(
            model_name='event',
            name='places',
            field=models.ManyToManyField(through='app.Session', to='app.Place'),
        ),
        migrations.AddField(
            model_name='event',
            name='tags',
            field=models.ManyToManyField(to='app.Tag'),
        ),
    ]
