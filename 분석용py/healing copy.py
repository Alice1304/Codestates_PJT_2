import pandas as pd

data = pd.read_csv('C:/Users/tiami/Desktop/CP2/신문/news_final.csv')



# keywords = ['4차 산업혁명','nft','인공지능','AI','사물인터넷','IoT','빅데이터','Big Data','클라우드컴퓨팅', '블록체인','Block Chain', '3D프린팅','가상현실','증강현실','NFT',
# '메타버스','자율주행','코딩','버튜버','무인항공기','신소재','개발자','파이썬','머신러닝','딥러닝']

keywords = ['4차 산업혁명']


pd.set_option('display.max_rows',None)
keywords_rev_4 = pd.DataFrame()
for i in keywords:
    result = data[data['title'].str.contains(i,na=False)]
    keywords_rev_4 = pd.concat([keywords_rev_4,result])


keywords_rev_4 = keywords_rev_4.drop_duplicates(['title'])
s = keywords_rev_4.groupby('year')['title'].count()
print(s)
