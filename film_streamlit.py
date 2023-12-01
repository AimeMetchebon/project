# -*- coding: utf-8 -*-
"""
Created on Thu Nov 30 14:10:27 2023

@author: metch
"""


import streamlit as st
import pandas as pd
#from PIL import Image

import matplotlib.pyplot as plt


#import plotly.express as px

# une analyse de corrélation et de distribution grâce à différents graphiques et des commentaires.

st.title('Presentation Projet 2 Groupe 4: Audrey, Florent et Aimé')

link = "C:/Users/metch/Projet2_WCS/df20film.csv"
df20= pd.read_csv(link)

st.write(df20.head(10))

st.write('Présentation de quelques chiffres clés')

st.write(f"nombre total de films présents dans la base de données: {df20['tconst'].nunique()}")


import seaborn as sns


pays = st.radio(
    "Présentation de quelques chiffres clés",
    ["nombre de films par pays de production", "categories principales des parties prenantes des films", \
     "Nombre de film par acteurs ces 20 dernieres années","Popularité budget et Genre de Film"],
    captions = ["FPP","Cat","NFA","POP"])

if pays == "nombre de films par pays de production":
    #fig = plt.figure(figsize = (15, 5))
    viz_barplot = sns.barplot(x = df20.groupby(['pays1'])['tconst'].nunique().sort_values(ascending =False).head(20).index, \
            y= df20.groupby(['pays1'])['tconst'].nunique().sort_values(ascending =False).head(20).values
    								)

    st.pyplot(viz_barplot.figure)

    plt.close()

    #viz_correlation = sns.barplot(x = df20.groupby(['category'])['tconst'].nunique().sort_values(ascending =False).head(6).index, \
           # y= df20.groupby(['category'])['tconst'].nunique().sort_values(ascending =False).head(6).values)
    								
    #st.pyplot(viz_correlation.figure)
    
    #plt.close()
    
elif pays == "categories principales des parties prenantes des films":
    viz_barplot = sns.barplot(y = df20.groupby(['category'])['tconst'].nunique().sort_values(ascending =False).index, \
            x = df20.groupby(['category'])['tconst'].nunique().sort_values(ascending =False).values)

    st.pyplot(viz_barplot.figure)

    plt.close()

    #viz_correlation = sns.pairplot(df_cars[df_cars.continent.str.contains("Europe")].drop('continent', axis = 1)						
    #								)
    								
    #st.pyplot(viz_correlation.figure)
    #plt.close()
    
elif pays == "Nombre de film par acteurs ces 20 dernieres années":
    viz_barplot = sns.barplot(y = df20[(df20['category']=='actor') & (df20['release_date']>='2000') ]['primaryName'].value_counts().head(10).index, \
            x= df20[(df20['category']=='actor') & (df20['release_date']>='2000') ]['primaryName'].value_counts().head(10).values)

    st.pyplot(viz_barplot.figure)

    plt.close()

    #st.write(df20[(df20['category']=='actor') & (df20['release_date']>='2000') ]['primaryName'].value_counts().head(20))
    
    
else:        
    
    viz_barplot = sns.scatterplot(df20[df20['release_date']>='2010'],y ='firstGenre',x='popularity', size ='budget')					
    								
    								
    st.pyplot(viz_barplot.figure)
    
    plt.close()
 
    #st.write('Variation de la popularité et du budget en fonction du genre de film')   
   


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