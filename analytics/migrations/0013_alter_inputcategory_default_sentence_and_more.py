# Generated by Django 5.0 on 2023-12-28 10:54

from django.db import migrations, models


class Migration(migrations.Migration):

    dependencies = [
        ('analytics', '0012_alter_characternum_governance_word_count_and_more'),
    ]

    operations = [
        migrations.AlterField(
            model_name='inputcategory',
            name='default_sentence',
            field=models.TextField(blank=True, null=True),
        ),
        migrations.AlterField(
            model_name='inputcategory',
            name='heading',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='inputcategory',
            name='industry',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='carbon_neutral_efforts',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='climate_change_considered_in_business',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='climate_related_financial_disclosure',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='company_number',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='disability_employment_efforts',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='diversity_respecting_hr_policy',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='dx_in_sustainability_context',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='engagement_survey_conducted',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='filling_company',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='filling_rate',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='greenhouse_gas_reduction_efforts',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='internal_systems_respecting_human_rights',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='major_classification',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='materiality_established',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='minor_classification',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='proactive_hiring_of_female_managers',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='scope_3_inclusion_in_analysis',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='strategy_for_value_enhancement',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='supply_chain_transparency_and_efficiency',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
        migrations.AlterField(
            model_name='wordrate',
            name='sustainability_committee_established',
            field=models.CharField(blank=True, max_length=20, null=True),
        ),
    ]
