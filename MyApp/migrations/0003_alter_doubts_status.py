# Generated by Django 4.0.4 on 2022-05-26 07:30

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('MyApp', '0002_alter_trainee_email'),
    ]

    operations = [
        migrations.AlterField(
            model_name='doubts',
            name='status',
            field=models.CharField(choices=[('SOLVED', 'solved'), ('UNSOLVED', 'unsolved')], max_length=20),
        ),
    ]
