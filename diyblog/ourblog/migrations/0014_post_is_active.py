# Generated by Django 4.1.2 on 2022-10-17 16:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ourblog", "0013_remove_comment_active"),
    ]

    operations = [
        migrations.AddField(
            model_name="post",
            name="is_active",
            field=models.BooleanField(default=True),
        ),
    ]
