# Generated by Django 5.0.6 on 2024-10-27 22:24

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("brand", "0048_alter_commentary_description1_and_more")]

    operations = [
        migrations.AddField(
            model_name="commentary",
            name="from_the_website",
            field=models.TextField(blank=True, help_text="needed for site compatibility"),
        )
    ]
