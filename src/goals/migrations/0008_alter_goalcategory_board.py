# Generated by Django 4.1.1 on 2022-10-10 08:21

from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    dependencies = [
        ('goals', '0007_create_new_objects'),
    ]

    operations = [
        migrations.AlterField(
            model_name='goalcategory',
            name='board',
            field=models.ForeignKey(
                on_delete=django.db.models.deletion.PROTECT,
                related_name='categories',
                to='goals.board',
                verbose_name='Доска',
            ),
        ),
    ]
