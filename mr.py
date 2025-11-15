import numpy as np
import pandas as pd
import ast  #! module to convert string into list

import pickle

from nltk.stem.porter import PorterStemmer

from sklearn.feature_extraction.text import CountVectorizer

from sklearn.metrics.pairwise import cosine_similarity



ps=PorterStemmer()

movies=pd.read_csv('tmdb_5000_movies.csv')
credits=pd.read_csv('tmdb_5000_credits.csv')

movies=movies.merge(credits,on='title')   #!merging two data set to deal with the data more easily

# print(movies.info())

movies=movies[['movie_id','title','overview','genres','keywords','cast','crew']]  #! extracted needed  columns from the dataset


# print(movies.isnull().sum())

movies.dropna(inplace=True)   #!used to drop null values

def convert(obj):
    movie_list=[]
    for i in ast.literal_eval(obj):
        movie_list.append(i['name'])
    return movie_list


def convert2(obj):
    movie_list=[]
    counter=0
    for i in ast.literal_eval(obj):
        if( counter!=0):

            movie_list.append(i['name'])
            counter+=1
        else:
            break
    return movie_list

def convert3(obj):
    movie_list=[]
 
    for i in ast.literal_eval(obj):
        if(i['job']=='Director'):
            movie_list.append(i['name'])
            break
    return movie_list

def stem(text):
    y=[]
    for i in text.split():
        y.append(ps.stem(i))

        return " ".join(y)
    
def recommend(movie):
    movie_index=new_dataset[new_dataset['title']=='movie'].index[0]

    distance=similiar[movie_index]

    movie_list=sorted(list(enumerate(distance)),reverse=True,key=lambda x:x[1])[1:6]

    for i in movie_list:
        new_dataset.iloc[i[0]].title


movies['genres']=movies['genres'].apply(convert)
movies['keywords']=movies['keywords'].apply(convert)
movies['cast']=movies['cast'].apply(convert2)
movies['crew']=movies['crew'].apply(convert3)
movies['overview']=movies['overview'].apply(lambda x:x.split())

movies['genres']=movies['genres'].apply(lambda x:[i.replace(" ","") for i in x])
movies['keywords']=movies['keywords'].apply(lambda x:[i.replace(" ","") for i in x])
movies['cast']=movies['cast'].apply(lambda x:[i.replace(" ","") for i in x])
movies['crew']=movies['crew'].apply(lambda x:[i.replace(" ","") for i in x])





movies['tags']=movies['overview']+movies['genres']+movies['keywords']+movies['cast']+movies['crew']


new_dataset=movies[['movie_id','title','tags']]

new_dataset['tags']=new_dataset['tags'].apply(lambda x:" ".join(x))
new_dataset['tags']=new_dataset['tags'].apply(lambda x:x.lower())
new_dataset['tags']=new_dataset['tags'].apply(stem)


# print(new_dataset.head())

count_vector=CountVectorizer(max_features=5000,stop_words='english')

vector=count_vector.fit_transform(new_dataset['tags']).toarray()

# print(vector)
print(new_dataset['title'].values)

similiar=cosine_similarity(vector)

pickle.dump(new_dataset,open('movie1.pkl','wb'))

pickle.dump(similiar,open('similiar.pkl','wb'))





