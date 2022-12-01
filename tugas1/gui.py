from tkinter import * 
from PIL import ImageTk, Image
from tkinter import filedialog

root = Tk()
root.title('Computer Vision')
root.geometry("1500x1500")

def show():
    myLabel = Label(root, text=clicked.get()).pack()

clicked = StringVar()
options = [
    "Negasi",
    "Rotate",
    "Pencerminan"
]

drop = OptionMenu(root, clicked, *options)
drop.pack()
   
myButton = Button(root, text="Show Selection", command=show).pack()
# def open():
    # global my_image
    # root.filename = filedialog.askopenfilename(initialdir="/media/ikantongkol/575E5BC04E0C3C04/Kuliah/Tugas/Tugas/SEMESTER 7/Visi Komputer/visi-komputer/tugas1/", title="Select A File")
    # my_label = Label(root, text=root.filename).pack()
    # my_image = ImageTk.PhotoImage(Image.open(root.filename))
    # my_image_label = Label(Image=my_image).pack()
    # 
# my_btn = Button(root, text="Open File", command=open).pack()

root.mainloop()