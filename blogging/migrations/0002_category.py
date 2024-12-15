# Generated by Django 5.1.3 on 2024-11-16 18:39

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("blogging", "0001_initial"),
    ]

    operations = [
        migrations.CreateModel(
            name="Category",
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
                ("name", models.CharField(max_length=128)),
                ("description", models.TextField(blank=True)),
                (
                    "post",
                    models.ManyToManyField(
                        blank=True, related_name="catergories", to="blogging.post"
                    ),
                ),
            ],
        ),
    ]
