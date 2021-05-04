# Generated by Django 3.2 on 2021-05-03 21:46

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('customer', '0007_alter_ordermodel_status'),
    ]

    operations = [
        migrations.RemoveField(
            model_name='ordermodel',
            name='status',
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='is_paid',
            field=models.BooleanField(default=False),
        ),
        migrations.AddField(
            model_name='ordermodel',
            name='is_shipped',
            field=models.BooleanField(default=False),
        ),
    ]
