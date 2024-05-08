# Generated by Django 4.2.1 on 2024-05-08 09:34

from django.db import migrations, models
import uuid


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Cake',
            fields=[
                ('cake_name', models.CharField(max_length=100)),
                ('cake_description', models.TextField()),
                ('cake_price', models.DecimalField(decimal_places=2, max_digits=10)),
                ('cake_id', models.UUIDField(default=uuid.uuid4, editable=False, primary_key=True, serialize=False)),
                ('cake_type', models.CharField(choices=[('Birthday', 'Birthday'), ('Wedding', 'Wedding'), ('Anniversary', 'Anniversary'), ('Other', 'Other')], max_length=20)),
                ('event', models.CharField(choices=[('Birthday Party', 'Birthday Party'), ('Wedding Ceremony', 'Wedding Ceremony'), ('Anniversary Celebration', 'Anniversary Celebration'), ('Other', 'Other')], max_length=30)),
            ],
        ),
    ]