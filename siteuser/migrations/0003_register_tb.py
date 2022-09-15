# Generated by Django 3.2.14 on 2022-08-02 17:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('siteuser', '0002_state_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='register_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('gender', models.CharField(max_length=20)),
                ('dob', models.CharField(max_length=20)),
                ('address', models.CharField(max_length=20)),
                ('phone', models.CharField(max_length=20)),
                ('securityquestion', models.CharField(max_length=20)),
                ('answer', models.CharField(max_length=20)),
                ('username', models.CharField(max_length=20)),
                ('password', models.CharField(max_length=20)),
                ('countryid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteuser.country_tb')),
                ('stateid', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='siteuser.state_tb')),
            ],
        ),
    ]
