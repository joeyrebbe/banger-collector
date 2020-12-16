# Generated by Django 3.1.2 on 2020-12-14 07:42

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('main_app', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Listening',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('date', models.DateField()),
                ('listen', models.CharField(choices=[('Y', 'Yes'), ('N', 'No')], default=('Y', 'Yes'), max_length=1)),
                ('banger', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='main_app.banger')),
            ],
        ),
    ]
