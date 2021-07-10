import quandl as qd
import matplotlib.pyplot as matplt

qd.ApiConfig.api_key = 'D7NyVWy1fazEisAuyhHX'

Microsoft_data = qd.get('EOD/MSFT', start_date="2010-07-09", end_date="2021-07-09")
Microsoft = Microsoft_data.head()
# print(Microsoft)

# Calculate the Returns
close_price = Microsoft_data[['Adj_Close']]
daily_return = close_price.pct_change()
daily_return.fillna(0, inplace=True)
# print(daily_return)

adj_price = Microsoft_data[['Adj_Close']]

# Calculate the moving average
mav = adj_price.rolling(window=50).mean()

# Print the results
print(mav[-10:])

adj_price.plot()
mav.plot()
matplt.show()