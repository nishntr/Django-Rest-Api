# Generated by Django 3.0.3 on 2020-03-16 13:26

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Para',
            fields=[
                ('id', models.AutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('created', models.DateTimeField(auto_now_add=True)),
                ('para', models.TextField()),
            ],
            options={
                'verbose_name': 'Para',
                'verbose_name_plural': 'Paras',
            },
        ),
    ]
