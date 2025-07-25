# Generated by Django 3.2.25 on 2025-06-15 07:17

from django.conf import settings
from django.db import migrations, models
import django.db.models.deletion


class Migration(migrations.Migration):

    initial = True

    dependencies = [
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.CreateModel(
            name='Profile',
            fields=[
                ('id', models.BigAutoField(auto_created=True, primary_key=True, serialize=False, verbose_name='ID')),
                ('name', models.CharField(max_length=100)),
                ('age', models.PositiveIntegerField(blank=True, null=True)),
                ('phone', models.CharField(blank=True, max_length=15)),
                ('email', models.EmailField(max_length=254)),
                ('income', models.DecimalField(decimal_places=2, max_digits=10)),
                ('budget', models.DecimalField(decimal_places=2, max_digits=10)),
                ('savings_goal', models.DecimalField(blank=True, decimal_places=2, max_digits=10, null=True)),
                ('occupation', models.CharField(blank=True, max_length=100)),
                ('city', models.CharField(blank=True, max_length=100)),
                ('created_at', models.DateTimeField(auto_now_add=True)),
                ('user', models.OneToOneField(on_delete=django.db.models.deletion.CASCADE, to=settings.AUTH_USER_MODEL)),
            ],
        ),
    ]
