# Generated by Django 2.1.1 on 2019-02-25 16:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metingen', '0004_auto_20180516_1228'),
    ]

    operations = [
        migrations.AlterField(
            model_name='scan',
            name='id',
            field=models.CharField(max_length=38, primary_key=True, serialize=False),
        ),
    ]
