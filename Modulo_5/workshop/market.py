import requests

url = 'http://localhost:9696/predict'

customer = {
  "gender": "male",
  "seniorcitizen": 0,
  "partner": "no",
  "dependents": "yes",
  "phoneservice": "no",
  "multiplelines": "no_phone_service",
  "internetservice": "dsl",
  "onlinesecurity": "no",
  "onlinebackup": "yes",
  "deviceprotection": "no",
  "techsupport": "no",
  "streamingtv": "no",
  "streamingmovies": "no",
  "contract": "month-to-month",
  "paperlessbilling": "yes",
  "paymentmethod": "electronic_check",
  "tenure": 6,
  "monthlycharges": 29.85,
  "totalcharges": 129.85
}

response = requests.post(url, json=customer)
churn = response.json()

print('response: ', churn)

if churn['churn'] >= 0.5:
    print(f' {churn}, send retention offer')   
else:
    print(f'The customer will stay with probability {1 - churn}')