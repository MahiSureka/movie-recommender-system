import streamlit as st
import pandas as pd
import pickle
import requests

st.set_page_config(
    page_title="Movie Recommender", 
    layout = "centered"
)

#removes the extra space on top
st.markdown("""<style>.block-container {
    padding-top: 2rem; padding-bottom: 1rem; }
</style> """, unsafe_allow_html=True)

st.title("Movie Recommender System")
#st.markdown("---")
#st.write("Welcome to the Hollywood and Bollywood Movie Recommender!")
#st.caption("Find your next favourite!")
st.markdown(
    "<p style='margin-top:-10px; color:gray;'>Find your next favourite!</p>",
    unsafe_allow_html=True
)

# trial data: 

# industry = st.radio(
#    "Choose an industry:",
#    ["Hollywood", "Bollywood"])

# movies = pd.read_csv("data/tmdb_5000_movies.csv") #load the csv

# movie_list = movies["title"].values #takes all movie names

# movie = st.selectbox(
#     "Select a movie:",
#     movie_list
# ) 

#if st.button("Recommend"):
#    st.write(f"You selected {movie} from {industry}.")

cinema = st.radio(
    "Choose Cinema:",
    ["Hollywood", "Bollywood"]
)

if cinema == "Hollywood":
    movies = pickle.load(open("moviesH.pkl", "rb"))
    recommendations = pickle.load(open("recommendationsH.pkl", "rb"))
    st.caption(f"{len(movies)} movies available")
else:
    movies = pickle.load(open("moviesB.pkl", "rb"))
    recommendations = pickle.load(open("recommendationsB.pkl", "rb"))
    st.caption(f"{len(movies)} movies available")

movie_list = movies["title"].values


# same recommend function: 
def recommend(movie):
    movie_index = movies[movies["title"] == movie].index[0]


    recommended_movies = []
#   recommended_posters = []

    for idx in recommendations[movie_index]:
        recommended_movies.append(
            movies.iloc[idx].title
        )
#       recommended_posters.append(fetch_poster(movies.iloc[i[0]].movie_id))       

    return recommended_movies

# function to fetch the poster from tmdb api. 
# posters - TMDB gives each movie an ID, use that to fetch its poster from their API. 
#def fetch_poster(movie_id):
#    url = f"https://api.themoviedb.org/3/movie/{movie_id}?api_key=770a1e13d80003a4246868e5276f3815"
#    print(url)
#    data = requests.get(url).json()
#
#    poster_path = data["poster_path"]
#    return "https://image.tmdb.org/t/p/w500" + poster_path # image url of the poster


# create a dropdown containing all 5000 movies and save our option in "movie"
movie = st.selectbox(
    "Select a movie:",
    movie_list
) 


# old way to show: 
#if st.button("Recommend"):
#    recommendations = recommend(movie)
#
#    for i in recommendations:
#        st.write(i)

st.markdown("---")
 
if st.button("Recommend"):
    st.subheader("Recommended for you:")

    with st.spinner("Finding similar movies..."):
        names = recommend(movie)

    col1, col2, col3, col4, col5 = st.columns(5)
    cols = [col1, col2, col3, col4, col5]

    for i in range(5):
        with cols[i]:
            st.markdown(f"""
            <div style="
                padding:20px;
                border-radius:12px;
                background:#294a3c;
                text-align:center;
                height:90px;
                display:flex;
                justify-content:center;
                align-items:center;
            ">
                {names[i]}
            </div>
            """, unsafe_allow_html=True)

# Another color option: #404a29 - oliv green
