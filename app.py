from tkinter import *
import argparse
import FaceTransfer as ft
from PIL import Image, ImageTk

parser = argparse.ArgumentParser(description='Controle de transferência de estilo.',
                                 formatter_class=argparse.ArgumentDefaultsHelpFormatter)
add_arg = parser.add_argument
add_arg('--content',        default=None, type=str,         help='Image de conteúdo.')
add_arg('--style',        default=None, type=str,         help='Imagem de estilo.')
args = parser.parse_args()

master = Tk()

image = Image.open('./images/output.jpg')
photo = ImageTk.PhotoImage(image)
photo_label = Label(image=photo)
photo_label.image = photo # keep a reference!

def display_image():
    #Update the GUI image    
    image = Image.open('./images/output.jpg')
    photo = ImageTk.PhotoImage(image)        
    photo_label.configure(image=photo)
    photo_label.image = photo
    
    
    master.after(1000, display_image)
    
def update_style(name, value):
    #Update the style
    face_transfer.new_style(name, value, args.content, args.style)
    
def run():        
        
    photo_label.pack()        
    for scale in ('hair', 'skin', 'eyebrows', 'eyes', 'nose', 'beard', 'ears', 'mouth'):
            
        label = Label(master)
        label.config(text = scale)
        
        
        widget = Scale(master, from_=0, to=3, orient="horizontal",
                          command=lambda value, name=scale: update_style(name, value))
        
        label.pack(side=LEFT)
        widget.pack(side=LEFT)
                
    master.after(1000, display_image)
    mainloop()

face_transfer = ft.FaceTransfer(args.content, args.style)    
run()        
    
    
