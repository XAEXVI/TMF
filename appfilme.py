import tkinter as tk
from tkinter import *
from tkinter import ttk
from tkinter.ttk import *
from PIL import Image, ImageTk
from fam import search_movie_json
from fam import get_streaming_services
from fam import getposter
import requests
from io import BytesIO
#faz o programa existir (obrigatório)

root = tk.Tk()
root.title("Exemplo")
root.geometry("1620x868")
root.configure(bg="#17171a")

#search bar
frame = Frame(root, style="Custom.TFrame", width=588, height=25)
frame.place(x=380, y=20)


def perform_search(event=None):
    title = entry.get()
    spm_id, spm_title, spm_plot = search_movie_json(title)
    title_label.config(text=spm_title)  # Update the text of the title Label
    plot_label.config(text=spm_plot)  # Update the text of the plot Label

    poster_filename = getposter(spm_id)
    if poster_filename:
        display_poster(poster_filename)

    return spm_id, spm_title, spm_plot



def getposter(spm_id):
    url = f"https://api.themoviedb.org/3/movie/{spm_id}/images"

    headers = {
        "accept": "application/json",
        "Authorization": "Bearer eyJhbGciOiJIUzI1NiJ9.eyJhdWQiOiJhNGMyZWFhZmI2OGU5NjJjZWJiOTIzNzZhYzkxOWQxMSIsInN1YiI6IjY0NzA3MzNkYzVhZGE1MDEzNTgzZDM1NSIsInNjb3BlcyI6WyJhcGlfcmVhZCJdLCJ2ZXJzaW9uIjoxfQ.Kf8TJriIsbpJxRG7o5RPN5S4TkKIag2iY0FbjG_LbC4"
    }

    response = requests.get(url, headers=headers)

    data = response.json()
    if 'posters' in data and len(data['posters']) > 0:
        poster_path = data['posters'][0]['file_path']
        poster_url = f"https://image.tmdb.org/t/p/original{poster_path}"
        image_response = requests.get(poster_url)

        if image_response.status_code == 200:
            image_content = image_response.content
            image = Image.open(BytesIO(image_content))
            image.save('poster.png', 'PNG')
            return 'poster.png'

    return None


def display_poster(filename):
    # Remove previous poster label, if exists
    for widget in posterframe.winfo_children():
        widget.destroy()

    image = Image.open(filename)
    image = image.resize((440, 600), Image.LANCZOS)  # Use LANCZOS resampling
    photo = ImageTk.PhotoImage(image)
    label = tk.Label(posterframe, image=photo)
    label.image = photo
    label.pack()

entry = ttk.Entry(frame, background="#17171a")
entry.pack(side="left", padx=10, pady=10)
entry.bind("<Return>", perform_search)

#title
sfp = ttk.Style()
sfp.configure("Custom.TFrame", background="#17171a")

frame = Frame(root, style="Custom.TFrame", width=800, height=60)
frame.place(x=360, y=100)

title_label = Label(frame, text="", font=("Arial", 28), wraplength=1200, background="#17171a", foreground="white")
title_label.grid(padx=0, pady=60)

# Plot
plotframe = ttk.Frame(root, style="Custom.TFrame", width=640, height=380)
plotframe.place(x=360, y=230)

plot_label = ttk.Label(plotframe, text='', font=("Arial", 16), wraplength=600, background="#17171a", foreground="white")
plot_label.grid(padx=30, pady=30)

#Elenco
Elencoframe = ttk.Frame(root, style="Custom.TFrame", width=640, height=380)
Elencoframe.place(x=360, y=230)

Elenco_label = ttk.Label(Elencoframe, text='', font=("Arial", 16), wraplength=600, background="#17171a", foreground="white")
Elenco_label.grid(padx=10, pady=30)

#Titulos semelhantes

TSframe = Frame(root,style="Custom.TFrame", width=640, height=415)
TSframe.place(x=360, y=620)


#frame poster filme

spos = ttk.Style()
spos.configure("Custom.TFrame", background="#17171a")
posterframe = tk.Frame(root, width=440, height=600)
posterframe.place(x=1100, y=120)

INFOframe = Frame(root,style="Custom.TFrame", width=440, height=200)
INFOframe.place(x=1100, y=800)



# Add the plot label to the frame
# plot = Label(frame, text="Lorem Ipsum er rett og slett dummytekst fra og for trykkeindustrien. "
#                         "Lorem Ipsum har vært bransjens standard for dummytekst helt siden 1500-tallet, "
#                         "da en ukjent boktrykker stokket en mengde bokstaver for å lage et prøveeksemplar av en bok. "
#                         "Lorem Ipsum har tålt tidens tann usedvanlig godt, og har i tillegg til å bestå gjennom "
#                         "fem århundrer også tålt spranget over til elektronisk typografi uten vesentlige endringer. "
#                         "Lorem Ipsum ble gjort allment kjent i 1960-årene ved lanseringen av Letraset-ark med "
#                         "avsnitt fra Lorem Ipsum, og senere med sideombrekkingsprogrammet Aldus PageMaker "
#                         "som tok i bruk nettopp Lorem Ipsum for dummytekst.")
# plot.grid(padx=20, pady=20)


#botão  
# ttk.Button(frm, text="Quit", command=root.destroy).grid(column=1, row=0)

# # Create the first frame
# frame1 = ttk.Frame(root, width=400, height=300, relief="raised", padding=10)
# frame1.grid(row=0, column=0)

# # Add widgets to frame1
# label1 = ttk.Label(frame1, text="Frame 1")
# label1.pack()

# # Create the second frame
# frame2 = ttk.Frame(root, width=400, height=300, relief="raised", padding=10)
# frame2.grid(row=0, column=1)

# # Add widgets to frame2
# label2 = ttk.Label(frame2, text="Frame 2")
# label2.pack()

root.mainloop()
