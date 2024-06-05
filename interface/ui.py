import tkinter as tk
from tkinter import filedialog, messagebox
from app.transcriber import transcribe_audio

def select_file():
    file_path = filedialog.askopenfilename()
    if file_path:
        transcript = transcribe_audio(file_path)
        messagebox.showinfo("Transcripción", transcript)

root = tk.Tk()
root.title("Transcriptor de Audio")

btn = tk.Button(root, text="Seleccionar Archivo de Audio", command=select_file)
btn.pack()

root.mainloop()

