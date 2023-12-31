# Generated by Django 4.2.7 on 2023-12-04 00:52

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('myapp', '0001_initial'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='datapoint',
            name='x_value',
        ),
        migrations.RemoveField(
            model_name='datapoint',
            name='y_value',
        ),
        migrations.AddField(
            model_name='datapoint',
            name='data',
            field=models.JSONField(default={}),
        ),
        migrations.CreateModel(
            name='DataColumn',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('column_name', models.CharField(max_length=255)),
                ('data_type', models.CharField(max_length=50)),
                ('visualization', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='myapp.visualization')),
            ],
        ),
    ]
