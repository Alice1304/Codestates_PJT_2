import pandas as pd

data = pd.read_csv('C:/Users/tiami/Desktop/CP2/신문/news_final.csv')



keywords = ['국회','대통령','장관','임기','청와대','대선','총선','진보','보수','지지율','대권','좌파','우파','자유주의','공산주의','내각','레임덕','무당파',
'의회','우경화','종북','안보','선거','사회주의','복지','민주화','정족수','좌경화','포퓰리즘','지방자치','도지사','정치']



# pd.set_option('display.max_rows',None)
empty = pd.DataFrame()
for i in keywords:
    result = data[data['title'].str.contains(i,na=False)]
    result = pd.concat([empty,result])

result = result.drop_duplicates(['title'])

s = result.groupby('year')['title'].count()
print(s)