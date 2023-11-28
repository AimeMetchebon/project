# -*- coding: utf-8 -*-
"""
Created on Tue Nov 21 19:33:51 2023

@author: metch
"""
import streamlit as st
import pandas as pd

import matplotlib.pyplot as plt
# une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.


link = "https://raw.githubusercontent.com/murpi/wilddata/master/quests/cars.csv"
df_cars = pd.read_csv(link)
st.write(df_cars)

st.write('Anlyse de correlation')


import seaborn as sns


pays = st.radio(
    "Choisissez le pays pour voir le graphique de correlation",
    ["US", "Europe", "Japan"],
    captions = ["Etats Unis Ameriques", "Europe", "Japan"])

if pays == "US":
    viz_correlation = sns.heatmap(df_cars[df_cars.continent.str.contains("US")].drop('continent', axis = 1).corr(), 
    								center=0,
    								cmap = sns.color_palette("vlag", as_cmap=True)
    								)

    st.pyplot(viz_correlation.figure)

    plt.close()

    viz_correlation = sns.pairplot(df_cars[df_cars.continent.str.contains("US")].drop('continent', axis = 1)						
    								)
    								
    st.pyplot(viz_correlation.figure)
    
    plt.close()
    
elif pays == "Europe":
    viz_correlation = sns.heatmap(df_cars[df_cars.continent.str.contains("Europe")].drop('continent', axis = 1).corr(), 
    								center=0,
    								cmap = sns.color_palette("vlag", as_cmap=True)
    								)

    st.pyplot(viz_correlation.figure)

    plt.close()

    viz_correlation = sns.pairplot(df_cars[df_cars.continent.str.contains("Europe")].drop('continent', axis = 1)						
    								)
    								
    st.pyplot(viz_correlation.figure)
    plt.close()
    
else:
    viz_correlation = sns.heatmap(df_cars[df_cars.continent.str.contains("Japan.")].drop('continent', axis = 1).corr(), 
    								center=0,
    								cmap = sns.color_palette("vlag", as_cmap=True)
    								)

    st.pyplot(viz_correlation.figure)

    plt.close()

    viz_correlation = sns.pairplot(df_cars[df_cars.continent.str.contains("Japan")].drop('continent', axis = 1)						
    								)
    								
    st.pyplot(viz_correlation.figure)
 
       
    plt.close()


    #st.write('corelation negative entre ,mpg et cylinders, mpg et hp, mpg et cubicinches, mpg et cylinders')

    #st.write('correlation positive entre cubicinches et culindres, cylinders et weightlbs')

#viz_correlation = sns.heatmap(df_cars[df_cars['continent']=='Japan.'].corr(), 
#								center=0,
#								cmap = sns.color_palette("vlag", as_cmap=True)
#								)
#st.pyplot(viz_correlation.figure)

#plt.close()


#viz_correlation = sns.pairplot(df_cars, hue ='continent'						
#								)
#								
#st.pyplot(viz_correlation.figure)

#st.write(df_cars.loc["Europe.",:])