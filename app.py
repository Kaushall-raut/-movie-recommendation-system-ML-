import time
from warnings import catch_warnings

import streamlit as st
import pickle
import pandas as pd
import requests



movies_list=pickle.load(open('movie1.pkl','rb'))
similiar=pickle.load(open('similiar.pkl','rb'))
movie_list=movies_list['title'].values

def fetch_image(id):
    try:
        res=  requests.get(f'https://api.themoviedb.org/3/movie/{id}?api_key=78a0995fd10ee83ab18023f06a9bc32b')
        data=res.json()
#   st.write(data)
#   st.write(data['poster_path'])
        path=data.get('poster_path')
        return "https://image.tmdb.org/t/p/w500"+path
    except Exception  as e:
        return "Too much request on api"


def recommend(movie):
        movie_index=movies_list[movies_list['title']==movie].index[0]

        distance=similiar[movie_index]

        movie_lists=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

        recommendation=[]
        poster=[]
        for i in movie_lists:
           recommendation.append( movies_list.iloc[i[0]].title)
           time.sleep(5)
           poster.append(fetch_image(movies_list.iloc[i[0]].movie_id))
        return recommendation,poster

st.title("Movie recommender system")


selected_option = st.selectbox(
    "watch at your ease?",
    (movie_list),
    index=None,
    placeholder="Select movies",
)

st.write("You selected:", selected_option)

if st.button("Recommend"):
  time.sleep(5)
  rec,poster=recommend(selected_option)
#   for i in rec:
#      st.write(i)
  col1, col2, col3,col4,col5 = st.columns(5,width=500)

  with col1:
    st.text(rec[0])
    st.image(poster[0])

  with col2:
    st.text(rec[1])
    st.image(poster[1])

  with col3:
    st.text(rec[2])
    st.image(poster[2])

  with col4:
    st.text(rec[3])
    st.image(poster[3])

  with col5:
    st.text(rec[4])
    st.image(poster[4])