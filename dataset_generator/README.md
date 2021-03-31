## Dataset Columns

* date
* close
* high
* low
* open
* volume
* adjClose 
* adjHigh
* adjLow
* adjOpen
* adjVolume
* divCash
* splitFactor


FIELD NAME | JSON FIELD | DATA TYPE | DESCRIPTION
-----------|------------|-----------|------------
Date | date | date |The date this data pertains to.
Open | open | float | The opening price for the asset on the given date.
High | high | float | The high price for the asset on the given date.
Low | low | float |The low price for the asset on the given date.  
Close | close | float | The closing price for the asset on the given date.  
Volume | volume | int64 | The number of shares traded for the asset.
Adj Open |  adjOpen |  float | The adjusted opening price for the asset on the given date.
Adj High |  adjHigh |  float | The adjusted high price for the asset on the given date.
Adj. Low | adjLow | float | The adjusted low price for the asset on the given date.
Adj. Close | adjClose | float | The adjusted closing price for the asset on the given date.
Adj. Volume | adjVolume | int64 | The number of shares traded for the asset.
Dividend | divCash | float | The dividend paid out on "date" (note that "date" will be the "exDate" for the dividend).
Split | splitFactor | float | The factor used to adjust prices when a company splits, reverse splits, or pays a distribution.


###Volume
Is the amount of shares bought/sold of a stock in a given period of time. It is important because the more volume the more people agree with the price of the stock.

###Adjusted Closing Price
The adjusted closing price shows the stock's value after posting a dividend. 
For example, if a share with a closing price of $100 paid a $5 dividend per share, the adjusted closing price would be $95 in order to account for the newly reduced value caused by the dividend.

###What is a dividend
_A stock dividend is a dividend payment to shareholders that is made in shares rather than as cash.
The stock dividend has the advantage of rewarding shareholders without reducing the company's cash balance, although it can dilute earnings per share._

