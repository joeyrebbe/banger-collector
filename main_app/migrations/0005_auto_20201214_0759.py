# Generated by Django 3.1.2 on 2020-12-14 07:59

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0004_auto_20201214_0757'),
    ]

    operations = [
        migrations.AlterField(
            model_name='listening',
            name='listen',
            field=models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default='Y', max_length=1),
        ),
    ]