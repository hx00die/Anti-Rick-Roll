import tkinter as tk
import urllib.request
import json
import urllib
import requests

def is_rick_rol(title):
    if "rick" in title or "Rick" in title or "Never" in title:
       return "Probably a rick roll\n"
    else:
        return "Probably not a rick roll\n"

def get_url_info(input_url):
    params = {"format": "json", "url": input_url}
    url = "https://www.youtube.com/oembed"
    query_string = urllib.parse.urlencode(params)
    url = url + "?" + query_string

    with urllib.request.urlopen(url) as response:
        response_text = response.read()
        data = json.loads(response_text.decode())
        return data

def button_pressed():
    input_url = entry.get()
    if 'thisworldthesedays'in input_url:
        label['text'] = 'probobly a rick roll'
    else:
        if 'youtube' not in input_url:
            input_url = requests.head(input_url).headers['location']
        result = get_url_info(input_url) 
        title = result["title"]
        channel = result["author_url"]
        answer = is_rick_rol(title)
        label['text'] = '{}Title: {}\nChannel: {}'.format(answer, title, channel)


HEIGHT = 500
WIDTH = 600

root = tk.Tk()
root.title("AntiRick-Roll")

canvas = tk.Canvas(root, height=HEIGHT, width=WIDTH)
canvas.pack()

background_image = tk.PhotoImage(file='landscape.png')
background_label = tk.Label(root, image=background_image)
background_label.place(relwidth=1, relheight=1)

frame = tk.Frame(root, bg='#80c1ff', bd=5)
frame.place(relx=0.5, rely=0.1, relwidth=0.75, relheight=0.1, anchor='n')

entry = tk.Entry(frame, font=40)
entry.place(relwidth=0.65, relheight=1)

button = tk.Button(frame, text="Check", font=40, command=button_pressed)
button.place(relx=0.7, relheight=1, relwidth=0.3)

lower_frame = tk.Frame(root, bg='#80c1ff', bd=10)
lower_frame.place(relx=0.5, rely=0.25, relwidth=0.75, relheight=0.6, anchor='n')

label = tk.Label(lower_frame, font=40)
label.place(relwidth=1, relheight=1)

root.mainloop()