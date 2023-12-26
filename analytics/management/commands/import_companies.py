from django.core.management.base import BaseCommand
import csv
from analytics.models import Company, CharacterNum, WordRate, InputCategory
from yuhoapp.settings import BASE_DIR
import os

class Command(BaseCommand):
    help = 'Import companies from a CSV file'

    def handle(self, *args, **kwargs):
        with open(os.path.join(BASE_DIR, 'yuho_data/個別企業情報.csv'), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            n=0
            for row in reader:
                print(n)
                n+=1
                Company.objects.create(
                    stock_code = row["\ufeffstock_code"], #\ufeff　注意
                    submission_date = row["submission_date"],
                    company_name = row["company_name"],
                    industry_classification = row["industry_classification"],
                    sales_amount = row["sales_amount"],
                    sales_data_available = row["sales_data_available"],
                    sales_small = row["sales_small"],
                    sales_medium = row["sales_medium"],
                    sales_large = row["sales_large"],
                    market_product_classification = row["market_product_classification"],
                    esg_score = row["esg_score"],
                    grade_a_or_above = row["grade_a_or_above"],
                    sustainability_approach = row["sustainability_approach"],
                    # governance = row["governance"],
                    # strategy = row["strategy"],
                    # talent_development_policy = row["talent_development_policy"],
                    # risk_management = row["risk_management"],
                    # indicators_and_goals = row["indicators_and_goals"],
                    # talent_development_indicators_and_performance = row["talent_development_indicators_and_performance"],
                    total_word_count = row["total_word_count"],
                    governance_word_count = row["governance_word_count"],
                    strategy_word_count = row["strategy_word_count"],
                    talent_strategy_word_count = row["talent_strategy_word_count"],
                    risk_management_word_count = row["risk_management_word_count"],
                    indicators_word_count = row["indicators_word_count"],
                    talent_indicators_word_count = row["talent_indicators_word_count"],
                    strategy_for_value_enhancement = row["strategy_for_value_enhancement"],
                    dx_in_sustainability_context = row["dx_in_sustainability_context"],
                    sustainability_committee_established = row["sustainability_committee_established"],
                    materiality_established = row["materiality_established"],
                    supply_chain_transparency_and_efficiency = row["supply_chain_transparency_and_efficiency"],
                    climate_change_considered_in_business = row["climate_change_considered_in_business"],
                    climate_related_financial_disclosure = row["climate_related_financial_disclosure"],
                    greenhouse_gas_reduction_efforts = row["greenhouse_gas_reduction_efforts"],
                    carbon_neutral_efforts = row["carbon_neutral_efforts"],
                    scope_3_inclusion_in_analysis = row["scope_3_inclusion_in_analysis"],
                    disability_employment_efforts = row["disability_employment_efforts"],
                    engagement_survey_conducted = row["engagement_survey_conducted"],
                    internal_systems_respecting_human_rights = row["internal_systems_respecting_human_rights"],
                    diversity_respecting_hr_policy = row["diversity_respecting_hr_policy"],
                    proactive_hiring_of_female_managers = row["proactive_hiring_of_female_managers"],
                )

        with open(os.path.join(BASE_DIR, 'yuho_data/文字数.csv'), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            n=0
            for row in reader:
                print(n)
                n+=1
                CharacterNum.objects.create(
                    major_classification = row["\ufeffmajor_classification"],
                    minor_classification = row["minor_classification"],
                    company_number = row["company_number"],
                    total_word_count = row["total_word_count"],
                    governance_word_count = row["governance_word_count"],
                    strategy_word_count = row["strategy_word_count"],
                    talent_strategy_word_count = row["talent_strategy_word_count"],
                    risk_management_word_count = row["risk_management_word_count"],
                    indicators_word_count = row["indicators_word_count"],
                    talent_indicators_word_count = row["talent_indicators_word_count"],
                )

        with open(os.path.join(BASE_DIR, 'yuho_data/ワード分析.csv'), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            n=0
            for row in reader:
                print(n)
                n+=1
                WordRate.objects.create(
                    major_classification = row["\ufeffmajor_classification"],
                    minor_classification = row["minor_classification"],
                    company_number = row["company_number"],
                    filling_company = row["filling_company"],
                    filling_rate = row["filling_rate"],
                    strategy_for_value_enhancement = row["strategy_for_value_enhancement"],
                    dx_in_sustainability_context = row["dx_in_sustainability_context"],
                    sustainability_committee_established = row["sustainability_committee_established"],
                    materiality_established = row["materiality_established"],
                    supply_chain_transparency_and_efficiency = row["supply_chain_transparency_and_efficiency"],
                    climate_change_considered_in_business = row["climate_change_considered_in_business"],
                    climate_related_financial_disclosure = row["climate_related_financial_disclosure"],
                    greenhouse_gas_reduction_efforts = row["greenhouse_gas_reduction_efforts"],
                    carbon_neutral_efforts = row["carbon_neutral_efforts"],
                    scope_3_inclusion_in_analysis = row["scope_3_inclusion_in_analysis"],
                    disability_employment_efforts = row["disability_employment_efforts"],
                    engagement_survey_conducted = row["engagement_survey_conducted"],
                    internal_systems_respecting_human_rights = row["internal_systems_respecting_human_rights"],
                    diversity_respecting_hr_policy = row["diversity_respecting_hr_policy"],
                    proactive_hiring_of_female_managers = row["proactive_hiring_of_female_managers"],
                )
        with open(os.path.join(BASE_DIR, 'yuho_data/入力フォームカテゴリー.csv'), newline='') as csvfile:
            reader = csv.DictReader(csvfile)
            n=0
            for row in reader:
                print(n)
                n+=1
                InputCategory.objects.create(
                    industry = row["\ufeffindustry"],
                    heading = row["heading"],
                    category1 = row["category1"],
                    category2 = row["category2"],
                    category3 = row["category3"],
                    category4 = row["category4"],
                    category5 = row["category5"],
                    default_sentence = row["default_sentence"],
                )