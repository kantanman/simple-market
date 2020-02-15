import data_struc
from flask import Flask, request
from buy_create import buy_create
from sell_create import sell_create
from market_create import market_create


#app = Flask(__name__)
#@app.route('/create/market', methods = ['POST'])
def create_market():
  #  Min = request.form.get('min')
  #  Max = request.form.get('max')
#  market_id = request.form.get('market_id')
    new_market = market_create(Min, Max, market_id)

#app.route('/create/buy', methods = ['POST'])
def create_buy():
   # price = request.form.get('price')
  #  quantity = request.form.get('quantity')
  #  market_id = request.form.get('market_id')
    new_buy = buy_create(price, quantity, market_id)
