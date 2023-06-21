from tkinter import *

# pip install pillow
from PIL import Image, ImageTk

class Window(Frame):
    def __init__(self, master=None):
        Frame.__init__(self, master)
        self.master = master
        self.pack(fill=BOTH, expand=1)

        
        label = Label( root, text="hello")
        label.config(font=("Courier", 44))
        label.place(x=0,y=5)
        
        load = Image.open("angryface.jpg")
        load = load.resize((100, 100))
        render = ImageTk.PhotoImage(load)
        img = Label(self, image=render)
        img.image = render
        img.place(x=30, y=40)

        
root = Tk()
app = Window(root)
root.wm_title("Emotion classifier")
root.geometry("1000x1000")
root.config(bg='cadet blue')
root.mainloop()
