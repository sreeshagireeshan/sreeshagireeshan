# Generated by Django 3.2.14 on 2022-08-05 17:36

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteuser', '0007_contact_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='blacklist_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('date', models.CharField(max_length=20)),
                ('time', models.CharField(max_length=20)),
                ('remarks', models.CharField(max_length=20)),
                ('contactid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='contactid2', to='siteuser.register_tb')),
                ('userid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, related_name='userid2', to='siteuser.register_tb')),
            ],
        ),
    ]
