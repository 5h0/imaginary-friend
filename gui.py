import tkinter as tk
from PIL import Image, ImageTk
from itertools import count


class ImageLabel(tk.Label):
    """
   Class that displays moving gifs.
   """

    def load(self, im):
        if isinstance(im, str):
            im = Image.open(im)

        self.loc = 0
        self.frames = []

        try:
            for i in count(1):
                self.frames.append(ImageTk.PhotoImage(im.copy()))
                im.seek(i)
        except EOFError:
            pass

        try:
            self.delay = im.info['duration']
        except:
            self.delay = 100

        if len(self.frames) == 1:
            self.config(image=self.frames[0])
        else:
            self.next_frame()

    def unload(self):
        self.config(image=None)
        self.frames = None

    def next_frame(self):
        if self.frames:
            self.loc += 1
            self.loc %= len(self.frames)
            self.config(image=self.frames[self.loc])
            self.after(self.delay, self.next_frame)


def gif():
    root = tk.Tk()
    label = ImageLabel(root)
    label.pack()
    label.load('MxTk.gif')
    root.mainloop()


def image():
    root = tk.Tk()
    my_image = tk.PhotoImage(file="MxTk.gif")
    label = tk.Label(image=my_image)
    label.pack()
    root.mainloop()