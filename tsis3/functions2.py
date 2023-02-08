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


def is_above_deadline(film_data):
    if film_data['imdb'] > 5.5:
        return True
    return False

def check_category(film_data, category):
    if film_data['category'] == category:
        return True
    return False

def make_list_of_good_movies(film_data):
    res = []
    for i in film_data:
        if is_above_deadline(i):
            res.append(i)
    return res

def find_category(film_data, category):
    res = []
    for i in film_data:
        if check_category(i, category):
            res.append(i)
    return res

def average_imdb(film_data):
    counter = 0
    summ = 0
    for i in film_data:
        summ += i['imdb']
        counter += 1
    return summ / counter

def average_imdb_per_category(film_data, category):
    counter = 0
    summ = 0
    for i in film_data:
        if check_category(i, category):
            summ += i['imdb']
            counter += 1
    return summ / counter
            


print(is_above_deadline(movies[0]))
print(make_list_of_good_movies(movies))
print(check_category(movies[-1],'Romance'))
print(find_category(movies, 'Romance'))
print(average_imdb(movies))
print(average_imdb_per_category(movies, 'Romance'))