# Generated by Django 3.0.5 on 2020-04-25 22:52

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('brazil', '0003_auto_20200422_2302'),
    ]

    operations = [
        migrations.AlterField(
            model_name='statedata',
            name='date',
            field=models.DateField(),
        ),
    ]
