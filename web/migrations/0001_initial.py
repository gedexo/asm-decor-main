# Generated by Django 4.2.5 on 2023-11-02 07:07

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):
    initial = True

    dependencies = []

    operations = [
        migrations.CreateModel(
            name="ServiceCategory",
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
                ("name", models.CharField(max_length=30)),
                ("description", models.TextField()),
                ("slug", models.SlugField(max_length=100, unique=True)),
            ],
        ),
        migrations.CreateModel(
            name="Service",
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
                ("service_title", models.CharField(max_length=30)),
                ("service_icon", models.ImageField(upload_to="")),
                ("service_coverimage", models.ImageField(upload_to="")),
                ("service_summery", models.CharField(max_length=50)),
                ("service_description", models.TextField()),
                (
                    "slug",
                    models.SlugField(
                        blank=True, max_length=100, null=True, unique=True
                    ),
                ),
                (
                    "category",
                    models.ForeignKey(
                        on_delete=django.db.models.deletion.CASCADE,
                        to="web.servicecategory",
                    ),
                ),
            ],
        ),
    ]