import streamlit as st
import pandas as pd
from sklearn.tree import DecisionTreeClassifier
import numpy as np
import os

df = pd.read_csv('movie_recommender.csv')

df_encoded = pd.get_dummies(df, columns=['Age', 'Mood', 'Preferred Genre'])
X = df_encoded.drop(columns=['Movie Recommendation'])
y = df['Movie Recommendation']

model = DecisionTreeClassifier(random_state=42)
model.fit(X, y)



st.title("Movie Recommender Machine Learning System")
st.header("Get a Movie Recommendation Based on Your Preferences")
age = st.selectbox('Select Age Group', ['Child', 'Teen', 'Adult', 'Senior'])
mood = st.selectbox('Select Mood', ['Happy', 'Sad', 'Excited', 'Relaxed'])
preferred_genre = st.selectbox('Select Preferred Genre', ['Comedy', 'Action', 'Romance', 'Drama', 'Animation', 'Adventure', 'Horror', 'Documentary', 'Thriller'])

user_input = {
    'Age': age,
    'Mood': mood,
    'Preferred Genre': preferred_genre
}

user_input_encoded = pd.DataFrame([user_input])
user_input_encoded = pd.get_dummies(user_input_encoded)
user_input_encoded = user_input_encoded.reindex(columns=X.columns, fill_value=0)

if st.button('Recommend Movie'):
    if user_input['Age'] != 'Child':
        movie_choices = df[(df['Age'] == user_input['Age']) & 
                           (df['Mood'] == user_input['Mood']) & 
                           (df['Preferred Genre'] == user_input['Preferred Genre'])]['Movie Recommendation'].unique()
    else:
        movie_choices = df[(df['Age'] == user_input['Age']) & 
                           (df['Mood'] == user_input['Mood']) & 
                           (df['Preferred Genre'] == user_input['Preferred Genre']) & 
                           (df['Preferred Genre'] != 'Horror')]['Movie Recommendation'].unique()
    if len(movie_choices) > 0:
        recommended_movie = np.random.choice(movie_choices)
        st.session_state.recommended_movie = recommended_movie
        st.write(f"**Recommended Movie:** {recommended_movie}")
    else:
        st.write("No movies available for the selected options.")
