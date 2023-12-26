# Importing pandas and matplotlib
import pandas as pd
import matplotlib.pyplot as plt

# Start coding!
netflix_df = pd.read_csv(r"C:\Users\vtvis\Documents\netflix_data.csv",index_col= 0)
netflix_subset = netflix_df[netflix_df["type"] == "Movie"]
netflix_movies = netflix_subset[['title','country','genre','release_year','duration']]
short_movies = netflix_movies[netflix_movies['duration']< 60]
print(short_movies.head())
colors = []
for lab, row in netflix_movies.iterrows():
    if row['genre'] == 'Children':
        colors.append("orange")
    elif row['genre'] == "Documentaries":
        colors.append("red")
    elif row['genre'] == 'Stand-Up':
        colors.append("blue")
    else:
        colors.append('black')
fig = plt.figure(figsize=(12,8))
plt.scatter(netflix_movies['release_year'],netflix_movies['duration'], c = colors)
plt.xlabel('Release year')
plt.ylabel('Duration (min)')
plt.title('Movie Duration by Year of Release')
plt.show()

# Answering the question
answer = 'maybe'
