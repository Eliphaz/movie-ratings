"""Restaurant rating lister."""


# put your code here
ratings = open("scores.txt").read().split('\n')
ratings_dct = {}
index = 1
for i in ratings:
    ratings_dct[i.split(':')[0]] = (i.split(':')[1])
    index += 1
print(ratings_dct)

entermovie = input('would you like to enter a movie? (y/n) ')

if entermovie != 'y' and entermovie != 'n':
    print('please enter a y or n')
    entermovie = input('would you like to enter a movie? (y/n) ')
if entermovie == 'n':
    pass
if entermovie == 'y':
    movie_name = input('what is the name of your film: ')
    movie_rating = input(f'what would you rate {movie_name} out of 5: ')
    while int(movie_rating) > 5 or int(movie_rating) < 0:
        print('please enter a number less than 5 and greater than 0')
        movie_rating = input(f'what would you rate {movie_name} out of 5: ')
    ratings_dct[movie_name] = movie_rating

sortednames = sorted(ratings_dct, key=lambda x: x.lower())
sorted_ratings = {}
for i in sortednames:
    sorted_ratings[i] = ratings_dct[i]

for k, v in sorted_ratings.items():
    print(f'the movie {k} is rated at {v}/5')
