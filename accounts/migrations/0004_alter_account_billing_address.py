# Generated by Django 4.1.2 on 2023-03-05 15:20

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('accounts', '0003_alter_account_managers_account_billing_address_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='account',
            name='billing_address',
            field=models.TextField(blank=True, max_length=600, null=True),
        ),
    ]