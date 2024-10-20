# Generated by Django 5.1.1 on 2024-10-02 03:17

from django.db import migrations, models


class Migration(migrations.Migration):
    dependencies = [
        ("myApp", "0001_initial"),
    ]

    operations = [
        migrations.RemoveField(
            model_name="custom_user",
            name="profile_pic",
        ),
        migrations.AddField(
            model_name="custom_user",
            name="auth_token",
            field=models.CharField(max_length=100, null=True),
        ),
        migrations.AddField(
            model_name="custom_user",
            name="created_at",
            field=models.DateTimeField(auto_now_add=True, null=True),
        ),
        migrations.AddField(
            model_name="custom_user",
            name="is_verified",
            field=models.BooleanField(default=False, null=True),
        ),
        migrations.AlterField(
            model_name="custom_user",
            name="user_type",
            field=models.CharField(
                choices=[("recruiter", "Recruiter"), ("jobseeker", "JobSeeker")],
                max_length=120,
                null=True,
            ),
        ),
    ]
