from tkinter import *
import pyqrcode
from PIL import ImageTk,Image

root=Tk()
root.title("QR code generator for url")
def generate():
    imagename=image_entry.get()
    updatedimagename=imagename+".png"
    url=link_entry.get()
    QRdata=pyqrcode.create(url)
    QRdata.png(updatedimagename,scale=3)
    image=ImageTk.PhotoImage(Image.open(updatedimagename))
    image_label=Label(image=image)
    image_label.image=image
    canvas.create_window(250,280,window=image_label)

canvas=Canvas(root,width=500,height=500,bg="green")
canvas.pack()


image_label=Label(root,text="Enter the image name",font="Arial",fg="black",bg="yellow")
canvas.create_window(250,50,window=image_label)

image_entry=Entry(root)
canvas.create_window(250,80,window=image_entry)

link_label=Label(root,text="Enter website link",font="Arial",fg="black",bg="yellow")
canvas.create_window(250,160,window=link_label)

link_entry=Entry(root)
canvas.create_window(250,190,window=link_entry)

generate_button=Button(root,text="Generate QR code",font="Arial",fg="green",bg="pink",command=generate)
canvas.create_window(250,400,window=generate_button)

final_label=Label(text="Image")
canvas.create_window(250,370,window=final_label)


root.mainloop()

