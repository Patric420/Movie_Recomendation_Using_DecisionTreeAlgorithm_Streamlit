# Base Python image
FROM python:3.13.2-slim

# Set working directory
WORKDIR /app

# Copy files into container
COPY . /app

# Install dependencies
RUN pip install --no-cache-dir streamlit pandas scikit-learn numpy

# Expose Streamlit default port
EXPOSE 8501

# Run Streamlit app
CMD ["streamlit", "run", "movie_recommender.py", "--server.port=8501", "--server.address=0.0.0.0"]
