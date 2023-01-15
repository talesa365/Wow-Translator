# Generated by Django 4.1.4 on 2023-01-15 21:41

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('write_encode_app', '0008_alter_input_content'),
    ]

    operations = [
        migrations.AlterField(
            model_name='input',
            name='character_length',
            field=models.CharField(default='', max_length=4),
        ),
        migrations.AlterField(
            model_name='input',
            name='content',
            field=models.TextField(default='', max_length=9999),
        ),
        migrations.AlterField(
            model_name='session',
            name='session_key',
            field=models.CharField(default='', max_length=50, unique=True),
        ),
        migrations.AlterField(
            model_name='translation',
            name='language',
            field=models.CharField(default='', max_length=15),
        ),
    ]
