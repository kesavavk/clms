# Generated by Django 2.1 on 2018-08-10 11:00

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        ('masterdata', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='bonus',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('rndp', models.FloatField()),
                ('drate', models.FloatField()),
                ('basic', models.FloatField()),
                ('date', models.DateField()),
                ('mastid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.Master')),
            ],
        ),
        migrations.CreateModel(
            name='incentive',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('wdays', models.FloatField()),
                ('mdate', models.DateField()),
                ('cid', models.CharField(max_length=6)),
                ('uid', models.CharField(max_length=6)),
                ('divid', models.CharField(max_length=3)),
                ('secid', models.CharField(max_length=4)),
                ('incamt', models.FloatField()),
                ('rpd', models.IntegerField()),
                ('epx', models.FloatField()),
                ('mastid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.Master')),
            ],
        ),
        migrations.CreateModel(
            name='Payroll',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('divid', models.CharField(max_length=3)),
                ('secid', models.CharField(max_length=4)),
                ('wdays', models.FloatField()),
                ('otdays', models.FloatField()),
                ('iomdays', models.FloatField()),
                ('iomotdays', models.FloatField()),
                ('totdays', models.FloatField()),
                ('drate', models.FloatField()),
                ('basic', models.FloatField()),
                ('other', models.FloatField()),
                ('other1', models.FloatField()),
                ('otamt', models.FloatField()),
                ('wdamt', models.FloatField()),
                ('wdotamt', models.FloatField()),
                ('iomamt', models.FloatField()),
                ('iomotamt', models.FloatField()),
                ('grosse', models.FloatField()),
                ('pfamt', models.FloatField()),
                ('esiamt', models.FloatField()),
                ('ded', models.FloatField()),
                ('othded', models.FloatField()),
                ('netamt', models.FloatField()),
                ('wbasic', models.FloatField()),
                ('iombasic', models.FloatField()),
                ('wpfamt', models.FloatField()),
                ('wesiamt', models.FloatField()),
                ('iompfamt', models.FloatField()),
                ('iomesiamt', models.FloatField()),
                ('wdotheramt', models.FloatField()),
                ('iomotheramt', models.FloatField()),
                ('supcharge', models.FloatField()),
                ('strenth', models.IntegerField()),
                ('pdate', models.DateField()),
                ('mastid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='masterdata.Master')),
            ],
        ),
    ]
