# Generated by Django 3.2.14 on 2022-08-04 11:40

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0006_season_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='seasonfactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factorname', models.CharField(max_length=20)),
                ('seasonid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.season_tb')),
            ],
        ),
    ]
