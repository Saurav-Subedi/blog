# Generated by Django 4.2.4 on 2023-09-07 07:50

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("base", "0005_remove_post_content_remove_post_title_post_name_and_more"),
    ]

    operations = [
        migrations.AlterField(
            model_name="post",
            name="name",
            field=models.CharField(max_length=100),
        ),
    ]
