import pandas as pd
df = pd.read_csv("miniproject/netflix/netflix_titles.csv")
# print(df.head())
# print(df.info())
# print(df.shape)

# print(df.isnull().sum())

df = df.fillna({"director": "name missing", "country" : "unknown", "cast":"unknown" , "rating":"unknown" , "duration":"unknown", "date_added":"00/00/0000" })

# print(df[['rating','duration','cast','country','date_added']].head(5))
df['date_added'] = pd.to_datetime(df['date_added'] , errors = 'coerce')




print("QUES1: How many movies and how many TV shows are there")
print("Total Movies:", df['type'].value_counts().get('Movie'))
print("Total TV Shows:", df['type'].value_counts().get('TV Show'))

print("QUES2: What are the top 10 countries with most Netflix content?")
ct = df[df["country"] != "unknown"]
country_counts = ct["country"].value_counts()
top10 = country_counts.head(10)
print(top10)


print("QUES3: What are the most common genres?")
genre_counts = df['listed_in'].value_counts()
print( genre_counts.head(1))

print("QUES4: What is the trend of content added over the years?")
df["year_added"] = df["date_added"].dt.year
yearly_counts = df["year_added"].value_counts().sort_index()
print(yearly_counts)

print("QUES5: Who are the top 10 most frequent directors?")
filterdf1 = df[df['director'] != "name missing"]
director = filterdf1["director"].value_counts()
print(director.head(10))


print("Ques: Show all Indian movies released after 2015.")
indianmovie = df[(df["country"] == "India") & (df["release_year"] >= 2015)]
print(indianmovie[["title", "release_year"]].head())
print("Total indian movie released after 2015 is: ", len(indianmovie))
      


print("Find all shows (movies/TV) with a duration longer than 90 minutes.")
movies = df[(df["type"] == "Movie") & (df["duration"] != "unknown")].copy()
movies["duration_min"] = movies["duration"].str.replace(" min" , "").astype(int)
mv90 = movies[movies["duration_min"] >= 90]
print(mv90[["title" , "duration"]].head())
print("Total movies having duration atleast 90 minutes are:", len(mv90))


print("List all content where the title contains the word Love")
love_titles = df[df['title'].str.contains('love', case=False, na=False)]
print(love_titles[['title', 'type', 'release_year']].head())
print("Total titles containing 'Love':", len(love_titles))


print("Group content by year and show the count")
print(df.groupby("release_year").count())








# print(df.info())
# print(df.head(5))