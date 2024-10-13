# Generated by Django 5.0.9 on 2024-10-10 18:44

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Event',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('event_type', models.CharField(choices=[('WORKSHOP', 'WORKSHOP'), ('CONFERENCE', 'CONFERENCE'), ('HACKATHON', 'HACKATHON')], max_length=50)),
                ('description', models.TextField(null=True)),
            ],
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.UniqueConstraint(fields=('event_type',), name='unique_event_type'),
        ),
        migrations.AddConstraint(
            model_name='event',
            constraint=models.CheckConstraint(check=models.Q(('event_type__in', ['WORKSHOP', 'CONFERENCE', 'HACKATHON'])), name='valid_event_type'),
        ),
    ]
