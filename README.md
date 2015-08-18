# Chrysalis-Mutual-Funds (Python-Django version)

First of all, a demonstration on <a href="https://www.youtube.com/watch?v=tIop2Y_w7M4">Youtube</a>. This is a modified version of my <a href="https://github.com/dannyshafer/ChrysalisApp-final-Sinatra-version-">Sinatra app</a> except implemented in Python/Django and analyzing stocks rather than mutual funds...and consuming an api rather than manually scraping Yahoo Finance. 

Ensure that you have Python 2.7, Django1.8.3, and this external module, <a href="https://pypi.python.org/pypi/yahoo-finance/1.1.4">Yahoo Finance</a>, installed. 

1. Clone from Github
2. Make migration by running "python manage.py migrate"
3. Start the server with "python manage.py runserver"
4. Navigate in your browser to port 8000 unless otherwise specified by your terminal
5. Enter a symbol and enjoy the ride. 

It would be neat in the future to add the ability to display the time-serues data in a graph format or in some way conducive to finding trends. Other possible functionality might be comparing stocks with each other both in performance and across fundamental metrics (i.e. EPS growth over time, performance versus broader stock market, etc). If you have ideas for improvement, feel free to submit a pull request.
