
import tkinter as tk
from PIL import Image, ImageTk, ImageSequence
import subprocess
import sys

class StartWindow:
    def __init__(self, root):
        self.root = root
        self.root.title("Start Window")

        self.canvas = tk.Canvas(root, width=600, height=600)
        self.canvas.pack()

        # Load the GIF using PIL
        gif_path = "cbir.gif"
        self.gif = Image.open(gif_path)
        self.frames = [ImageTk.PhotoImage(frame) for frame in ImageSequence.Iterator(self.gif)]

        self.current_frame = 0
        self.update_background()

        self.button1 = tk.Button(root, text="Text based image search", font=("Helvetica", 16),
                                 command=self.open_program1, relief=tk.RAISED, borderwidth=4)
        self.button1.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=-50)

        self.button2 = tk.Button(root, text="Image based image search", font=("Helvetica", 16),
                                 command=self.open_program2, relief=tk.RAISED, borderwidth=4)
        self.button2.place(relx=0.5, rely=0.5, anchor=tk.CENTER, y=50)

    def update_background(self):
        self.canvas.create_image(0, 0, anchor=tk.NW, image=self.frames[self.current_frame])
        self.current_frame = (self.current_frame + 1) % len(self.frames)
        self.root.after(100, self.update_background)  # Update every 100 ms

    def open_program1(self):
        subprocess.run(["python", "main.py"])

    def open_program2(self):
        subprocess.run(["python", "2.py"])


if __name__ == "__main__":
    start_root = tk.Tk()
    start_app = StartWindow(start_root)
    print(sys.path)
    start_root.mainloop()



