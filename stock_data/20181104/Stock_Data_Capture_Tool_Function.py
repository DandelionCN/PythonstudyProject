#!/usr/bin/python3
# -*- coding:utf-8 -*-
# tushare data capture by pyhon3

""" tushare function list
bar', 'bdi', 'broker_tops', 'cap_tops', 'close_apis', 'codecs', 'coins', 'coins_bar', 'coins_snapshot', 'coins_tick', 'coins_trade', 
'day_boxoffice', 'day_cinema',
 'forecast_data', 'fund', 'fund_holdings', 'futures', 'get_apis', 'get_area_classified', 'get_balance_sheet', 'get_cash_flow', 'get_cashflow_data', 'get_cffex_daily', 'get_concept_classified', 'get_cpi', 'get_czce_daily', 'get_day_all', 'get_dce_daily', 'get_debtpaying_data', 'get_deposit_rate', 'get_fund_info', 'get_future_daily',
 'get_gdp_contrib', 'get_gdp_for', 'get_gdp_pull', 'get_gdp_quarter', 'get_gdp_year', 
'get_gem_classified', 'get_gold_and_foreign_reserves', 'get_growth_data', 
'get_h_data', 'get_hist_data', 'get_hists', 'get_hs300s', 'get_index', 'get_industry_classified', 'get_instrument', 'get_intlfuture', 'get_k_data', 'get_latest_news', 'get_loan_rate', 'get_markets', 'get_money_supply', 'get_money_supply_bal', 'get_nav_close', 'get_nav_grading', 'get_nav_history', 'get_nav_open', 'get_notices', 'get_operation_data', 'get_ppi', 'get_profit_data', 'get_profit_statement', 'get_realtime_quotes', 'get_report_data', 'get_rrr', 'get_shfe_daily', 'get_shfe_vwap', 'get_sina_dd', 'get_sme_classified', 'get_st_classified', 'get_stock_basics', 'get_suspended', 'get_sz50s', 'get_terminated', 'get_tick_data', 'get_today_all', 'get_today_ticks', 
'get_token', 'get_zz500s', 'global_realtime', 'guba_sina', 'inst_detail', 'inst_tops', 'internet', 'is_holiday', 'latest_content', 'lpr_data', 'lpr_ma_data', 'margin_detail', 'margin_offset', 'margin_target', 'margin_zsl', 'moneyflow_hsgt',
 'month_boxoffice', 'new_cbonds', 'new_stocks', 'notice_content', 'os', 'pledged_detail', 'pro', 'pro_api', 'pro_bar', 'profit_data', 'profit_divis', 'quotes', 
'realtime_boxoffice', 'reset_instrument', 'set_token', 'sh_margin_details', 'sh_margins', 'shibor_data', 'shibor_ma_data', 'shibor_quote_data', 'stock', 'stock_issuance', 'stock_pledged', 'sz_margin_details', 'sz_margins', 'tick',
 'top10_holders', 'top_list', 'trade_cal', 'trader', 'util', 'xsg_data']
 
"""

import pandas as pd
import tushare as ts
import datetime
import os


def capture_stock_data():
    capture_date = datetime.datetime.now().strftime("%Y%m%d")
    save_dir = "/home/dandelion/stock_data/" + capture_date

    if not os.path.exists(save_dir):
        os.mkdir(save_dir)
        print("The save directory is created successfully!\n",save_dir)
    print("The save directory is already exist!\n",save_dir)
    # ======================Daily Command================================================================
    # get the boxoffcie data of the last day and save as csvfile named as the capture command
    ts.day_boxoffice().to_csv(
        save_dir + "/" + capture_date + "_day_boxoffice.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("day_boxoffice data capture completed!")

    # get the cinema data of the last day and save as csvfile named as the capture command
    ts.day_cinema().to_csv(
        save_dir + "/" + capture_date + "_day_cinema.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("day_cinema data capture completed!")

    ts.month_boxoffice().to_csv(
        save_dir + "/" + capture_date + "_month_boxoffice.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("month_boxoffice data capture completed!")

    ts.realtime_boxoffice().to_csv(
        save_dir + "/" + capture_date + "_realtime_boxoffice.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("realtime_boxoffice data capture completed!")

    # get the stock data index of the last day and save as csvfile named as the capture command
    ts.get_index().to_csv(
        save_dir + "/" + capture_date + "_get_index.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_index data capture completed!")

    # get the history cpi data and save as csvfile named as the capture command
    ts.get_cpi().to_csv(
        save_dir + "/" + capture_date + "_get_cpi.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_cpi data capture completed!")

    # get the history gdp data  by month and save as csvfile named as the capture command
    ts.get_gdp_year().to_csv(
        save_dir + "/" + capture_date + "_get_gdp_year.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_gdp_year data capture completed!")

    # get today all stock data and save as csvfile named as the capture command
    # ts.get_today_all().to_csv(save_dir+'/'+capture_date+'_get_today_all.csv',header=True,sep=',',index=False)

    # get detail information of the top brokers today and save as csvfile named as the capture command
    ts.broker_tops().to_csv(
        save_dir + "/" + capture_date + "_broker_tops.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("broker_tops data capture completed!")

    # get detail information of the top brokers today and save as csvfile named as the capture command
    ts.cap_tops().to_csv(
        save_dir + "/" + capture_date + "_cap_tops.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("cap_tops data capture completed!")

    ts.get_area_classified().to_csv(
        save_dir + "/" + capture_date + "_get_area_classified.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_area_classified data capture completed!")

    # ts.get_balance_sheet(code='').to_csv(save_dir+'/'+capture_date+'_get_balance_sheet.csv',header=True,sep=',',index=False)
    # print('get_balance_sheet data capture completed!')

    # ts.get_cash_flow(code='').to_csv(save_dir+'/'+capture_date+'_get_cash_flow.csv',header=True,sep=',',index=False)
    # print('get_cash_flow data capture completed!')

    ts.get_day_all().to_csv(
        save_dir + "/" + capture_date + "_get_day_all.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_day_all data capture completed!")
    ts.get_cashflow_data(2018, 3).to_csv(
        save_dir + "/" + capture_date + "_get_cashflow_data.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_cashflow_data data capture completed!")
    ts.get_concept_classified().to_csv(
        save_dir + "/" + capture_date + "_get_concept_classified.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_concept_classified data capture completed!")
    ts.get_debtpaying_data(2018, 3).to_csv(
        save_dir + "/" + capture_date + "_get_debtpaying_data.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_debtpaying_data data capture completed!")
    ts.get_deposit_rate().to_csv(
        save_dir + "/" + capture_date + "_get_deposit_rate.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_deposit_rate data capture completed!")

    ts.get_gdp_contrib().to_csv(
        save_dir + "/" + capture_date + "_get_gdp_contrib.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_gdp_for().to_csv(
        save_dir + "/" + capture_date + "_get_gdp_for.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_gdp_pull().to_csv(
        save_dir + "/" + capture_date + "_get_gdp_pull.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_gdp_quarter().to_csv(
        save_dir + "/" + capture_date + "_get_gdp_quarter.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("get_gdp_ data capture completed!")
    # ts.get_gdp_year().to_csv(save_dir+'/'+capture_date+'_get_gdp_year.csv',header=True,sep=',',index=False)
    ts.get_gem_classified().to_csv(
        save_dir + "/" + capture_date + "_get_gem_classified.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_gold_and_foreign_reserves().to_csv(
        save_dir + "/" + capture_date + "_get_gold_and_foreign_reserves.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_growth_data(2018, 3).to_csv(
        save_dir + "/" + capture_date + "_get_growth_data.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_industry_classified().to_csv(
        save_dir + "/" + capture_date + "_get_industry_classified.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_hs300s().to_csv(
        save_dir + "/" + capture_date + "_get_hs300s.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_sz50s().to_csv(
        save_dir + "/" + capture_date + "_get_sz50s.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_zz500s().to_csv(
        save_dir + "/" + capture_date + "_get_zz500s.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_operation_data(2018, 3).to_csv(
        save_dir + "/" + capture_date + "_get_operation_data.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_stock_basics().to_csv(
        save_dir + "/" + capture_date + "_get_stock_basics.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.get_report_data(2018, 3).to_csv(
        save_dir + "/" + capture_date + "_get_report_data.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.inst_detail().to_csv(
        save_dir + "/" + capture_date + "_inst_detail.csv",
        header=True,
        sep=",",
        index=False,
    )
    ts.inst_tops().to_csv(
        save_dir + "/" + capture_date + "_inst_tops.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("inst_tops data capture completed!")
    ts.new_stocks().to_csv(
        save_dir + "/" + capture_date + "_new_stocks.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("new_stocks data capture completed!")
    ts.top_list().to_csv(
        save_dir + "/" + capture_date + "_top_list.csv",
        header=True,
        sep=",",
        index=False,
    )
    print("top_list data capture completed!")

    # get_hist_data(code='', start='2017-08-01', end='2018-08-01', ktype='D', retry_count=3, pause=0.001)
    # 数据类型，D=日k线 W=周 M=月 5=5分钟 15=15分钟 30=30分钟 60=60分钟，默认为D

    # get_k_data(code='', start='', end='', ktype='D', autype='qfq', index=False, retry_count=3, pause=0.001)
    # ts.get_realtime_quotes('601577')

    # top10_holders(code='', year='', quarter='', gdtype='0', retry_count=3, pause=0.001)
    # top_list(date=None, retry_count=3, pause=0.001)
    # trade_cal()
    # xsg_data(year=None, month=None, retry_count=3, pause=0.001)    获取限售股解禁数据


if __name__ == "__main__":
    print("==========================================================================")
    print("Better Tool,Better Future!Welcome to use Stock_Data_Capture tool!")
    print("--------------------------------------------------------------------------")
    print("Author:Dandelion|Contact:490359939@qq.com|All rights reserved!")
    print("--------------------------------------------------------------------------")
    print("Attention Please:Make sure your file directory has no Chinese Characters!")
    print("==========================================================================")
    print("Now start to capture data.......")
    capture_stock_data()
    print("All datas have been captured completely!")
    input("Press EnterKey to Exit the Programe!")
