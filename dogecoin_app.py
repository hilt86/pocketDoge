from flask import Flask, render_template, request
import requests

app = Flask(__name__)


addresses = {
    'KidASave': 'dogeAddress',
    'KidASpend': 'dogeAddress',
    'KidAGive': 'dogeAddress',
    'KidBSpend': 'dogeAddress',
    'KidBGive': 'dogeAddress',
    'KidBSave': 'dogeAddress',
    'KidCSpend': 'dogeAddress',
    'KidCSave': 'dogeAddress',
    'KidCGive': 'dogeAddress'
}

@app.route('/', methods=['GET', 'POST'])
def index():
    balances = {}
    for name, address in addresses.items():
        api_url = f'https://dogechain.info/api/v1/address/balance/{address}'
        response = requests.get(api_url)
        if response.status_code == 200:
            data = response.json()
            balances[name] = {
                'address': address,
                'balance': data['balance']
            }
        else:
            balances[name] = {
                'address': address,
                'balance': 'Error fetching data'
            }
    
    return render_template('index.html', balances=balances)

if __name__ == '__main__':
    app.run(host='0.0.0.0', port=5000)

