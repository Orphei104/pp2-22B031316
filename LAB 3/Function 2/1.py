import math
# Dictionary of movies

movies = [
{
"name": "Usual Suspects",
"imdb": 7.0,
"category": "Thriller"
},
{
"name": "Hitman",
"imdb": 6.3,
"category": "Action"
},
{
"name": "Dark Knight",
"imdb": 9.0,
"category": "Adventure"
},
{
"name": "The Help",
"imdb": 8.0,
"category": "Drama"
},
{
"name": "The Choice",
"imdb": 6.2,
"category": "Romance"
},
{
"name": "Colonia",
"imdb": 7.4,
"category": "Romance"
},
{
"name": "Love",
"imdb": 6.0,
"category": "Romance"
},
{
"name": "Bride Wars",
"imdb": 5.4,
"category": "Romance"
},
{
"name": "AlphaJet",
"imdb": 3.2,
"category": "War"
},
{
"name": "Ringing Crime",
"imdb": 4.0,
"category": "Crime"
},
{
"name": "Joking muck",
"imdb": 7.2,
"category": "Comedy"
},
{
"name": "What is the name",
"imdb": 9.2,
"category": "Suspense"
},
{
"name": "Detective",
"imdb": 7.0,
"category": "Suspense"
},
{
"name": "Exam",
"imdb": 4.2,
"category": "Thriller"
},
{
"name": "We Two",
"imdb": 7.2,
"category": "Romance"
}
]

def is_above_5_5(movie):
    return movie["imdb"] > 5.5

def filter_movies(moviess):
    return [movie for movie in moviess if is_above_5_5(movie)]

def is_high_score(movie):
    return movie['imdb'] > 5.5

high_score_movies = list(filter(is_high_score, movies))
print(high_score_movies)

def by_category(category):
    return [movie for movie in movies if movie['category'] == category]

action_movies = by_category('Action')
print(action_movies)

def avg_score(moviesss):
    scores = [movie['imdb'] for movie in moviesss]
    return math.floor(sum(scores) / len(scores))

print(avg_score(high_score_movies))

def avg_category_score(category):
    category_movies = by_category(category)
    return avg_score(category_movies)

print(avg_category_score('Action'))

