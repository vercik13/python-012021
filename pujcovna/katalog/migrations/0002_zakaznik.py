# Generated by Django 3.2 on 2021-05-05 18:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0001_initial'),
    ]

    operations = [
        migrations.CreateModel(
            name='Zakaznik',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('jmeno', models.CharField(max_length=100)),
                ('prijmeni', models.CharField(max_length=1000)),
                ('cislo_ridicskeho_prukazu', models.CharField(max_length=100)),
            ],
        ),
    ]
