from django.shortcuts import redirect, get_object_or_404, render
from django.urls import reverse
from .models import Company, CharacterNum, WordRate, InputCategory
from django.http import JsonResponse
from django.contrib import messages


import json
from authlib.integrations.django_client import OAuth
from django.conf import settings
from urllib.parse import quote_plus, urlencode

oauth = OAuth()

oauth.register(
    "auth0",
    client_id=settings.AUTH0_CLIENT_ID,
    client_secret=settings.AUTH0_CLIENT_SECRET,
    client_kwargs={
        "scope": "openid profile email",
    },
    server_metadata_url=f"https://{settings.AUTH0_DOMAIN}/.well-known/openid-configuration",
)

#ログインまわり
def login(request):
    return oauth.auth0.authorize_redirect(
        request, request.build_absolute_uri(reverse("callback"))
    )

# 👆 We're continuing from the steps above. Append this to your webappexample/views.py file.
def callback(request):
    token = oauth.auth0.authorize_access_token(request)
    request.session["user"] = token
    print("sessionを付与しました")
    return redirect(request.build_absolute_uri(reverse("search")))

def logout(request):
    request.session.clear()
    messages.add_message(request, messages.INFO, 'ログアウトしました。')
    return redirect(
        f"https://{settings.AUTH0_DOMAIN}/v2/logout?"
        + urlencode(
            {
                "returnTo": request.build_absolute_uri(reverse("search")),
                "client_id": settings.AUTH0_CLIENT_ID,
            },
            quote_via=quote_plus,
        ),
    )

def search_view(request):

    query = request.GET.get('q', '')

    if query:
        companies = Company.objects.filter(company_name__icontains=query)
        if companies.count() == 1:  # 一致する企業が1つだけ見つかった場合
            return redirect(reverse('company_detail', args=[companies.first().id]))
    else:
        companies = Company.objects.none()

    return render(request, 'search.html',
            context={
                'companies': companies,
                "session": request.session.get("user"),
                "pretty": json.dumps(request.session.get("user"), indent=4),
            }
        )


def company_detail(request, id):
    company = get_object_or_404(Company, pk=id)

    cn_sale_l = CharacterNum.objects.filter(major_classification="売上大", minor_classification=company.industry_classification).first()
    cn_sale_m = CharacterNum.objects.filter(major_classification="売上中", minor_classification=company.industry_classification).first()
    cn_sale_s = CharacterNum.objects.filter(major_classification="売上小", minor_classification=company.industry_classification).first()
    cn_esg_score = CharacterNum.objects.filter(major_classification="MSCIスコアA以上", minor_classification=company.industry_classification).first()

    wr_sale_l = WordRate.objects.filter(major_classification="売上大", minor_classification=company.industry_classification).first()
    wr_sale_m = WordRate.objects.filter(major_classification="売上中", minor_classification=company.industry_classification).first()
    wr_sale_s = WordRate.objects.filter(major_classification="売上小", minor_classification=company.industry_classification).first()
    wr_esg_score = WordRate.objects.filter(major_classification="MSCIスコアA以上", minor_classification=company.industry_classification).first()

    return render(request, 'company_detail.html',
    {
        'company': company,
        "cn_sale_l": cn_sale_l,  "cn_sale_m": cn_sale_m,  "cn_sale_s": cn_sale_s,  "cn_esg_score": cn_esg_score,
        "wr_sale_l": wr_sale_l,  "wr_sale_m": wr_sale_m,  "wr_sale_s": wr_sale_s,  "wr_esg_score": wr_esg_score,
        "session": request.session.get("user"),
        "pretty": json.dumps(request.session.get("user"), indent=4),
    })

def sentence_example(request):
    keyword = request.GET.get("keyword")
    industry = request.GET.get("industry")
    example_company1 = Company.objects.filter(sustainability_approach__icontains=keyword, industry_classification__icontains=industry, sales_large=1)[0]
    example_company2 = Company.objects.filter(sustainability_approach__icontains=keyword, industry_classification__icontains=industry, sales_large=1)[1]

    return render(request, 'sentenceexample.html',
        context={
            'keyword': keyword,
            "industry":industry,
            "example_company1":example_company1,
            "example_company2":example_company2,
            "session": request.session.get("user"),
            "pretty": json.dumps(request.session.get("user"), indent=4),
        }
    )

def get_settings(request):
    industry = request.GET.get('industry')
    settings = InputCategory.objects.filter(industry__icontains=industry).values('heading','category1','category2','category3','category4','category5',"default_sentence")
    return JsonResponse({'settings': list(settings)})

def generate_sentence(request):
    industries = InputCategory.objects.values_list('industry', flat=True).distinct()

    response_dict = {'industries': industries, "session": request.session.get("user"), "pretty": json.dumps(request.session.get("user"), indent=4),}

    response_dict['section1'] = InputCategory.objects.filter(industry__icontains="小売")[0]
    response_dict['section2'] = InputCategory.objects.filter(industry__icontains="小売")[1]
    response_dict['section3'] = InputCategory.objects.filter(industry__icontains="小売")[2]
    response_dict['section4'] = InputCategory.objects.filter(industry__icontains="小売")[3]
    response_dict['section5'] = InputCategory.objects.filter(industry__icontains="小売")[4]
    response_dict['section6'] = InputCategory.objects.filter(industry__icontains="小売")[5]

    return render(request, 'generation.html', response_dict)
