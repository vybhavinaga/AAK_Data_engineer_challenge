# Spotify Music Analysis - ETL and EDA

This project performs ETL (Extract, Transform, Load) and Exploratory Data Analysis (EDA) on a Spotify songs dataset. The goal is to explore music attributes, listener interaction, and patterns in track popularity using both raw and engineered features.

---

## Dataset

- Source: [Spotify Dataset](https://www.kaggle.com/datasets/sanjanchaudhari/spotify-dataset)
- Size: 20,594 tracks
- Features include:
  - Audio attributes: Danceability, Energy, Acousticness, Valence, Tempo, etc.
  - Popularity metrics: views, likes, comments
  - Metadata: track, artist, channel, most_playedon

---

## ETL Process

- Loaded dataset and inspected shape, data types, and missing values
- Dropped unnecessary columns and handled missing values
- Standardised categorical fields like Artist names and track titles

---

## Feature Engineering

- engagement_rate =(Likes + Comments ) / Views
- mood_score = Valence * Energy
- danceability_score = Danceability * Tempo

---

## EDA

The following visualisations and insights were produced:
- Top 10 Most Viewed and Liked tracks : to identify popular content.
- Correlation Heat map : views and likes are strongly correlated. Mood and danceability show weak correlation with popularity.
-  Track Duration distribution : most songs are 2 to 5 minutes
-  Box and Violin plots : engagement rate tends to decrease as popularity increases; mood scores are centered in a moderate range
-  Word Cloud of Track Titles : highlights common terms

---

### Real World Applications

Top viewed and liked tracks help streaming platforms and marketers identify trending content. Track duration analysis can guide music producers to align with industry norms for better listener retention. Correlation heatmaps assist data scientists in selecting predictive features for recommendation systems. Engagement rate analysis can uncover niche tracks with loyal listeners, useful for targeted marketing. Mood, danceability, and word cloud visualizations support playlist curation, therapeutic music apps, and naming trend analysis.

---

## Conclusion

This project demonstrates how structured EDA and thoughtful feature engineering can uncover patterns in music datasets.

---

## Usage Instructions

1. Clone or download this repository to the local machine
2. Ensure Python 3.x is installed along with following libraries:
   - pandas
   - numpy
   - matplotlib
   - seaborn
   - wordcloud
3. Open the notebook file in Jupiter and run all cells.
4. Use the dataset provided in the repository. If you choose to download the dataset from the link mentioned in the Dataset section, save it in your working directory and rename it to spotify_dataset.
5. Providing a pdf version of the notebook for a quick preview.

---

