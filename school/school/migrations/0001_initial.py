# Generated by Django 4.0.3 on 2022-04-04 15:22

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Class',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('floor', models.IntegerField()),
                ('door', models.CharField(max_length=1)),
            ],
            options={
                'verbose_name_plural': 'Classes',
            },
        ),
        migrations.CreateModel(
            name='Student',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('own_class', models.ForeignKey(null=True, on_delete=django.db.models.deletion.SET_NULL, related_name='students', to='school.class', verbose_name='Class to which this student belongs')),
            ],
            options={
                'verbose_name_plural': 'Students',
            },
        ),
    ]
