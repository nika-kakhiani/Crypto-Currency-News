from django.shortcuts import render
import requests
import json

# Create your views here.


def home(request):
    api_request = requests.get("https://min-api.cryptocompare.com/data/v2/news/?lang=EN")
    api = json.loads(api_request.content)

    price_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=BTC,ETH,XRP,BCH,EOS,LTC,XLM,ADA,USDT,MIOTA,TRX&tsyms=USD,EUR")
    price = json.loads(price_request.content)

    context = {
        "api": api,
        "price": price,
    }
    return render(request, "home.html", context)


def prices(request):
    if request.method == "POST":
        quote = request.POST["quote"]
        quote = quote.upper()
        crypto_request = requests.get("https://min-api.cryptocompare.com/data/pricemultifull?fsyms=" + quote + "&tsyms=USD,EUR")
        crypto = json.loads(crypto_request.content)

        context = {
            "quote": quote,
            "crypto": crypto,
        }
        return render(request, "prices.html", context)
    else:
        notfound = "Enter a crypto currency symbol into the form above..."

        context = {
            "notfound": notfound,
        }
        return render(request, "prices.html", context)
