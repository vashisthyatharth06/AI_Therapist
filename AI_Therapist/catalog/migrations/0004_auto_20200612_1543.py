# Generated by Django 3.0.5 on 2020-06-12 20:43

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('catalog', '0003_calendar'),
    ]

    operations = [
        migrations.AlterField(
            model_name='calendar',
            name='mood',
            field=models.CharField(choices=[('d', 'Depressed'), ('a', 'Angry'), ('w', 'Workload'), ('s', 'Sad'), ('r', 'Relationship Problems'), ('t', 'Tensed About Past')], max_length=1),
        ),
        migrations.AlterField(
            model_name='calendar',
            name='mood_time',
            field=models.TimeField(auto_now=True),
        ),
    ]