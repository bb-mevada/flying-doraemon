from tkinter import *

root = Tk()
root.title('Moving Doraemon')
root.geometry('600x400+400+200')
root.configure(bg='black')
root.resizable(False,False)

# Creating Canvas
my_canvas = Canvas(root,width=600,height=400,bg='black')
my_canvas.pack()

# Creating Images
img = PhotoImage(file='./doraemon.png')
my_img = my_canvas.create_image(300,200,image=img)

def move(e):
    global img
    img = PhotoImage(file='./doraemon.png')
    my_img = my_canvas.create_image(e.x,e.y,image=img)

my_canvas.bind('<B1-Motion>',move)

root.mainloop()