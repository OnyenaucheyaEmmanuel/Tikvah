# Generated by Django 5.1.5 on 2025-02-04 11:04

from django.conf import settings
from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('transaction', '0002_dailyprofit'),
        migrations.swappable_dependency(settings.AUTH_USER_MODEL),
    ]

    operations = [
        migrations.AlterUniqueTogether(
            name='dailyprofit',
            unique_together=set(),
        ),
        migrations.AddConstraint(
            model_name='dailyprofit',
            constraint=models.UniqueConstraint(fields=('date', 'user'), name='unique_daily_profit_per_user'),
        ),
        migrations.RemoveField(
            model_name='dailyprofit',
            name='total_profit',
        ),
    ]
