import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip
import os

videoPath = ""


def chooseFile():
    global videoPath
    fileName = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("videos", "*.mp4"), ("all files", "*.*")),
    )
    videoPath = fileName
    convertFileBtn["state"] = tk.NORMAL


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


root = tk.Tk()

frame = tk.Frame(root, pady=10, padx=10)
frame.grid()

chooseFileBtn = tk.Button(frame, text="Choose video file", command=chooseFile)
chooseFileBtn.grid(column=0, row=0)

convertFileBtn = tk.Button(
    frame, text="Convert to mp3", command=convertVideo, state=tk.DISABLED
)
convertFileBtn.grid(column=1, row=0)

root.mainloop()
