import tkinter as tk
import requests
from bs4 import BeautifulSoup

# function to search lyrics
def search_lyrics():
    # get the song name from the user input
    song_name = entry.get()
    # search the lyrics using the song name
    url = f'https://www.azlyrics.com/lyrics/{song_name.replace(" ", "")}.html'
    page = requests.get(url)
    soup = BeautifulSoup(page.content, 'html.parser')
    # extract the lyrics and the source
    lyrics_div = soup.find_all('div', class_='col-xs-12 col-lg-8 text-center')[0]
    lyrics = lyrics_div.find_all('div')[6].get_text()
    source = url
    # display the lyrics and the source
    result_label.config(text=lyrics)
    source_label.config(text=f"Source: {source}")

# create the GUI
root = tk.Tk()
root.title("Lyrics Search")
root.geometry("400x300")

# create the widgets
label = tk.Label(root, text="Enter a song name:")
label.pack(pady=10)
entry = tk.Entry(root, width=30)
entry.pack(pady=10)
search_button = tk.Button(root, text="Search Lyrics", command=search_lyrics)
search_button.pack(pady=10)
result_label = tk.Label(root, wraplength=380, justify='left', anchor='w')
result_label.pack(pady=10)
source_label = tk.Label(root, fg='blue', cursor='hand2')
source_label.pack()

# run the GUI
root.mainloop()
