# Generated by Django 5.0.6 on 2024-10-23 04:31

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [("brand", "0047_rename_summary_commentary_description1_and_more")]

    operations = [
        migrations.AlterField(
            model_name="commentary",
            name="description1",
            field=models.TextField(
                blank=True,
                help_text="Formerly summary, shown on the bank page in the first section.",
            ),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="description2",
            field=models.TextField(
                blank=True,
                help_text="Formerly details, shown on the bank page in the second section.",
            ),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="description3",
            field=models.TextField(
                blank=True,
                help_text="formerly from_the_website, shown on the bank page in the third section.",
            ),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="headline",
            field=models.TextField(
                blank=True,
                help_text="Formerly header, shown on the bank page in the first section.",
            ),
        ),
        migrations.AlterField(
            model_name="commentary",
            name="subtitle",
            field=models.TextField(blank=True, help_text="subtitle shown on bank pages."),
        ),
    ]
