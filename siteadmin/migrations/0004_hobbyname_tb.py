# Generated by Django 3.2.14 on 2022-08-03 12:12

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('siteadmin', '0003_delete_hobby_tb'),
    ]

    operations = [
        migrations.CreateModel(
            name='hobbyname_tb',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('hobbyname', models.CharField(max_length=20)),
            ],
        ),
    ]
