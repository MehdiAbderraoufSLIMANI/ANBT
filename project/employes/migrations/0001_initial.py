# Generated by Django 4.0.5 on 2022-08-06 07:34

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Employe',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('nom', models.CharField(max_length=30, null=True)),
                ('prenom', models.CharField(max_length=30, null=True)),
                ('Nbureau', models.IntegerField(null=True, verbose_name='N°bureau')),
                ('direction', models.CharField(max_length=50, null=True)),
                ('fonction', models.CharField(max_length=50, null=True)),
                ('addresse_ip', models.CharField(max_length=100, null=True, unique=True, verbose_name='addresse ip')),
            ],
        ),
    ]
