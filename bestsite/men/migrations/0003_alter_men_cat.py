# Generated by Django 4.1.7 on 2023-04-03 23:35

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('men', '0002_alter_men_cat'),
    ]

    operations = [
        migrations.AlterField(
            model_name='men',
            name='cat',
            field=models.ForeignKey(null=True, on_delete=django.db.models.deletion.CASCADE, to='men.category', verbose_name='Категория'),
        ),
    ]
