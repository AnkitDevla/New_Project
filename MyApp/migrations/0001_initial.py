# Generated by Django 4.0.1 on 2022-05-24 10:14

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Trainee',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=20)),
                ('contact_no', models.CharField(max_length=13)),
                ('exp', models.PositiveIntegerField()),
            ],
        ),
        migrations.CreateModel(
            name='Trainer',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=200)),
                ('age', models.IntegerField()),
                ('email', models.EmailField(max_length=200)),
                ('contact_no', models.CharField(max_length=13)),
                ('gender', models.CharField(max_length=10)),
            ],
        ),
        migrations.CreateModel(
            name='Doubts',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=20)),
                ('question', models.CharField(max_length=500)),
                ('answer', models.CharField(max_length=500)),
                ('when_asked', models.DateTimeField()),
                ('status', models.CharField(max_length=20)),
                ('answer_by', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.trainer')),
                ('question_from', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='MyApp.trainee')),
            ],
        ),
    ]
