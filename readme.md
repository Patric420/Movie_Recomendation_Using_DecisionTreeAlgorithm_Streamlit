# Movie Recommender System


![Movie Recommender System](capture.png)

This project is a **Movie Recommender System** built using **Streamlit** and **scikit-learn**. It predicts movie recommendations based on user preferences such as age group, mood, and preferred genre.

## Features
- Users can select their **Age**, **Mood**, and **Preferred Genre**.
- The system uses a **Decision Tree Classifier** to recommend movies based on the given preferences.
- The dataset contains information about different movies, including age suitability, mood, genre, and movie recommendations.
- The system randomly selects a movie from the available recommendations based on the selected preferences.

## Requirements

To run this project locally, you will need the following Python libraries:

- `streamlit`
- `pandas`
- `scikit-learn`
- `matplotlib`
- `numpy`

You can install these dependencies using `pip`:

```bash
pip install -r requirements.txt
```

## Dataset 
**This project uses a CSV file called movie_recommender.csv. The dataset contains the following columns**
- `Age`: Age group of the user (Child, Teen, Adult, Senior)
- `Mood`: The user's mood (Happy, Sad, Excited, Relaxed)
- `Preferred Genre`: The user's preferred movie genre
- `Movie Recommendation`: The recommended movie for the selected preferences

## How to Use
 **Just follow the link :** `https://movie-recomendation-by-hakim-saoud.streamlit.app`

## How to download 

1. **Clone the repository to your local machine:**
    ```bash
        git clone (https://github.com/your-username/movie-recommender-system.git)
        cd movie-recommender-system
    ```

2. **Run the Streamlit app:**
    ```bash
        streamlit run app.py
    ```
3. **Enter your preferences:**
- Select your Age Group.
- Choose your Mood.
- Select your Preferred Genre.
- Click Recommend Movie to get a movie suggestion.

## Deployment
- You can deploy this app on Streamlit Cloud by linking your GitHub repository. This will allow users to interact with the recommender system directly from the web.





