# Generated by Django 3.2.23 on 2024-08-15 20:06

from django.db import migrations
import sortedm2m.fields


class Migration(migrations.Migration):

    dependencies = [
        ('database', '0001_initial'),
    ]

    operations = [
        migrations.AlterField(
            model_name='grade',
            name='subjects',
            field=sortedm2m.fields.SortedManyToManyField(help_text=None, related_name='subjects', to='database.Subject'),
        ),
    ]
