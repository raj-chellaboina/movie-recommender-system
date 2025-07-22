import streamlit as st
import pickle
import pandas as pd
import requests

def fetch(movie_id):
    # responce=requests.get('https://api.themoviedb.org/3/movie/{}?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US'.format(movie_id))
    # print(responce)
    # data=responce.json()
    # return "https://image.tmdb.org/t/p/w500"+data['poster_path']

    return "https://image.tmdb.org/t/p/w500/7BmQj8qE1FLuLTf7Xjf9sdIHzoa.jpg"
# api.themoviedb.org/3/movie/65?api_key=8265bd1679663a7ea12ac168da84d2e8&language=en-US
def recommend(movie):
    movie_index = movies[movies['title'] == movie].index[0]
    distance = similarity[movie_index]
    movie_list = sorted(list(enumerate(distance)), reverse=True, key=lambda x: x[1])[1:6]
    recommendded_movie=[]
    recommendded_movie_posters=[]
    for i in movie_list:
        movieid=movies.iloc[i[0]].movie_id
        recommendded_movie_posters.append(fetch(movieid))
        recommendded_movie.append(movies.iloc[i[0]].title)
    # print(recommendded_movie_posters)
    return recommendded_movie,recommendded_movie_posters

movie_list=pickle.load(open('movies_dict.pkl','rb'))
movies=pd.DataFrame(movie_list)

similarity=pickle.load(open('similarity.pkl','rb'))

st.title('Movie recomender')
option=st.selectbox('How would you like to be contacted',

                    movies['title'].values)

if st.button('Recommend'):
    names,posters=recommend(option)
    col1,col2,col3,col4,col5=st.columns(5)
    with col1:
        st.text(names[0])
        st.image(posters[0])
    with col2:
        st.text(names[1])
        st.image(posters[1])
    with col3:
        st.text(names[2])
        st.image(posters[2])
    with col4:
        st.text(names[3])
        st.image(posters[3])
    with col5:
        st.text(names[4])
        st.image(posters[4])