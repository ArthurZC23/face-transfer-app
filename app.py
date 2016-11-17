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

def change_content(e):
        
    name = content_listbox.get(content_listbox.curselection()).split(' ')[0]
    face_transfer.load_content(name)
    
    
def change_style(e):
    
    name = style_listbox.get(style_listbox.curselection()).split(' ')[0]
    face_transfer.load_style(name)
    
def reset():
    for widget in scale_list:
        widget.set(0)
    

def display_image():
    #Update the GUI image    
    image = Image.open('./images/output.png')
    photo = ImageTk.PhotoImage(image)        
    photo_label.configure(image=photo)
    photo_label.image = photo        
    master.after(1000, display_image)
    
def update_texture(name, value):
        
    #Update the style
    face_transfer.change_texture(name, value, args.content, args.style)    

face_transfer = ft.FaceTransfer(args.content, args.style)    

#GUI
master = Tk()

#Frames
frame = Frame(master)
frame.pack()
bottomframe = Frame(master)
bottomframe.pack(side = BOTTOM )

#Images
image = Image.open('./images/output.png')
photo = ImageTk.PhotoImage(
    image)
photo_label = Label(frame, image=photo)
photo_label.image = photo # keep a reference!
photo_label.pack()        
#Scales
scale_list = []
for scale in ('hair', 'skin', 'eyebrows', 'eyes', 'nose', 'beard', 'ears', 'mouth'):            
    label = Label(frame)
    label.config(text = scale)                
    widget = Scale(frame, from_=0, to=6, orient="horizontal",
                      command=lambda value, name=scale: update_texture(name, value))        
    label.pack(side=LEFT)
    widget.pack(side=LEFT)
    scale_list.append(widget)

#Listbox    
label = Label(bottomframe)
label.config(text = 'content')                
label.pack(side=LEFT)
content_listbox = Listbox(bottomframe)
content_listbox.pack(side = LEFT)   
for item in ["Arthur", "Matheus", "Sergio"]:
    content_listbox.insert(END, item)  
content_listbox.bind('<<ListboxSelect>>', change_content)

label = Label(bottomframe)
label.config(text = 'style')                
label.pack(side=LEFT)
style_listbox = Listbox(bottomframe)
style_listbox.pack(side = LEFT)   
for item in ["Morgan Freeman", "Brad Pitt", "Channing Tatum", \
            'Michael Jackson']:
    style_listbox.insert(END, item)                 
style_listbox.bind('<<ListboxSelect>>', change_style)

#Button
b = Button(bottomframe, text="Reset", command=reset)
b.pack(side=RIGHT)

master.after(1000, display_image)
mainloop()