# Generated by Django 3.2 on 2021-05-09 16:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('katalog', '0005_auto_20210507_2138'),
    ]

    operations = [
        migrations.CreateModel(
            name='PridaniAutomobilu',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('registracni_znacka', models.CharField(max_length=100)),
                ('znacka_vozidla', models.CharField(max_length=100)),
                ('pocet_kilometru', models.IntegerField()),
                ('datum_tech_kontroly', models.DateField()),
            ],
        ),
    ]
