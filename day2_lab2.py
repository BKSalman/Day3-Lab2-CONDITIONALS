movie = "some movie"

movie_rating = 3

movie_popularity_score = 72.65

if movie_rating >= 4 and int(movie_popularity_score )> 80:
	print("Highly recommended")
elif movie_rating >= 3 and int(movie_popularity_score) > 70:
	print("I recommended it . It is good")
elif movie_rating >= 2 and int(movie_popularity_score) > 60:
	print("You should check it out!")
elif movie_rating >= 2 and int(movie_popularity_score) > 50:
	print("Don't watch it. It is a waste of time")
