# Generated by Django 5.1.2 on 2024-10-25 16:00

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('cv', '0002_remove_education_user_remove_personalinfo_user_and_more'),
    ]

    operations = [
        migrations.CreateModel(
            name='Bio',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('bio', models.TextField(blank=True, null=True)),
            ],
        ),
    ]
