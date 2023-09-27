#Importing required libraries:
import streamlit as st
import pickle
import requests

#Poster display:
def fetch_poster( movie_id ):
    url = 'https://api.themoviedb.org/3/movie/{}?api_key=c7ec19ffdd3279641fb606d19ceb9bb1&language=en-US'.format( movie_id )
    data = requests.get( url )
    data = data.json()
    poster_file_path = data[ 'poster_path' ]
    full_path = 'https://image.tmdb.org/t/p/w500/' + poster_file_path
    return full_path

#Recommendation system fn:
def recommend( movie ):
    index = movies[ movies[ 'title' ] == movie ].index[ 0 ]
    gap = sorted( list( enumerate( similar_movies[ index ] ) ), reverse = True, key = lambda vector : vector[ 1 ] )
    recommend_movie = []
    recommend_movie_poster = []
    for _ in gap[ 1 : 11 ]:
        movies_id = movies.iloc[ _[ 0 ] ].id
        recommend_movie.append( movies.iloc[ _[ 0 ] ].title )
        recommend_movie_poster.append( fetch_poster( movies_id ) )
    return recommend_movie, recommend_movie_poster

#Gathering pickle files:
movies = pickle.load( open( 'C:/Users/AWIKSSHIITH/OneDrive/Desktop/MRS/movies_list.pkl', 'rb' ) )
similar_movies = pickle.load( open( 'C:/Users/AWIKSSHIITH/OneDrive/Desktop/MRS/similar_movies.pkl', 'rb' ) )
movies_list = movies[ 'title' ].values

#App interface:
st.header( 'RecommAI - Your personal movie recommender' )
user_input = st.selectbox( 'Select your favourite movie:', movies_list )
if st.button( 'Recommend movies' ):
    movie_title, poster = recommend( user_input )
    st.image( poster[ 0 ] )
    st.text( movie_title[ 0 ] )
    st.image( poster[ 1 ] )
    st.text( movie_title[ 1 ] )
    st.image( poster[ 2 ] )
    st.text( movie_title[ 2 ] )
    st.image( poster[ 3 ] )
    st.text( movie_title[ 3 ] )
    st.image( poster[ 4 ] )
    st.text( movie_title[ 4 ] )
    st.image( poster[ 5 ] )
    st.text( movie_title[ 5 ] )
    st.image( poster[ 6 ] )
    st.text( movie_title[ 6 ] )
    st.image( poster[ 7 ] )
    st.text( movie_title[ 7 ] )
    st.image( poster[ 8 ] )
    st.text( movie_title[ 8 ] )
    st.image( poster[ 9 ] )
    st.text( movie_title[ 9 ] )