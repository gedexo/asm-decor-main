# Generated by Django 4.2.7 on 2023-11-10 11:51

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('web', '0008_alter_client_options'),
    ]

    operations = [
        migrations.AddField(
            model_name='servicecategory',
            name='order',
            field=models.PositiveIntegerField(blank=True, null=True),
        ),
    ]