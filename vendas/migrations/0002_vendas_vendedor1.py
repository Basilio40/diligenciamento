# Generated by Django 3.2.3 on 2021-05-28 04:22

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('vendas', '0001_initial'),
    ]

    operations = [
        migrations.AddField(
            model_name='vendas',
            name='vendedor1',
            field=models.CharField(blank=True, max_length=200, null=True),
        ),
    ]