from flask import Flask, request, jsonify
import requests
from datetime import datetime, timedelta

app = Flask(__name__)

# Функція для отримання курсу USD з API НБУ
def get_usd_rate(date: str):
    """
    Отримує курс USD з API НБУ на вказану дату.
    :param date: Дата у форматі YYYYMMDD
    :return: Курс USD або повідомлення про помилку
    """
    url = f"https://bank.gov.ua/NBUStatService/v1/statdirectory/exchange?valcode=USD&date={date}&json"
    try:
        response = requests.get(url)
        if response.status_code == 200 and response.json():
            data = response.json()[0]
            return {
                "currency": data['cc'],
                "rate": data['rate'],
                "date": data['exchangedate']
            }
        else:
            return {"error": "No data available for the selected date"}
    except Exception as e:
        return {"error": str(e)}

# Маршрут для отримання курсу валют
@app.route('/currency', methods=['GET'])
def currency():
    param = request.args.get('param')
    
    if param == 'today':
        today_date = datetime.now().strftime('%Y%m%d')
        rate = get_usd_rate(today_date)
        return jsonify(rate)
    
    elif param == 'yesterday':
        yesterday_date = (datetime.now() - timedelta(days=1)).strftime('%Y%m%d')
        rate = get_usd_rate(yesterday_date)
        return jsonify(rate)
    
    else:
        return jsonify({"error": "Invalid parameter. Use 'param=today' or 'param=yesterday'."})

if __name__ == '__main__':
    app.run(port=8000, debug=True)
