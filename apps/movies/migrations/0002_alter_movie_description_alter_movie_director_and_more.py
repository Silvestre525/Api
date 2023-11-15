# Generated by Django 4.0.4 on 2023-11-15 14:03

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('movies', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='movie',
            name='description',
            field=models.TextField(db_column='description'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='director',
            field=models.CharField(db_column='director', max_length=100),
        ),
        migrations.AlterField(
            model_name='movie',
            name='rating',
            field=models.DecimalField(blank=True, db_column='rating', decimal_places=1, max_digits=3, null=True),
        ),
        migrations.AlterField(
            model_name='movie',
            name='release_date',
            field=models.DateField(db_column='release_date'),
        ),
        migrations.AlterField(
            model_name='movie',
            name='title',
            field=models.CharField(db_column='title', max_length=200),
        ),
        migrations.AlterModelTable(
            name='movie',
            table='Movies',
        ),
    ]
