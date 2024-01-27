import tkinter as tk
from tkinter import filedialog
from moviepy.editor import VideoFileClip

videoPath = ""


def chooseFile():
    global videoPath
    fileName = filedialog.askopenfilename(
        initialdir="/",
        title="Select file",
        filetypes=(("videos", "*.mp4"), ("all files", "*.*")),
    )
    videoPath = fileName
    print(fileName.title())


def convertVideo():
    audioPath = videoPath[:-4] + ".mp3"

    videoFile = VideoFileClip(videoPath)

    audioFile = videoFile.audio
    audioFile.write_audiofile(audioPath)
    videoFile.close()
    audioFile.close()


root = tk.Tk()

frame = tk.Frame(root, pady=10, height=50)
frame.grid()

chooseFileBtn = tk.Button(root, text="Choose video file", command=chooseFile).grid(
    column=0, row=0
)
convertFileBtn = tk.Button(root, text="Convert to mp3", command=convertVideo).grid(
    column=1, row=0
)

root.mainloop()
