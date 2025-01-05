import requests
import pandas as pd
import matplotlib.pyplot as plt
from datetime import datetime, timedelta

# api
BASE_URL = "https://bank.gov.ua/NBU_Exchange/exchange_site"
VALCODE = "usd"
SORT = "exchangedate"
ORDER = "desc"
FORMAT = "json"

# time calculating
endDate = datetime.now().date()
startDate = endDate - timedelta(days=7)

start = startDate.strftime('%Y%m%d')
end = endDate.strftime('%Y%m%d')

# request cooking
url = f"{BASE_URL}?start={start}&end={end}&valcode={VALCODE}&sort={SORT}&order={ORDER}&{FORMAT}"

# request 
response = requests.get(url)

if response.status_code == 200:
    data = response.json()
    if data:
        # table formatting
        table = pd.DataFrame(data)
        print(table[['exchangedate', 'cc', 'rate']])
        
        # plot data
        table['exchangedate'] = pd.to_datetime(table['exchangedate'], format='%d.%m.%Y')
        table = table.sort_values('exchangedate')
        plt.figure(figsize=(10, 6))
        plt.plot(table['exchangedate'], table['rate'], marker='o')
        plt.title(' usd rate changing')
        plt.xlabel('date')
        plt.ylabel('UAH')
        plt.xticks(rotation=45)
        plt.grid(True)
        plt.show()
    else:
        print("there is no data for this time")
else:
    print(f"request fail: {response.status_code}")
