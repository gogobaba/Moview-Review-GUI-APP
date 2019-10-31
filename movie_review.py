import tkinter as tk
from tkinter import font
from PIL import Image
from PIL import ImageTk
from Movies import Movie
import requests
import json
from checkInternet import is_connected
from Movies import Movie
import sqlite3

#omdb api -> https://www.omdbapi.com/?i=tt3896198&apikey=e120531a



HEIGHT = 600
WIDTH = 600
REMOTE_SERVER = 'www.google.com'



def format_response(data):


    Title = data['Title']
    imdbRating = data['imdbRating']
    Rated = data['Rated']
    Released = data['Released']
    Runtime = data['Runtime']
    Genre = data['Genre']
    Actors = data['Actors']
    Director = data['Director']
    Country = data['Country']
    Plot = data['Plot']
    new_movie = Movie(Title,imdbRating,Rated,Released,Runtime,Genre,Actors,Director,Country,Plot)

    return new_movie.get_str()


def test_function(entry_text):
    if(is_connected(REMOTE_SERVER)):
        r = requests.get('https://www.omdbapi.com/?i=tt3896198&apikey=e120531a&t={}'.format(entry_text))
        data = json.loads(r.text)
        format_response(data)
        label['text'] = format_response(data)
    else:
        label['text'] = 'Cant Connect to internet'


    
    

root = tk.Tk()

canvas = tk.Canvas(root,height=HEIGHT,width=WIDTH)
canvas.pack()

background_image = ImageTk.PhotoImage(Image.open('logo.jpg'))
background_label = tk.Label(root,image=background_image)
background_label.place(relwidth=1,relheight=1)

frame = tk.Frame(root,bg='skyblue',bd=2)
frame.place(relx = 0.5,rely=0.1,relwidth=0.75,relheight=0.1,anchor='n')

entry = tk.Entry(frame,font=40)
entry.place(relwidth=0.65,relheight=1)

button = tk.Button(frame,font=40,text='Search',bg='beige',command=lambda : test_function(entry.get()))
button.place(relx=0.68,relwidth=0.32,relheight=1)

lower_frame = tk.Frame(root,bg='skyblue',bd=10)
lower_frame.place(relx=0.5,rely=0.25,relwidth=0.75,relheight=0.7,anchor='n')

label = tk.Label(lower_frame,font=('Courier',14),wraplength=400,justify='left',anchor='nw',fg='Orange')
label.place(relwidth=1,relheight=1)

root.mainloop()

