import requests
from bs4 import BeautifulSoup



url = "https://pt.wikipedia.org/wiki/Python"

response = requests.get(url)

html = response.text

soup = BeautifulSoup(html, 'html.parser')

tables = soup.find_all('table')

i = 1

for table in tables:
    if(i == 7):
        print(f"------TABELA {i}------")
        
        with open(f"tabela_{i}", "w") as file:
            rows = table.find_all('tr')
            index = -1
            for row in rows:
                cells = row.find_all(['th', 'td'])
                if index == -1:
                    index_str = "index"
                else:
                    index_str = str(index)

                index += 1

                file.write(index_str)
                print(index_str, end="")
                
                for cell in cells:
                    cell_content = ";" + cell.get_text(strip=True)
                    file.write(cell_content)
                    print(cell_content, end="")
                file.write("\n")
                print("")

    i += 1
        