# Generated by Django 4.1.2 on 2022-10-10 10:17

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ("ourblog", "0002_rename_comments_comment"),
    ]

    operations = [
        migrations.AddField(
            model_name="author",
            name="slug",
            field=models.SlugField(default=2),
            preserve_default=False,
        ),
    ]
