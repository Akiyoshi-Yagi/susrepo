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
    print("get_settings")
    print(settings)
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

    if request.method == 'POST':
        set_industry = request.POST.get('set_industry')

        response_dict['section1'] = InputCategory.objects.filter(industry__icontains=set_industry)[0]
        response_dict['section2'] = InputCategory.objects.filter(industry__icontains=set_industry)[1]
        response_dict['section3'] = InputCategory.objects.filter(industry__icontains=set_industry)[2]
        response_dict['section4'] = InputCategory.objects.filter(industry__icontains=set_industry)[3]
        response_dict['section5'] = InputCategory.objects.filter(industry__icontains=set_industry)[4]
        response_dict['section6'] = InputCategory.objects.filter(industry__icontains=set_industry)[5]

        for i in range(1,7):

            if "generation"+str(i) in request.POST:

                for j in range(1,7):
                    if i == j:
                        openai.api_key = settings.OPENAI_API_KEY

                        category_1 = request.POST.get('category'+str(i)+'_1')
                        category_2 = request.POST.get('category'+str(i)+'_2')
                        category_3 = request.POST.get('category'+str(i)+'_3')
                        category_4 = request.POST.get('category'+str(i)+'_4')
                        category_5 = request.POST.get('category'+str(i)+'_5')

                        section =  InputCategory.objects.filter(industry__icontains=set_industry)[i-1]

                        prompt = f"あなたは企業の有価証券報告書作成のエキスパートである。{section.industry}に属するとある企業XXX社の有価証券報告書のサステナビリティの章の{section.heading}の項目の文章を生成してください。次の条件を満たしてください。1. 項目分けせずに、一つなぎの文章で生成してください。2. 800字以上1000字以下でお願いします。3. 「当社は、〜。{section.category1}においては〜。{section.category2}に関しては〜。{section.category3}においては〜。{section.category4}に関しては〜。{section.category5}には〜。」という文章フレームで書いてください。4. 文章の内容は、{section.category1}:{category_1}。{section.category2}:{category_2}。{section.category3}:{category_3}。{section.category4}:{category_4}。{section.category5}:{category_5}。をもとにかく。これ以外の嘘の内容を書いてはいけない。"

                        response = openai.ChatCompletion.create(
                            model="gpt-4-1106-preview",
                            messages=[
                                {"role": "user", "content": prompt}
                                ])


                        response_dict["response_sentence_"+str(j)] = response['choices'][0]['message']['content']
                    else:
                        response_dict["response_sentence_"+str(j)] = request.POST.get('category'+str(j)+'_6')
                return render(request, 'generation.html' , response_dict)
        return render(request, 'generation.html', response_dict)

    # GETリクエストの場合、またはフォームが正しく送信されなかった場合
    return render(request, 'generation.html', response_dict)

        # データを結合
        # initial_sentence = "あなたは" + "小売業界" + "の企業の有価証券報告書の担当者です。以下の内容に沿って、有価証券報告書のサステナビリティ欄の" + "指標及び目標" + "に記載する文章を作成してください。"
        # combined_data = initial_sentence + f"{category1}\n{category2}\n{category3}\n{category4}\n{category5}\n{category6}"

        # APIにデータを送信し、レスポンスを受け取る
        # api_url = 'あなたのAPIのURL'
        # response = requests.post(api_url, data={'combined_data': combined_data})

        # # APIからのレスポンスを処理（例: JSON形式のレスポンスを想定）
        # if response.status_code == 200:
        #     response_data = response.json()
        #     # 必要に応じてレスポンスデータを処理

        #     # 結果をテンプレートに渡す
        #     return render(request, 'generation.html', {'response_data': response_data})

