# Generated by Django 4.1.3 on 2024-05-10 17:26

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("militares", "0010_finalizadomilitar_finalizadobeneficiario"),
    ]

    operations = [
        migrations.CreateModel(
            name="TB_Vencimentos",
            fields=[
                (
                    "id",
                    models.BigAutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("Posto_Grad", models.CharField(max_length=100)),
                ("Codigo", models.CharField(max_length=100)),
                (
                    "Salario_Padrao",
                    models.DecimalField(decimal_places=2, max_digits=10),
                ),
                ("Cod_Funcao", models.CharField(max_length=100)),
            ],
        ),
    ]
