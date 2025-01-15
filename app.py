from flask import Flask, render_template, request

app = Flask(__name__)

# Static dictionary for exchange rates (you can later replace this with live API data)
exchange_rates = {
    'USD': 1,
    'EUR': 0.85,
    'GBP': 0.75,
    'INR': 74.4
}

@app.route('/', methods=['GET', 'POST'])
def index():
    if request.method == 'POST':
        amount = float(request.form['amount'])
        from_currency = request.form['from_currency']
        to_currency = request.form['to_currency']

        # Convert the amount
        result = amount * exchange_rates[to_currency] / exchange_rates[from_currency]
        return render_template('index.html', result=result, amount=amount, from_currency=from_currency, to_currency=to_currency)

    return render_template('index.html')

if __name__ == '__main__':
    app.run(debug=True)
