# Generated by Django 4.2.9 on 2024-01-19 21:05

from django.db import migrations, models


class Migration(migrations.Migration):

    initial = True

    dependencies = [
    ]

    operations = [
        migrations.CreateModel(
            name='Booking',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=255)),
                ('phone_number', models.CharField(max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('service_type', models.CharField(choices=[('haircut', 'Haircut'), ('coloring', 'Coloring'), ('styling', 'Styling')], max_length=20)),
                ('notes', models.TextField(blank=True, null=True)),
                ('date_preference', models.DateField()),
                ('time_preference', models.TimeField()),
                ('created_at', models.DateTimeField(auto_now_add=True)),
            ],
        ),
    ]
