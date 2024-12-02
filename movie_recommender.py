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

counter_file = "visit_counter.txt"

# Initialize or update visit counter
if not os.path.exists(counter_file):
    with open(counter_file, "w") as f:
        f.write("0")

with open(counter_file, "r") as f:
    visit_count = int(f.read())

visit_count += 1

with open(counter_file, "w") as f:
    f.write(str(visit_count))

st.title("Movie Recommender Machine Learning System")
st.header("Get a Movie Recommendation Based on Your Preferences")

st.write(f"**This page has been visited {visit_count} times.**")


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
st.markdown(
    """
    ---
    ## Connect with me on [LinkedIn](https://www.linkedin.com/in/your-profile)
    """,
    unsafe_allow_html=True
)
