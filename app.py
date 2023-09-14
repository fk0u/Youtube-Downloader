import tkinter as tk
from tkinter import ttk
from tkinter import messagebox
from pytube import YouTube
import os

def download_video():
    video_url = link_entry.get()
    resolution = resolution_var.get()
    is_mp3 = mp3_var.get()
    
    # Path ke direktori output yang ditentukan
    output_path = "C:\\download\\youtube_downloader"

    try:
        yt = YouTube(video_url)

        if is_mp3:
            audio_stream = yt.streams.filter(only_audio=True).first()
            audio_stream.download(output_path=output_path)
        else:
            video_stream = yt.streams.filter(res=resolution).first()
            video_stream.download(output_path=output_path)

        messagebox.showinfo("Download Complete", "Downloaded successfully!")
    except Exception as e:
        messagebox.showerror("Error", str(e))

app = tk.Tk()
app.title('YouTube Downloader')

frame = ttk.Frame(app)
frame.grid(column=0, row=0, padx=20, pady=20, sticky=(tk.W, tk.E))

link_label = ttk.Label(frame, text='YouTube Video URL:')
link_label.grid(column=0, row=0, sticky=tk.W)

link_entry = ttk.Entry(frame, width=50)
link_entry.grid(column=1, row=0)

resolution_label = ttk.Label(frame, text='Select Resolution:')
resolution_label.grid(column=0, row=1, sticky=tk.W)

resolutions = ['highest', '720p', '480p']
resolution_var = tk.StringVar()
resolution_var.set('highest')

resolution_combobox = ttk.Combobox(frame, textvariable=resolution_var, values=resolutions)
resolution_combobox.grid(column=1, row=1)

mp3_var = tk.BooleanVar()
mp3_checkbox = ttk.Checkbutton(frame, text='Download as MP3', variable=mp3_var)
mp3_checkbox.grid(column=0, row=2, columnspan=2, sticky=tk.W)

download_button = ttk.Button(frame, text='Download', command=download_video)
download_button.grid(column=1, row=3, pady=10)

frame.columnconfigure(1, weight=1)

app.mainloop()
