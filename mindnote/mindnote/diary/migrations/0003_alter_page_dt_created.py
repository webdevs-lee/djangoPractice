# Generated by Django 4.0.5 on 2024-05-13 02:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('diary', '0002_alter_page_dt_created'),
    ]

    operations = [
        migrations.AlterField(
            model_name='page',
            name='dt_created',
            field=models.DateField(auto_now_add=True, verbose_name='Date Created'),
        ),
    ]