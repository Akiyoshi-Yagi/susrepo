from .models import Company, CharacterNum, WordRate, InputCategory
import openai
import pandas as pd


all_category = InputCategory.objects.all()
df = pd.DataFrame(columns=['Column1', 'Column2','Column3'])
i=0
for category in all_category[79:]:
    print(i)
    i +=1
    industry = category.industry
    heading = category.heading
    category1 = category.category1
    category2 = category.category2
    category3 = category.category3
    category4 = category.category4
    category5 = category.category5
    
    prompt = f"あなたは企業の有価証券報告書作成のエキスパートである。{industry}に属するとある企業XXX社の有価証券報告書のサステナビリティの章の{heading}の項目の文章を生成してください。次の条件を満たしてください。1. 項目分けせずに、一つなぎの文章で生成してください。2. 分量は800字以上1000字以下。3. 「当社は、〜。（改行）{category1}においては〜。（改行）{category2}に関しては〜。（改行）{category3}においては〜。（改行）{category4}に関しては〜。（改行）{category5}には〜。」という文章フレームで記述。4. 文章の内容は架空の定量データや固有名詞を積極的に使いできるだけ具体的に記述する。例えば女性の管理職率20%達成、2030年までにCO2排出量100%削減を目標した「NCM（Non Co2 Movement)」、などのような具体的な数値や戦略名称を利用。 5. 業界の特色がよく表現されるような戦略や目標設定をしてください。"
    
    response = openai.ChatCompletion.create(
        model="gpt-4-1106-preview",
        messages=[
    {"role": "user", "content": prompt}
    ])

    print(response['choices'][0]['message']['content'])

    data = pd.DataFrame({'Column1': [industry], 'Column2': [heading], 'Column3': [response['choices'][0]['message']['content']]})
    df = pd.concat([df, data])
    df.to_excel('output4.xlsx', index=False)



                        

