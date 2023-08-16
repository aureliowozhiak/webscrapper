import requests
import pandas as pd

websites = ["https://pt.wikipedia.org/wiki/Python"]

for url in websites:
    try:
        for i in range(0, 100):
            pd.read_html(url)[i].to_csv(f"tabela_{i}_pandas.csv")
    except:
        pass