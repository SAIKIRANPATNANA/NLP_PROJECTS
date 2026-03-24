import streamlit as sl
import pandas as pd
import numpy as np
import pickle as pkl
import requests
def fetch_poster(movie_id):
    response = requests.get("https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US".format(movie_id))
    data = response.json()
    return "https://image.tmdb.org/t/p/w500/" + data["poster_path"]
def recommend(movie):
    movie_idx = df[df['title']==movie].index[0]
    distances = similarity[movie_idx]
    similar_movie_idx = sorted(list(enumerate(distances)),reverse=True,key=lambda x: x[1])[1:6]
    similar_movie_list = []
    for i in similar_movie_idx:
        li = []
        li.append(df.iloc[i[0]].id)
        li.append(df.iloc[i[0]].title)
        similar_movie_list.append(li)
    return similar_movie_list
movies_dict = pkl.load(open('notebooks/movies_dict.pkl','rb'))
df = pd.DataFrame(movies_dict)
similarity = pkl.load(open('notebooks/similarity.pkl','rb'))
sl.title("Movie Recommendation System")
selected_movie_name = sl.selectbox("Enter the Movie of your Interest?",df['title'].values)
if sl.button('Recommend'):
    recommendations = recommend(selected_movie_name)
    names = [i[1] for i in recommendations]
    posters = [i[0] for i in recommendations]
    col1, col2, col3, col4, col5 = sl.columns(5)
    with col1:
        sl.text(names[0])
        sl.image(fetch_poster(posters[0]))
    with col2:
        sl.text(names[1])
        sl.image(fetch_poster(posters[1]))
    with col3:
        sl.text(names[2])
        sl.image(fetch_poster(posters[2]))
    with col4:
        sl.text(names[3])
        sl.image(fetch_poster(posters[3]))
    with col5:
        sl.text(names[4])
        sl.image(fetch_poster(posters[4]))
    
