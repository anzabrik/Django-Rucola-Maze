# Generated by Django 4.2.2 on 2023-08-28 09:44

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('inventory', '0011_alter_ingredient_name_alter_menuitem_title'),
    ]

    operations = [
        migrations.AlterField(
            model_name='reciperequirement',
            name='menu_item',
            field=models.ForeignKey(on_delete=django.db.models.deletion.CASCADE, to='inventory.menuitem'),
        ),
    ]