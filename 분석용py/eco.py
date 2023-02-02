import pandas as pd

data = pd.read_csv('C:/Users/tiami/Desktop/CP2/신문/news_final.csv')



economic = ['경제','부동산','주식','펀드','종목','금리','환율','구조조정','재계','주가','보유세','대출','세금','상장','투자','재테크','고용','금융']
# '재산세','종부세','유니콘기업','상장폐지','ESG','중소기업']

#economic = ['불황','침체','경제위기','고용악화','고환율','물가상승','꺽였다','투자 리스크','해고','감원','감축','성장률 둔화','상장 폐지','상폐','금융위기','하락세','부채','가계대출']



# pd.set_option('display.max_rows',None)
keywords_eco = pd.DataFrame()
for i in economic:
    result = data[data['title'].str.contains(i,na=False)]
    keywords_eco = pd.concat([keywords_eco,result])

keywords_eco = keywords_eco.drop_duplicates(['title'])
s = keywords_eco.groupby('year')['title'].count()
print(s)