from coincall import User, Public, Futures, Options, Referral

if __name__ == '__main__':

    # NO AUTH
    # api_key = '-1'
    # api_secret_key = '-1'

    # prod
    api_key = 'xdtHWn32rsuDQConutzl9JDZB+Y1leitFl356YHrmts='
    api_secret_key = 'LIvSQPOTSS+CaxqrsbbWnM/R02WksxA/W2JdYK62AxE='

    publicApi = Public.PublicAPI()
    userApi = User.UserAPI(api_key, api_secret_key)
    futuresApi = Futures.FuturesAPI(api_key, api_secret_key)
    optionsApi = Options.OptionsAPI(api_key, api_secret_key)
    referralApi = Referral.ReferralAPI(api_key, api_secret_key)

    # Public
    # print(publicApi.get_server_time())
    # print(publicApi.get_config())
    # print(publicApi.get_realtime_funding_rate())

    # User
    # print(userApi.get_user_info())
    # print(userApi.get_account_summary())

    # Futures
    # print(futuresApi.get_symbols())
    # print(futuresApi.get_depth(symbol='BTCUSD'))
    # print(futuresApi.get_lasttrade(symbol='BTCUSD'))
    # print(futuresApi.get_leverage(symbol='BTCUSD'))
    # print(futuresApi.set_leverage(symbol='BTCUSD', leverage=1))
    # print(futuresApi.get_positions())
    # print(futuresApi.place_order('BTCUSD',0.5,1,3,price=25000.1))
    # print(futuresApi.cancel_order(clientOrderId=1663004711982333952))
    # print(futuresApi.cancel_orders('BTCUSD'))
    # print(futuresApi.get_open_orders(symbol='BTCUSD'))
    # print(futuresApi.get_order_by_id(orderId=1663004711982333952))
    # print(futuresApi.get_order_history())
    # print(futuresApi.get_trade_history())

    # Options
    # print(optionsApi.get_instruments('BTC'))
    # print(optionsApi.get_options_by_endtime(index='BTCUSD',endTime='1719561600000'))
    # print(optionsApi.get_option_by_name('BTCUSD-28JUN24-90000-P'))
    # print(optionsApi.get_depth(symbol='BTCUSD-28JUN24-38000-C'))
    # print(optionsApi.get_lasttrade(symbol='BTCUSD-28JUN24-90000-P'))
    # print(optionsApi.get_positions())
    # print(optionsApi.place_order('BTCUSD-28JUN24-38000-C',0.5,1,3,price=4000))
    # print(optionsApi.cancel_order(clientOrderId=166300471198952))
    # print(optionsApi.cancel_orders('ETHUSD'))
    # print(optionsApi.get_open_orders())
    # print(futuresApi.get_order_by_id(clientOrderId=1663004711982333952))
    # print(futuresApi.get_order_history())
    # print(futuresApi.get_trade_history(startTime=1695023717407))

    # Referral
    print(referralApi.get_referrals())

