# Generated by Django 4.1.2 on 2022-10-19 22:23

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ourblog", "0022_alter_comment_is_active"),
    ]

    operations = [
        migrations.AlterField(
            model_name="comment",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
