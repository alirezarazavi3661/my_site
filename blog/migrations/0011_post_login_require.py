# Generated by Django 3.2.19 on 2023-09-04 18:02

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('blog', '0010_rename_approach_comment_approved'),
    ]

    operations = [
        migrations.AddField(
            model_name='post',
            name='login_require',
            field=models.BooleanField(default=False),
        ),
    ]
