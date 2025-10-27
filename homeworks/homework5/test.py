import requests

url = 'http://localhost:9696/predict'

client = {
    "lead_source": "organic_search",
    "number_of_courses_viewed": 4,
    "annual_income": 80304.0
}

response = requests.post(url, json=client).json()

print(response)
#if response['lead_probability'] == 'lead':
#    print('client is likely to lead')
#else:
#    print('client is not likely to lead')


