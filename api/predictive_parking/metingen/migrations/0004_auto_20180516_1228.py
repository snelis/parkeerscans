# Generated by Django 2.0.1 on 2018-05-16 12:28

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('metingen', '0003_auto_20171121_1246'),
    ]

    operations = [
        migrations.AddField(
            model_name='scan',
            name='parkeerrecht_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AddField(
            model_name='scanraw',
            name='parkeerrecht_id',
            field=models.BigIntegerField(null=True),
        ),
        migrations.AlterField(
            model_name='scan',
            name='sperscode',
            field=models.CharField(max_length=15, null=True),
        ),
    ]