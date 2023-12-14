from django.db import models

# class Company(models.Model):
#     name = models.CharField(max_length=100)  # 企業名
#     industry = models.CharField(max_length=100)  # 業界
#     revenue = models.DecimalField(max_digits=10, decimal_places=2)  # 売上高

#     def __str__(self):
#         return self.name



class Company(models.Model):
    stock_code = models.CharField(max_length=10, blank=True, null=True)
    submission_date = models.DateField(blank=True, null=True)
    company_name = models.CharField(max_length=100)
    industry_classification = models.CharField(max_length=50, blank=True, null=True)
    sales_amount = models.CharField(max_length=10, blank=True, null=True)
    sales_data_available = models.BooleanField(blank=True, null=True)
    sales_small = models.BooleanField(blank=True, null=True)
    sales_medium = models.BooleanField(blank=True, null=True)
    sales_large = models.BooleanField(blank=True, null=True)
    market_product_classification = models.CharField(max_length=50, blank=True, null=True)
    esg_score = models.CharField(max_length=10, blank=True, null=True)
    grade_a_or_above = models.BooleanField(blank=True, null=True)
    # sustainability_approach = models.TextField(blank=True, null=True)
    # governance = models.TextField(blank=True, null=True)
    # strategy = models.TextField(blank=True, null=True)
    # talent_development_policy = models.TextField(blank=True, null=True)
    # risk_management = models.TextField(blank=True, null=True)
    # indicators_and_goals = models.TextField(blank=True, null=True)
    # talent_development_indicators_and_performance = models.TextField(blank=True, null=True)
    total_word_count = models.IntegerField(blank=True, null=True)
    governance_word_count = models.IntegerField(blank=True, null=True)
    strategy_word_count = models.IntegerField(blank=True, null=True)
    talent_strategy_word_count = models.IntegerField(blank=True, null=True)
    risk_management_word_count = models.IntegerField(blank=True, null=True)
    indicators_word_count = models.IntegerField(blank=True, null=True)
    talent_indicators_word_count = models.IntegerField(blank=True, null=True)
    strategy_for_value_enhancement = models.BooleanField(blank=True, null=True)
    dx_in_sustainability_context = models.BooleanField(blank=True, null=True)
    sustainability_committee_established = models.BooleanField(blank=True, null=True)
    materiality_established = models.BooleanField(blank=True, null=True)
    supply_chain_transparency_and_efficiency = models.BooleanField(blank=True, null=True)
    climate_change_considered_in_business = models.BooleanField(blank=True, null=True)
    climate_related_financial_disclosure = models.BooleanField(blank=True, null=True)
    greenhouse_gas_reduction_efforts = models.BooleanField(blank=True, null=True)
    carbon_neutral_efforts = models.BooleanField(blank=True, null=True)
    scope_3_inclusion_in_analysis = models.BooleanField(blank=True, null=True)
    disability_employment_efforts = models.BooleanField(blank=True, null=True)
    engagement_survey_conducted = models.BooleanField(blank=True, null=True)
    internal_systems_respecting_human_rights = models.BooleanField(blank=True, null=True)
    diversity_respecting_hr_policy = models.BooleanField(blank=True, null=True)
    proactive_hiring_of_female_managers = models.BooleanField(blank=True, null=True)

    def __str__(self):
        return self.company_name


class CharacterNum(models.Model):
    major_classification = models.CharField(max_length=10, blank=True, null=True)
    minor_classification = models.CharField(max_length=10, blank=True, null=True)
    company_number = models.IntegerField(blank=True, null=True)
    total_word_count = models.CharField(max_length=10, blank=True, null=True)
    governance_word_count = models.CharField(max_length=10, blank=True, null=True)
    strategy_word_count = models.CharField(max_length=10, blank=True, null=True)
    talent_strategy_word_count = models.CharField(max_length=10, blank=True, null=True)
    risk_management_word_count = models.CharField(max_length=10, blank=True, null=True)
    indicators_word_count = models.CharField(max_length=10, blank=True, null=True)
    talent_indicators_word_count = models.CharField(max_length=10, blank=True, null=True)
    
    def __str__(self):
        return self.major_classification

class WordRate(models.Model):
    major_classification = models.CharField(max_length=10, blank=True, null=True)
    minor_classification = models.CharField(max_length=10, blank=True, null=True)
    company_number = models.CharField(max_length=10, blank=True, null=True)
    filling_company = models.CharField(max_length=10, blank=True, null=True)
    filling_rate = models.CharField(max_length=10, blank=True, null=True)
    strategy_for_value_enhancement = models.CharField(max_length=10, blank=True, null=True)
    dx_in_sustainability_context = models.CharField(max_length=10, blank=True, null=True)
    sustainability_committee_established = models.CharField(max_length=10, blank=True, null=True)
    materiality_established = models.CharField(max_length=10, blank=True, null=True)
    supply_chain_transparency_and_efficiency = models.CharField(max_length=10, blank=True, null=True)
    climate_change_considered_in_business = models.CharField(max_length=10, blank=True, null=True)
    climate_related_financial_disclosure = models.CharField(max_length=10, blank=True, null=True)
    greenhouse_gas_reduction_efforts = models.CharField(max_length=10, blank=True, null=True)
    carbon_neutral_efforts = models.CharField(max_length=10, blank=True, null=True)
    scope_3_inclusion_in_analysis = models.CharField(max_length=10, blank=True, null=True)
    disability_employment_efforts = models.CharField(max_length=10, blank=True, null=True)
    engagement_survey_conducted = models.CharField(max_length=10, blank=True, null=True)
    internal_systems_respecting_human_rights = models.CharField(max_length=10, blank=True, null=True)
    diversity_respecting_hr_policy = models.CharField(max_length=10, blank=True, null=True)
    proactive_hiring_of_female_managers = models.CharField(max_length=10, blank=True, null=True)

    
    def __str__(self):
        return self.major_classification

class InputCategory(models.Model):
    industry = models.CharField(max_length=15, blank=True, null=True)
    heading = models.CharField(max_length=15, blank=True, null=True)
    category1 = models.CharField(max_length=20, blank=True, null=True)
    category2 = models.CharField(max_length=20, blank=True, null=True)
    category3 = models.CharField(max_length=20, blank=True, null=True)
    category4 = models.CharField(max_length=20, blank=True, null=True)
    category5 = models.CharField(max_length=20, blank=True, null=True)
    default_sentence = models.CharField(max_length=1000, blank=True, null=True)
    
    def __str__(self):
        return self.industry