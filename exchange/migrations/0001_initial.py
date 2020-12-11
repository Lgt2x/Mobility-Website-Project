# Generated by Django 3.1.4 on 2020-12-04 10:58

import django.db.models.deletion
from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="City",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
            ],
        ),
        migrations.CreateModel(
            name="Country",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                (
                    "continent",
                    models.CharField(
                        choices=[
                            ("AS", "Asie"),
                            ("AF", "Afrique"),
                            ("AdN", "Amerique du Nord"),
                            ("AdS", "Amerique du Sud"),
                            ("EU", "Europe"),
                            ("OC", "Oceanie"),
                        ],
                        max_length=30,
                    ),
                ),
                ("ECTSConversion", models.FloatField(default=0)),
            ],
        ),
        migrations.CreateModel(
            name="Exchange",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "year",
                    models.IntegerField(choices=[(4, "4TC"), (5, "5TC")], default=4),
                ),
                (
                    "semester",
                    models.IntegerField(
                        choices=[(1, "S1"), (2, "S2"), (3, "Année")], default=1
                    ),
                ),
                ("start_date", models.DateField()),
                ("end_date", models.DateField()),
                ("visa", models.BooleanField(default=False)),
                ("visa_months", models.IntegerField(blank=True, default=0, null=True)),
                ("visa_weeks", models.IntegerField(blank=True, default=0, null=True)),
                ("visa_days", models.IntegerField(blank=True, default=0, null=True)),
                ("comment", models.CharField(blank=True, max_length=10000, null=True)),
                ("rent", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "monthly_expenses",
                    models.IntegerField(blank=True, default=0, null=True),
                ),
                (
                    "night_life_grade",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                        default=0,
                        null=True,
                    ),
                ),
                (
                    "cultural_life_grade",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                        default=0,
                        null=True,
                    ),
                ),
                (
                    "security_grade",
                    models.IntegerField(
                        blank=True,
                        choices=[(1, "1"), (2, "2"), (3, "3"), (4, "4"), (5, "5")],
                        default=0,
                        null=True,
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="Student",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=100)),
                ("surname", models.CharField(max_length=100)),
                (
                    "email",
                    models.EmailField(
                        default="prenom.nom@insa-lyon.fr",
                        help_text="Utilisez votre adresse INSA : prenom.nom@insa-lyon.fr",
                        max_length=254,
                    ),
                ),
                (
                    "INSA_department",
                    models.CharField(
                        choices=[
                            ("BS", "BS"),
                            ("GCU", "GCU"),
                            ("GM", "GM"),
                            ("GE", "GE"),
                            ("TC", "TC"),
                            ("IF", "IF"),
                            ("SGM", "SGM"),
                            ("GEN", "GEN"),
                            ("GI", "GI"),
                        ],
                        max_length=10,
                    ),
                ),
                (
                    "nationality",
                    models.CharField(blank=True, max_length=100, null=True),
                ),
            ],
        ),
        migrations.CreateModel(
            name="University",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(max_length=1000)),
                ("website", models.URLField(blank=True)),
                (
                    "latitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=11, null=True
                    ),
                ),
                (
                    "longitude",
                    models.DecimalField(
                        blank=True, decimal_places=6, max_digits=11, null=True
                    ),
                ),
                (
                    "rank_metric",
                    models.DecimalField(decimal_places=2, default=0, max_digits=3),
                ),
                (
                    "life_metric",
                    models.DecimalField(decimal_places=2, default=0, max_digits=3),
                ),
                ("CWUR_rank", models.IntegerField(blank=True, null=True)),
                ("demand", models.IntegerField(default=0)),
                ("project", models.BooleanField(default=False)),
                ("can_split_year", models.BooleanField(default=False)),
                ("AvailableForBS", models.BooleanField(default=False)),
                ("AvailableForGCU", models.BooleanField(default=False)),
                ("AvailableForGE", models.BooleanField(default=False)),
                ("AvailableForGEN", models.BooleanField(default=False)),
                ("AvailableForGI", models.BooleanField(default=False)),
                ("AvailableForGM", models.BooleanField(default=False)),
                ("AvailableForIF", models.BooleanField(default=False)),
                ("AvailableForSGM", models.BooleanField(default=False)),
                ("AvailableForTC", models.BooleanField(default=False)),
                (
                    "city",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE, to="exchange.city"
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UniversityLanguages",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("language", models.CharField(default="", max_length=50)),
                (
                    "diploma_language",
                    models.CharField(blank=True, max_length=200, null=True),
                ),
                (
                    "language_level",
                    models.CharField(
                        blank=True,
                        choices=[
                            ("A0", "A0"),
                            ("A1", "A1"),
                            ("A2", "A2"),
                            ("B1", "B1"),
                            ("B2", "B2"),
                            ("C1", "C1"),
                            ("C2", "C2"),
                            ("X", "Non Specifié"),
                        ],
                        default="X",
                        max_length=10,
                        null=True,
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exchange.university",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UniversityContractStudent",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contract_type",
                    models.CharField(
                        choices=[("DD", "Double Diplôme"), ("M", "Mobilité")],
                        default="X",
                        max_length=200,
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exchange.university",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="UniversityContractAdmin",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "contract_type",
                    models.CharField(
                        choices=[("DD", "Double Diplôme"), ("M", "Mobilité")],
                        default="X",
                        max_length=200,
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exchange.university",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="FinancialAid",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(blank=True, max_length=100, null=True)),
                ("amount", models.IntegerField(blank=True, default=0, null=True)),
                (
                    "received_every",
                    models.CharField(
                        blank=True,
                        choices=[("S", "Semaines"), ("M", "Mois")],
                        max_length=15,
                        null=True,
                    ),
                ),
                (
                    "exchange",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exchange.exchange",
                    ),
                ),
            ],
        ),
        migrations.CreateModel(
            name="ExchangeOffer",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                (
                    "duration",
                    models.CharField(
                        choices=[("S", "Semestre"), ("A", "Année")], max_length=200
                    ),
                ),
                ("available_places", models.IntegerField(default=0)),
                ("exclusive", models.BooleanField(default=False)),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exchange.university",
                    ),
                ),
            ],
        ),
        migrations.AddField(
            model_name="exchange",
            name="student",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="exchange.student"
            ),
        ),
        migrations.AddField(
            model_name="exchange",
            name="university",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="exchange.university"
            ),
        ),
        migrations.CreateModel(
            name="Department",
            fields=[
                (
                    "id",
                    models.AutoField(
                        auto_created=True,
                        primary_key=True,
                        serialize=False,
                        verbose_name="ID",
                    ),
                ),
                ("name", models.CharField(default="", max_length=100)),
                (
                    "rank",
                    models.IntegerField(
                        default=1,
                        help_text="Utilisez une valeur entre 1 et 5, 1 étant la plus basse et 5 la plus haute.",
                    ),
                ),
                (
                    "university",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="exchange.university",
                    ),
                ),
            ],
            options={
                "permissions": (
                    ("noter_depart", "Creer et noter un département d'une université"),
                ),
            },
        ),
        migrations.AddField(
            model_name="city",
            name="country",
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.CASCADE, to="exchange.country"
            ),
        ),
    ]