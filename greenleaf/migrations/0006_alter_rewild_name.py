# Generated by Django 3.2.6 on 2021-09-03 13:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('greenleaf', '0005_alter_rewild_name'),
    ]

    operations = [
        migrations.AlterField(
            model_name='rewild',
            name='name',
            field=models.CharField(max_length=50),
        ),
    ]