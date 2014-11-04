# -*- coding: utf-8 -*-
"""
Created on Mon Oct 27 11:31:56 2014

@author: francescocorea
"""

from __future__ import print_function 
import numpy as np
import matplotlib.mlab as mlab
import matplotlib.cbook as cbook
import matplotlib.ticker as ticker
import datetime
import matplotlib.finance as finance
from matplotlib.pyplot import *

ticker_name="FB"
begdate=(2014,9,24)
enddate=(2014,10,16)

facebook_price=finance.quotes_historical_yahoo(ticker_name,begdate,enddate,asobject=True, adjusted=True)

daily_returns=(facebook_price.close[1:]-facebook_price.close[:-1])/facebook_price.close[1:]

#These data are obtained through Datasift.com. The sentiment score for each tweet in one day of trading is downloaded and a daily average is computed.
average_sentiment=[1.228120516,0.979452055,0.893063584,0.839393939,0.532905297,0.617117117,0.976454294,0.710443038,0.702651515,0.661290323,0.609977324,0.328437917,0.608870968,0.433697348,0.414985591,0.449838188]

# Returns distribution
[n,bins,patches]=hist(daily_returns,100)

x=mlab.normpdf(bins,np.mean(daily_returns),np.std(daily_returns))
plot(bins,x,color='r',lw=2)

xlabel("Returns distribution")
ylabel("Frequency")
title("Facebook returns distribution")
show()

figure,(ax1,ax2)=pyplot.subplots(2,sharex=True)
pyplot.xticks(rotation=70)
pyplot.xlabel('Days of trading')

# Prices time series plot
ax1.plot(facebook_price.date,facebook_price.close,'o-')
ax1.set_title('Facebook prices series')
ax1.set_ylabel('Prices')

#Returns time series plot
ax2.plot(facebook_price.date[1:],daily_returns,'o-')
ax2.set_title('Facebook returns series')
ax2.set_ylabel('Returns')

figure.subplots_adjust(hspace=.5)

#Sentiment analysis
figure,ax1=pyplot.subplots()
pyplot.xticks(rotation=70)
x=facebook_price.date[1:]
y1=daily_returns
y2=average_sentiment

ax2=ax1.twinx()
ax1.plot(x,y1,'bo-')
ax2.plot(x,y2,'ro-')

figtext(0.2,0.2,'Blue for returns, Red for scores ')
xlabel("Days of trading")
ax1.set_ylabel('Returns')
ax2.set_ylabel('Scores')
title("Returns VS Sentiment score")
show()
