import streamlit as st
import pickle

# Load data
movies = pickle.load(open('movies.pkl', 'rb'))
similarity = pickle.load(open('similarity.pkl', 'rb'))

def recommend(movie):
    # Get index of selected movie
    index = movies[movies['title'] == movie].index[0]
    distances = similarity[index]

    # Get top 5 similar movies (excluding the movie itself)
    movie_list = sorted(list(enumerate(distances)), reverse=True, key=lambda x: x[1])[1:6]

    return [movies.iloc[i[0]].title for i in movie_list]

# --- UI ---
st.title("🎬 Movie Recommendation System By Aditya Sony")

# Dropdown to select movie
selected_movie = st.selectbox("Choose a movie", movies['title'].values)

# Button to recommend movies
if st.button("Recommend"):
    recommended_movies = recommend(selected_movie)

    st.subheader("Recommended Movies:")

    # Display recommendations in 5 columns
    cols = st.columns(5)
    for i, col in enumerate(cols):
        with col:
            st.markdown(f"**{recommended_movies[i]}**")