# -*- coding: utf-8 -*-
"""
Created on Tue Jun 11 12:22:51 2024

@author: Anamika
"""

import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns
import streamlit as st
import pickle as pk




st.markdown("# Reliance Stock Market Prediction")

data = pk.load(open(r"C:\Users\deept\Desktop\Reliance Industry Stock Forecast\data.pkl", 'rb'))
price = pk.load(open(r"C:\Users\deept\Desktop\Reliance Industry Stock Forecast\price_df.pkl", 'rb'))
st.set_option('deprecation.showPyplotGlobalUse', False)
st.title('Visualizations')
st.header("Graphs")
plt.figure(figsize=(20,15))
    #Plot 1
    
plt.subplot(2,2,1)
plt.plot(data['Open'],color='green')
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.title('Open')
#Plot 2
plt.subplot(2,2,2)
plt.plot(data['Close'],color='red')
plt.xlabel('Date')
plt.ylabel('Close Price')
plt.title('Close')
#Plot 3
plt.subplot(2,2,3)
plt.plot(data['High'],color='green')
plt.xlabel('Date')
plt.ylabel('High Price')
plt.title('High')
#Plot 4
plt.subplot(2,2,4)
plt.plot(data['Low'],color='red')
plt.xlabel('Date')
plt.ylabel('Low Price')
plt.title('Low')
st.pyplot()
    
st.header("Box Plots")
plt.figure(figsize=(20,15))
#Plot 1
plt.subplot(2,2,1)
plt.boxplot(data['Open'])
plt.xlabel('Date')
plt.ylabel('Open Price')
plt.title('Open')
#Plot 2
plt.subplot(2,2,2)
plt.boxplot(data['Close'])
plt.xlabel('Date')
plt.ylabel('Cloes Price')
plt.title('Close')
#Plot 3
plt.subplot(2,2,3)
plt.boxplot(data['High'])
plt.xlabel('Date')
plt.ylabel('High Price')
plt.title('High')
#Plot 4
plt.subplot(2,2,4)
plt.boxplot(data['Low'])
plt.xlabel('Date')
plt.ylabel('Low Price')
plt.title('Low')
st.pyplot()


#-------------------------KDE Plots-----------------------------------------
st.header("KDE Plots")
# KDE-Plots
plt.figure(figsize=(20,15))
#Plot 1
plt.subplot(2,2,1)
sns.kdeplot(data['Open'], color='green')
plt.title('Open')
#Plot 2
plt.subplot(2,2,2)
sns.kdeplot(data['Close'], color='red')
plt.title('Close')
#Plot 3
plt.subplot(2,2,3)
sns.kdeplot(data['High'], color='green')
plt.title('High')
#Plot 4
plt.subplot(2,2,4)
sns.kdeplot(data['Low'], color='red')
plt.title('Low')
st.pyplot()

b=st.button('Show next 30 days predictions')

if(b):
    price

