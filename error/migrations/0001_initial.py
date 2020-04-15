# Generated by Django 3.0.5 on 2020-04-12 04:55

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Issue',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('timestamp', models.DateTimeField(auto_now=True)),
                ('updated', models.DateTimeField(auto_now_add=True)),
                ('image', models.FileField(blank=True, default='/placeholder.png', null=True, upload_to='')),
                ('title', models.CharField(max_length=120)),
                ('body', models.TextField()),
                ('location', models.CharField(max_length=120)),
            ],
            options={
                'ordering': ['-timestamp', '-updated'],
            },
        ),
    ]
