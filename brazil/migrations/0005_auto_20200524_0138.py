# Generated by Django 3.0.5 on 2020-05-24 04:38

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("brazil", "0004_auto_20200425_1952"),
    ]

    operations = [
        migrations.AddField(
            model_name="statedata",
            name="update_source",
            field=models.CharField(
                choices=[
                    ("MS", "Ministério da Saúde"),
                    ("SES", "Secretaria Estadual de Saúde"),
                ],
                default="Secretaria Estadual de Saúde",
                max_length=30,
            ),
            preserve_default=False,
        ),
        migrations.AlterField(
            model_name="statedata",
            name="state",
            field=models.CharField(
                choices=[
                    ("AC", "AC"),
                    ("AL", "AL"),
                    ("AM", "AM"),
                    ("AP", "AP"),
                    ("BA", "BA"),
                    ("CE", "CE"),
                    ("DF", "DF"),
                    ("ES", "ES"),
                    ("GO", "GO"),
                    ("MA", "MA"),
                    ("MG", "MG"),
                    ("MS", "MS"),
                    ("MT", "MT"),
                    ("PA", "PA"),
                    ("PB", "PB"),
                    ("PE", "PE"),
                    ("PI", "PI"),
                    ("PR", "PR"),
                    ("RJ", "RJ"),
                    ("RN", "RN"),
                    ("RO", "RO"),
                    ("RR", "RR"),
                    ("RS", "RS"),
                    ("SC", "SC"),
                    ("SE", "SE"),
                    ("SP", "SP"),
                    ("TO", "TO"),
                ],
                max_length=30,
            ),
        ),
    ]
