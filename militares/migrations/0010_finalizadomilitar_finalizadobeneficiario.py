# Generated by Django 4.1.3 on 2024-05-08 20:20

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ("militares", "0009_alter_beneficiario_cpf_alter_beneficiario_militar"),
    ]

    operations = [
        migrations.CreateModel(
            name="FinalizadoMilitar",
            fields=[
                (
                    "RE",
                    models.CharField(max_length=6, primary_key=True, serialize=False),
                ),
                ("posto_graduacao", models.CharField(max_length=100)),
                ("nome", models.CharField(max_length=255)),
                ("adicionais", models.IntegerField()),
                ("dependentes", models.IntegerField()),
                ("sexta_parte", models.CharField(max_length=3)),
                (
                    "hora_aula",
                    models.DecimalField(
                        blank=True, decimal_places=2, max_digits=5, null=True
                    ),
                ),
                ("data_agregacao", models.DateField()),
                ("data_saida", models.DateField(blank=True, null=True)),
                ("oficio_dp", models.CharField(max_length=100)),
                ("mes_referencia", models.CharField(max_length=3)),
                ("pag_a_contar_de", models.DateField()),
            ],
        ),
        migrations.CreateModel(
            name="FinalizadoBeneficiario",
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
                ("cpf", models.CharField(max_length=11)),
                ("nome", models.CharField(max_length=255)),
                ("agencia_cc", models.CharField(max_length=100)),
                ("cota", models.DecimalField(decimal_places=2, max_digits=5)),
                (
                    "militar",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="militares.finalizadomilitar",
                    ),
                ),
            ],
        ),
    ]