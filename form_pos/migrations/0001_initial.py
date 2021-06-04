# Generated by Django 3.0.5 on 2020-05-07 12:19

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Myform',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('date', models.DateField(blank=True, default='', null=True)),
                ('reports', models.CharField(choices=[('DAILY', 'DAILY'), ('WEEKLY', 'WEEKLY'), ('MONTHLY', 'MONTHLY')], default='', max_length=50)),
                ('team_lead', models.CharField(choices=[(1, 'a'), (2, 'b'), (3, 'c')], default='', max_length=20)),
                ('no_of_hours', models.CharField(max_length=100)),
                ('today_progress', models.CharField(max_length=100)),
                ('today_file', models.FileField(default='', upload_to='')),
                ('concern', models.CharField(max_length=500)),
                ('next_plan', models.CharField(max_length=500)),
                ('next_file', models.FileField(default='', upload_to='')),
            ],
        ),
        migrations.CreateModel(
            name='Team_Lead',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(blank=True, max_length=50)),
                ('name', models.CharField(blank=True, max_length=50)),
            ],
        ),
        migrations.CreateModel(
            name='Multi_File',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('images', models.FileField(blank=True, null=True, upload_to='form_pos/')),
                ('f', models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='form_pos.Myform')),
            ],
        ),
    ]
