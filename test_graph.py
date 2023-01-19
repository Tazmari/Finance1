def check(sma5_last2, price2):
    for ticker_list_items in ticker_list:
        ticker_list_objects = yf.Ticker(ticker_list_items)

    current_price_df = ticker_list_objects.history(start=start_date, end=end_date)
    price2 = round(current_price_df['Close'].iloc[-1],2)
    col1, col2 = st.columns([2, 2])
    data = np.random.randn(10, 1)
    col1.write(price2)
#for ticker_list_items in ticker_list:
   # ticker_list_objects = yf.Ticker(ticker_list_items)
    current_price_df2 = ticker_list_objects.history(start=start_date, end=end_date)
    current_price_df2['SMA-5%'] = talib.SMA(current_price_df2['Close']*.95, timeperiod = 10)
    sma5_list2 = current_price_df2['SMA-5%']
    sma5_last2 = round(sma5_list2[-1],2)

    col1, col2 = st.columns([2, 2])
    data = np.random.randn(10, 1)
    col2.write(sma5_last2)
    if sma5_last2>= price2:
        return True
    return False

if check(sma5_last2,price2):
    print("Yes")
else:
    print("No")