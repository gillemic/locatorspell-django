# Generated by Django 4.2.2 on 2023-06-05 21:15

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('events', '0003_alter_event_category_alter_event_charity_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='event',
            name='category',
            field=models.CharField(blank=True, default='None', max_length=10),
        ),
        migrations.AlterField(
            model_name='event',
            name='charity',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='promoted',
            field=models.BooleanField(blank=True, default=False),
        ),
        migrations.AlterField(
            model_name='event',
            name='url',
            field=models.CharField(blank=True, default='', max_length=100),
        ),
    ]
