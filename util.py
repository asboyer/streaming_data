from datetime import datetime
import requests, json
from bs4 import BeautifulSoup

def make_date_string():
    today = datetime.today()
    return f'{today.month}_{today.day}_{today.year}'

def build_dictionary(url):
    r = requests.get(url)
    text = r.text
    soup = BeautifulSoup(text, 'html.parser')
    rows = soup.findAll('tr')
    
    headers = []
    header_text = rows[0].getText()
    header_text = header_text.split("\n")
    header_text[1] = ''
    header_text[-2] = ''
    for h in header_text:
        if h.strip() != "":
            headers.append(h.strip())
    
    rows.pop(0)
    
    stats = {}
    
    for i in range(0, 100):
        t = rows[i].getText()
        data = t.split("\n")
    
        data[1] = ''
        for d in range(len(data)):
            if "[" in data[d]:
                data[d] = ''
        
        info = []
        
        for d in data:
            if d.strip() != "":
                info.append(d.strip())
        
        stats[str(i + 1)] = {}
    
        for h in range(len(headers)):
            if headers[h].startswith('Streams'):
                info[h] = int(info[h].replace(',', '')) * 1000000
            else:
                info[h] = info[h].replace('"', '')
            stats[str(i + 1)][headers[h]] = info[h]
    
    
    with open(f'{make_date_string()}.json', 'w+', encoding='utf8') as file:
        file.write(json.dumps(stats, ensure_ascii=False, indent=4))

