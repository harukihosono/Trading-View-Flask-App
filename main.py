import json
import os
from flask import Flask, jsonify, request, render_template
from flask_httpauth import HTTPBasicAuth

app = Flask(__name__)
auth = HTTPBasicAuth()
path = os.path.join(os.path.dirname(__file__), 'settings.json')
settings_file = path

# JSONファイルからTradingBot設定を読み込む
with open(settings_file, 'r') as f:
    settings = json.load(f)

# TradingBot設定を保存する関数
def save_settings(settings):
    with open(settings_file, 'w') as f:
        json.dump(settings, f)

# 認証関数
@auth.verify_password
def verify_password(username, password):
    if username == 'admin' and password == '0000':
        return True
    else:
        return False

# TradingBot設定を変更するエンドポイント
@app.route('/settings', methods=['POST'])
@auth.login_required
def set_settings():
    api_key = request.form['api_key']
    api_secret = request.form['api_secret']
    amount = request.form['amount']
    currency_pair = request.form['currency_pair']
    settings['api_key'] = api_key
    settings['api_secret'] = api_secret
    settings['amount'] = amount
    settings['currency_pair'] = currency_pair
    save_settings(settings)
    return jsonify({'api_key': api_key, 'api_secret': api_secret, 'amount': amount, 'currency_pair': currency_pair})

# HTMLをレンダリングするエンドポイント
@app.route('/')
@auth.login_required
def index():
    api_key = settings['api_key']
    api_secret = settings['api_secret']
    amount = settings['amount']
    currency_pair = settings['currency_pair']
    return render_template('index.html', api_key=api_key, api_secret=api_secret, amount=amount, currency_pair=currency_pair)

@app.route('/', methods=['POST'])
def order():
    data = request.get_json()
    side = data['side']
    comment = data['comment']
    # ここで必要な処理を実行
    return 'OK'

if __name__ == '__main__':
    app.run(debug=True)