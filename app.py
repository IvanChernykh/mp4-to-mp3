import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import os

videoPath = ""

defaultTitleText = "Please, select video file"


def chooseFile():
    global videoPath
    fileName = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("videos", "*.mp4"), ("all files", "*.*")),
    )
    if fileName.endswith("mp4"):
        videoPath = fileName
        convertFileBtn["state"] = tk.NORMAL
        title["text"] = "Now convert to mp3"
    else:
        title["text"] = "Wrong format!"


def convertVideo():
    global videoPath
    convertFileBtn["state"] = tk.DISABLED
    audioPath = os.path.basename(videoPath)[:-4] + ".mp3"
    videoFile = VideoFileClip(videoPath)

    audioFile = videoFile.audio
    audioFile.write_audiofile(audioPath)
    videoFile.close()
    audioFile.close()
    videoPath = ""
    title["text"] = defaultTitleText


root = tk.Tk()
root.title("mp3 converter")


frame = tk.Frame(root, pady=20, padx=20)
frame.grid()

title = tk.Label(frame, text=defaultTitleText)
title.grid(column=0, row=0, columnspan=2)

chooseFileBtn = tk.Button(frame, text="Choose file", command=chooseFile)
chooseFileBtn.grid(column=0, row=1)

convertFileBtn = tk.Button(
    frame, text="Convert to mp3", command=convertVideo, state=tk.DISABLED
)
convertFileBtn.grid(column=1, row=1)

root.mainloop()
