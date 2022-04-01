# Generated by Django 2.2 on 2022-03-14 20:24

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Post',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('title', models.CharField(max_length=500)),
                ('content', models.TextField()),
                ('extract', models.CharField(max_length=1000)),
                ('date_pub', models.DateTimeField()),
                ('author', models.CharField(default='Kvidal', max_length=250)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
