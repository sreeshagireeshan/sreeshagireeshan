# Generated by Django 3.2.14 on 2022-08-06 06:33

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0009_agefactor_tb'),
        ('siteuser', '0008_blacklist_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='customerhobbyfactor_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('factorid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.hobbyfactor_tb')),
                ('hobbyid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteadmin.hobbyname_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteuser.register_tb')),
            ],
        ),
    ]
