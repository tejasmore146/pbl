from bs4 import BeautifulSoup
import pandas as pd


# source = open("source.html", 'r')
# contents = source.read()
# soup = BeautifulSoup(contents, 'lxml')

df = pd.read_html('https://fe2022.mahacet.org/StaticPages/frmInstituteWiseAllotmentList?did=2021', extract_links='body')
# df = pd.read_html('output.html')

df = df[0]
# df.to_csv("data2.csv")


series = df["CAP-III"]
print(series[0][1])

# print(df)