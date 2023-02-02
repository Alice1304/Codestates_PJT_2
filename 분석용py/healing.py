import pandas as pd

data = pd.read_csv('C:/Users/tiami/Desktop/CP2/신문/news_final.csv')



keywords = ['힐링','마음챙김','치유','우울증','테라피','멘탈','심리','상담','정신건강','자살','스트레스','자존감','명상','멘탈','심신','공감','불면증','내면','자아','희망']
not_keywords = ['힐링캠프','김상중']



pd.set_option('display.max_rows',None)
empty = pd.DataFrame()
for i in keywords:
    result = data[data['title'].str.contains(i,na=False)]
    for j in not_keywords:
        result = result[~result['title'].str.contains(j, na=False)]
        result = result[~result['title'].str.contains('\'힐링\'', na=False)]
        result = pd.concat([empty,result])
        print(keywords_healing)

result = result.drop_duplicates(['title'])

s = result.groupby('year')['title'].count()
print(s)