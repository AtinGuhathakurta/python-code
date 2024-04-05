#!/usr/bin/env python
# coding: utf-8

# In[1]:


import pandas as pd
import numpy as np
import yfinance as yf
import pandas_datareader.data as web
import datetime


# In[2]:


#Listing random 70 stocks avaialble to be extracted using yFinance

Stock = [
    {"name": "Bharti Airtel Limited", "symbol": "BHARTIARTL.NS"},
    {"name": "Ashok Leyland Limited", "symbol": "ASHOKLEY.NS"},
    {"name": "Aurobindo Pharma Limited", "symbol": "AUROPHARMA.NS"},
    {"name": "Arex Industries Ltd.", "symbol": "AREXMIS.BO"},
    {"name": "Sanwaria Agro Oils Limited", "symbol": "SANWARIA.NS"},
    {"name": "Almondz Global Securities Limited", "symbol": "ALMONDZ.NS"},
    {"name": "Adinath Textiles Ltd", "symbol": "ADINATH.BO"},
    {"name": "State Bank of India", "symbol": "SBIN.NS"},
    {"name": "Bharat Petroleum Corporation Limited", "symbol": "BPCL.NS"},
    {"name": "McNally Bharat Engineering Company Limited", "symbol": "MBECL.NS"},
    {"name": "Bank of Maharashtra", "symbol": "MAHABANK.NS"},
    {"name": "D. B. Corp Limited", "symbol": "DBCORP.BO"},
    {"name": "Bosch Limited", "symbol": "BOSCHLTD.NS"},
    {"name": "Bharat Heavy Electricals Ltd.", "symbol": "BHEL.BO"},
    {"name": "IDBI Bank Limited", "symbol": "IDBI.NS"},
    {"name": "IRB Infrastructure Developers Limited", "symbol": "IRB.BO"},
    {"name": "Dabur India Limited", "symbol": "DABUR.NS"},
    {"name": "TCI Developers Limited", "symbol": "TCIDEVELOP.NS"},
    {"name": "New Delhi Television Limited", "symbol": "NDTV.BO"},
    {"name": "Ishita Drugs & Industries Ltd", "symbol": "ISHITADR.BO"},
    {"name": "Gateway Distriparks Limited", "symbol": "GDL.BO"},
    {"name": "Dr. Reddy's Laboratories Limited", "symbol": "DRREDDY.NS"},
    {"name": "India Power Corporation Limited", "symbol": "DPSCLTD.NS"},
    {"name": "DLF Limited", "symbol": "DLF.BO"},
    {"name": "Deepak Spinners Limited", "symbol": "DEEPAKSP.BO"},
    {"name": "Danlaw Technologies India Limited", "symbol": "DANLAW.BO"},
    {"name": "Vipul Dye Chem Ltd.", "symbol": "VIPULDYE.BO"},
    {"name": "Vadilal Dairy International Ltd.", "symbol": "VADIDAI.BO"},
    {"name": "Trimurthi Limited", "symbol": "TRIMURTHI.BO"},
    {"name": "Thakkers Developers Ltd", "symbol": "THAKDEV.BO"},
    {"name": "TATA MOTORS LTD - DVR", "symbol": "TATAMTRDVR.BO"},
    {"name": "SUPERSTAR DISTILLERIES & FOODS", "symbol": "SUPDF.BO"},
    {"name": "Shri Dinesh Mills Limited", "symbol": "SHRIDINE.BO"},
    {"name": "Radhe Developers (India) Ltd.", "symbol": "RADHEDE.BO"},
    {"name": "Proto Developers & Technologies Limited", "symbol": "PROTODEV.BO"},
    {"name": "Prabhat Dairy Limited", "symbol": "PRABHAT.NS"},
    {"name": "ND Metal Industries Ltd", "symbol": "NDMETAL.BO"},
    {"name": "MODERN DENIM LTD.", "symbol": "MDRNSUT-B.BO"},
    {"name": "Mangalam Drugs & Organics Limited", "symbol": "MANGALAM.BO"},
    {"name": "Mahindra Lifespace Developers Limited", "symbol": "MAHLIFE.NS"},
    {"name": "Landmark Property Development Company Limited", "symbol": "LPDC.NS"},
    {"name": "Kaushalya Infrastructure Development Corporation Limited", "symbol": "KAUSHALYA.NS"},
    {"name": "IRB Infrastructure Developers Limited", "symbol": "IRB.NS"},
    {"name": "Interworld Digital Ltd.", "symbol": "INTERDIGI.BO"},
    {"name": "Indian Toners & Developers Ltd.", "symbol": "INDTONER.BO"},
    {"name": "India Lease Development Limited", "symbol": "INDLEASE.BO"},
    {"name": "Housing Development and Infrastructure Limited", "symbol": "HDIL.NS"},
    {"name": "Housing Development & Infrastructure Limited", "symbol": "HDIL.BO"},
    {"name": "Housing Development Finance Corporation Limited", "symbol": "HDFC.NS"},
    {"name": "Housing Development Finance Corporation Limited", "symbol": "HDFC.BO"},
    {"name": "Golkunda Diamonds & Jewellery Limited", "symbol": "GOLKUNDIA.BO"},
    {"name": "Goenka Diamond and Jewels Limited", "symbol": "GOENKA.NS"},
    {"name": "Ess Dee Aluminium Limited", "symbol": "ESSDEE.BO"},
    {"name": "Energy Development Company Limited", "symbol": "ENERGYDEV.NS"},
    {"name": "E.I.D.- Parry (India) Limited", "symbol": "EIDPARRY.BO"},
    {"name": "Keltech Energies Limited", "symbol": "KELENRG.BO"},
    {"name": "Schneider Electric Infrastructure Limited", "symbol": "SCHNEIDER.NS"},
    {"name": "Eastern Silk Industries Ltd.", "symbol": "EASTSILK.BO"},
    {"name": "Tata Elxsi Limited", "symbol": "TATAELXSI.NS"},
    {"name": "Swaraj Engines Limited", "symbol": "SWARAJENG.NS"},
    {"name": "Sterling International Enterprises Ltd.", "symbol": "STEERINTER.BO"},
    {"name": "Sequel e-Routers Ltd.", "symbol": "SEQUELE.BO"},
    {"name": "Rural Electrification Corporation Limited", "symbol": "RECLTD.NS"},
    {"name": "Piramal Enterprises Limited", "symbol": "PEL.NS"},
    {"name": "M.K. Exim (India) Limited", "symbol": "MKEXIM.BO"},
    {"name": "Jaybharat Textiles And Real Estate Limited", "symbol": "JAYTEX.BO"},
    {"name": "Indiabulls Real Estate Limited", "symbol": "IBREALEST.BO"},
    {"name": "Everonn Education Limited", "symbol": "EVERONN.NS"},
    {"name": "Essel Propack Limited", "symbol": "ESSELPACK.NS"},
    {"name": "Entegra Limited", "symbol": "ENTEGRA.NS"},
    {"name": "Emmessar Biotech & Nutrition Limited", "symbol": "EMMESSA.BO"},
    {"name": "E.com Infotech India Ltd.", "symbol": "ECOM.BO"},
    {"name": "Bharat Electronics Limited", "symbol": "BEL.BO"},
    {"name": "Adani Ports and Special Economic Zone Limited", "symbol": "ADANIPORTS.NS"},
    {"name": "Zicom Electronic Security Systems Limited", "symbol": "ZICOM.BO"},
    {"name": "Anukaran Commercial Enterprises Ltd.", "symbol": "ZANUKCOM.BO"},
    {"name": "Oracle Financial Services Software Limited", "symbol": "OFSS.NS"},
    {"name": "LIC Housing Finance Limited", "symbol": "LICHSGFIN.NS"},
    {"name": "Fortune Financial Services (India) Limited", "symbol": "FORTUNEF.BO"},
    {"name": "Sundram Fasteners Limited", "symbol": "SUNDRMFAST.BO"},
    {"name": "Sundaram Finance Limited", "symbol": "SUNDARMFIN.BO"},
    {"name": "Sita Shree Food Products Limited", "symbol": "SITASHREE.NS"},
    {"name": "Relaxo Footwears Limited", "symbol": "RELAXO.BO"},
    {"name": "Rashtriya Chemicals And Fertilizers Limited", "symbol": "RCF.BO"},
    {"name": "PTC India Financial Services Limited", "symbol": "PFS.NS"},
    {"name": "Power Finance Corporation Limited", "symbol": "PFC.NS"},
    {"name": "Nikki Global Finance Limited", "symbol": "NIKKIGL.BO"},
    {"name": "Muthoot Finance Limited", "symbol": "MUTHOOTFIN.NS"},
    {"name": "Max Financial Services Limited", "symbol": "MAX.NS"},
    {"name": "Magma Fincorp Limited", "symbol": "MAGMA.NS"},
]

#Declaring Columns in the dataframe to used for Optimization

Stocks=pd.DataFrame(Stock)    #declaring as dataframe from list
Stocks = Stocks.reset_index()
Stocks["Industry"]=""
Stocks["Current Price"]=""    #recording the latest price
Stocks["Historic Price"]=""   #recording the historic price
Stocks["Weight"]=1            #assigning one weight to each of the 70 stocks. Assuming Thats the desired asset class allocation
Stocks["Diff"]=""             #Tracking movement of the stock prices
Stocks["Growth"]=""           #Tracking the percentage growth/fall of the proce from historic records


# In[3]:


# Recording the metrics against each stock in the portfolio to calculate the benchmark and re-calibrate the weight of the stocks

for index,i in Stocks.iterrows():
    try:
        name = i['name']          #assigning the name of the stock
        symbol = i['symbol']      #assigning the ticker of the stock
 
        stock = yf.Ticker(symbol)

        startDate = datetime.datetime(2021, 1, 1)
        endDate = datetime.datetime(2022, 1, 1)
        
        current_price = stock.history(period='1d')["Close"].iloc[-1]     #recording the latest price of the stock
        historic_price = stock.history(period='1y')["Open"].iloc[-1]     #recording the historic price of the stock

        Stocks["Industry"]=stock.info['sector']
        
        formatted_current_price = "{:.2f}".format(current_price)          #formatting the price to 2 decimal points for readability
        Stocks.iloc[index,Stocks.columns.get_loc('Current Price')]=formatted_current_price
        
        formatted_historic_price = "{:.2f}".format(historic_price)        #formatting the price to 2 decimal points for readability
        Stocks.iloc[index,Stocks.columns.get_loc('Historic Price')]=formatted_historic_price

        #print(f"{name}: {formatted_current_price}")
    except:
        Stocks.drop(index,axis=0, inplace=True)         #drop stocks whose data cannot be retrieved or have updated information
        #print("exception")
        pass


# In[4]:


Stocks['Current Price'].replace('', np.nan, inplace=True)
Stocks['Historic Price'].replace('', np.nan, inplace=True)

Stocks.dropna(subset=['Current Price'],inplace = True)      #removing stocks with zero or null share prices
Stocks.dropna(subset=['Historic Price'],inplace = True)     #removing stocks with zero or null share prices

Stocks["Diff"]=Stocks["Current Price"].astype(float)-Stocks["Historic Price"].astype(float)   #calculating the movement of the share price

Stocks["Current Price"]=Stocks["Current Price"].astype(float)   #reassigning the prices to floating type from string for calculation
Stocks["Historic Price"]=Stocks["Historic Price"].astype(float)  #reassigning the prices to floating type from string for calculation

Stocks["Growth"]=(Stocks["Diff"]+Stocks["Historic Price"])/Stocks["Historic Price"]    #calculating the percentage movement of each share

Portfolio = Stocks.sum(axis=0)        #summarizing all the metrics to total
Portfolio["Growth"]=(Portfolio["Diff"]+Portfolio["Historic Price"])/Portfolio["Historic Price"]   #calculating the percentage movement of total portfolio

Stocks["Weight"]=Portfolio["Growth"]/Stocks["Growth"]   #Re-calibrating the weight of the individual stocks to keep consistent asset class allocation

Stocks.sort_values(by="Growth",ascending=False,inplace=True)  #Sorting the list of stocks by growth% to show the best performing shares
Stocks.reset_index(inplace=True,drop=True)

display(Stocks)



# In[ ]:





# In[ ]:




