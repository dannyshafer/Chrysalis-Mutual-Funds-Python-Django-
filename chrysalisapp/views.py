from django.shortcuts import render
from django.http import HttpResponse
from yahoo_finance import Share
from models import HistoricalData, Stock
import urllib2
# Create your views here.
def index(request):
  return render(request, "home.html")

def stock_summary(request, symbol=None):
    if symbol == None:
        symbol = request.POST['symbol']

    current_stock = Stock()
    stock = Share(symbol)
    current_stock.symbol = symbol.upper()
    current_stock.price = stock.get_price()
    current_stock.change = stock.get_change()
    current_stock.volume = stock.get_volume()
    current_stock.prev_close = stock.get_prev_close()
    current_stock.stock_open = stock.get_open()
    current_stock.avg_daily_volume = stock.get_avg_daily_volume()
    current_stock.stock_exchange = stock.get_stock_exchange()
    current_stock.market_cap = stock.get_market_cap()
    current_stock.book_value = stock.get_book_value()
    current_stock.ebitda = stock.get_ebitda()
    current_stock.dividend_share = stock.get_dividend_share()
    current_stock.dividend_yield = stock.get_dividend_yield()
    current_stock.earnings_share = stock.get_earnings_share()
    current_stock.days_high = stock.get_days_high()
    current_stock.days_low = stock.get_days_low()
    current_stock.year_high = stock.get_year_high()
    current_stock.year_low = stock.get_year_low()
    current_stock.fifty_day_moving_avg = stock.get_50day_moving_avg()
    current_stock.two_hundred_day_moving_avg = stock.get_200day_moving_avg()
    current_stock.price_earnings_ratio = stock.get_price_earnings_ratio()
    current_stock.price_earnings_growth_ratio = stock.get_price_earnings_growth_ratio()
    current_stock.price_sales = stock.get_price_sales()
    current_stock.price_book = stock.get_price_book()
    current_stock.short_ratio = stock.get_short_ratio()

    date_metrics = []
    url = 'http://chartapi.finance.yahoo.com/instrument/1.0/'+symbol+'/chartdata;type=quote;range=1y/csv'
    page = urllib2.urlopen(url).read()
    pagebreaks = page.split('\n')
    for line in pagebreaks:
        items = line.split(',')
        if 'Company-Name:' in line:
            current_stock.company_name = line[13:len(line)]
            current_stock.save()
        if 'values' not in items:
            if len(items)==6:
                hd = HistoricalData(
                    stock_id = Stock.objects.get(id=int(current_stock.id)).id,
                    date = items[0][4:6]+'/'+items[0][6:9]+'/'+items[0][0:4],
                    close = items[1][0:(len(items[1])-2)],
                    high = items[2][0:(len(items[2])-2)],
                    price_open = items[3][0:(len(items[3])-2)],
                    low = items[4][0:(len(items[4])-2)],
                    volume = items[5][0:-6]+","+items[5][-6:-3]+","+items[5][-3:len(items[5])])
                hd.save()
                date_metrics.append(hd)
    del date_metrics[0]
    return render(request, "stock_summary.html", {'current_stock': current_stock, 'date_metrics': date_metrics})





