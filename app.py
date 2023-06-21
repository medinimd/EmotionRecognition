import tensorflow as tf
import matplotlib.pyplot as plt
import cv2
import os
import numpy as np
from tensorflow.keras.preprocessing.image import ImageDataGenerator
from tensorflow.keras.preprocessing import image
#from emotion_recog import model_response()

from tkinter import *
import tkinter.messagebox
from PIL import ImageTk,Image 



class Student:
    def __init__(self,root):
        self.root = root
        self.root.title('Emotion classifier')
        self.root.geometry("750x500+0+0")
        self.root.config(bg='cadet blue')

        #MainFrame = Frame(self.root, bg='cadet blue')
        #MainFrame.grid()

        l = Label(root, text = "Emotion Classification System")
        l.config(font =("Courier", 30))
        l.pack()

        load = Image.open("angryface.jpg")
        render = ImageTk.PhotoImage(load)

        img = Label(self, image=render)
        img.image = render
        img.place(x=0, y=0)
    
        #DataFrame = Frame(MainFrame,bd=1,width=150,height=200,padx=20,pady=20,relief=RIDGE,bg='cadet blue')
        #DataFrame.pack(side=BOTTOM)
        
        #DataFrameLeft = LabelFrame(DataFrame,bd=1,width=1000,height=600,padx=20,relief=RIDGE,bg='light blue',font = ('arial',20,'bold'),text='Image display')
        #DataFrameLeft.pack(side=LEFT)




if __name__=='__main__':
    root = Tk()
    Student(root)
    root.mainloop()



'''
model=tf.keras.models.load_model('my_model2.hdf5')

dir_path = 'dataset/test/'


for i in os.listdir(dir_path ):
    img = image.load_img(dir_path+'//'+ i, target_size=(200,200))
    plt.imshow(img)
    plt.show()

    X = image.img_to_array(img)
    X = np.expand_dims(X,axis =0)
    images = np.vstack([X])

    val = model.predict(images)
    if val == 0:
        print("you are happy")
    else:
        print("you are not happy")
'''

