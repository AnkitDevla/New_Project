# Generated by Django 4.0.4 on 2022-05-30 15:25

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0005_alter_doubts_status'),
    ]

    operations = [
        migrations.AlterField(
            model_name='trainer',
            name='gender',
            field=models.CharField(max_length=10),
        ),
    ]
