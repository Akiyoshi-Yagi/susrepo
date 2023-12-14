# Generated by Django 4.2.7 on 2023-11-29 14:58

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0004_characternum'),
    ]

    operations = [
        migrations.AlterField(
            model_name='characternum',
            name='governance_word_count',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='characternum',
            name='indicators_word_count',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='characternum',
            name='risk_management_word_count',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='characternum',
            name='strategy_word_count',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='characternum',
            name='talent_indicators_word_count',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='characternum',
            name='talent_strategy_word_count',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
        migrations.AlterField(
            model_name='characternum',
            name='total_word_count',
            field=models.CharField(blank=True, max_length=10, null=True),
        ),
    ]
