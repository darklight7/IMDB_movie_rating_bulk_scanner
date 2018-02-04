import os,requests, sys, webbrowser, bs4
from requests import get
from bs4 import BeautifulSoup
import pandas as pd
import sys, csv ,operator


root, dirs, files = os.walk(r'''H:\Movies''').__next__()
print (dirs)

l=len(dirs)
names=[]
rating=[]
for i in range (0,l):
    x=dirs[i];

    x=x[0:40]


    print('Googling...')
    res = requests.get('http://google.com/search?q=' + ''.join(x)+' imdb rating')
    print('http://google.com/search?q=' + ''.join(x)+' imdb rating')
    response = requests.get('http://google.com/search?q=' + ' '.join(x)+' imdb')
    html_soup = BeautifulSoup(response.text, 'html.parser')
    type(html_soup)
    movie_containers = html_soup.find_all('div', class_='s')
    first_movie = movie_containers[0]
    first_name = first_movie.text
    first_name=first_name[52:55]
    print(first_name)
    names.append(x)
    rating.append(first_name)
    res.raise_for_status()
movie = pd.DataFrame({'Movie': names,
                            'Ratings': rating})
movie=movie.sort_values(by=['Ratings'],ascending=False)
print(movie)
movie.to_csv('movie.csv')
