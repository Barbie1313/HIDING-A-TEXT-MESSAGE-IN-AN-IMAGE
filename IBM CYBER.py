from tkinter import *
from PIL import Image, ImageTk
from tkinter import filedialog
from stegano import lsb

filename = None

def show_image():
    global filename
    filename = filedialog.askopenfilename(filetypes=[("Image Files", "*.png;*.jpg;*.jpeg")])
    try:
        img = Image.open(filename).resize((300, 300), Image.LANCZOS)
        photo = ImageTk.PhotoImage(img)
        lbl.config(image=photo, text="")
        lbl.image = photo
    except Exception as e:
        print(f"Error: {e}")

def hide_data():
    global filename
    if filename:
        message = text1.get(1.0, END)
        secret = lsb.hide(filename, message)
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])
        if save_path:
            secret.save(save_path)
            print("Data hidden and saved successfully.")
        else:
            print("Save canceled.")
    else:
        print("Please select an image first.")

def show_data():
    global filename
    if filename:
        clear_message = lsb.reveal(filename)
        text1.delete(1.0, END)
        text1.insert(END, clear_message)
    else:
        print("Please select an image first.")

def save_image():
    global filename
    if filename:
        save_path = filedialog.asksaveasfilename(defaultextension=".png", filetypes=[("Image Files", "*.png")])
        if save_path:
            Image.open(filename).save(save_path)
            print("Image saved successfully.")
        else:
            print("Save canceled.")
    else:
        print("Please select an image first.")

root = Tk()
root.title("Steganography - Hiding a Secret Text Message in an Image")
root.geometry("700x500+150+180")
root.resizable(False, False)
root.configure(bg="#2f4155")

Label(root, text="CYBER SECURITY", bg="#2f4155", fg="white", font="arial 25 bold").place(x=100, y=20)

try:
    app_icon_img = Image.open(r'C:\Users\Adithi\OneDrive\Desktop\IBM CYBER\kitty.jpg').resize((32, 32), Image.LANCZOS)
    app_icon = ImageTk.PhotoImage(app_icon_img)
    root.iconphoto(False, app_icon)
except FileNotFoundError:
    print("Application icon image file not found.")

try:
    other_img = Image.open(r"C:\Users\Adithi\Desktop\cat.jpg").resize((300, 300), Image.LANCZOS)
    other_photo = ImageTk.PhotoImage(other_img)
    Label(root, image=other_photo, bg="#2f4155").place(x=50, y=70)
except FileNotFoundError:
    print("Other image file not found.")

f = Frame(root, bd=3, bg="black", width=340, height=280, relief=GROOVE)
f.place(x=10, y=80)

lbl = Label(f, bg="black")
lbl.place(x=40, y=10)

frame2 = Frame(root, bd=3, width=340, height=280, bg="white", relief=GROOVE)
frame2.place(x=350, y=80)

text1 = Text(frame2, font="Roboto 20", bg="white", fg="black", relief=GROOVE, wrap=WORD)
text1.place(x=0, y=0, width=320, height=295)

scrollbar = Scrollbar(frame2, command=text1.yview)
scrollbar.place(x=320, y=0, height=295)
text1.configure(yscrollcommand=scrollbar.set)

frame3 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame3.place(x=10, y=370)

Button(frame3, text="Open Image", width=10, height=2, font="arial 14 bold", command=show_image).place(x=20, y=30)
Button(frame3, text="Save Image", width=10, height=2, font="arial 14 bold", command=save_image).place(x=180, y=30)
Label(frame3, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

frame4 = Frame(root, bd=3, bg="#2f4155", width=330, height=100, relief=GROOVE)
frame4.place(x=360, y=370)

Button(frame4, text="Hide Data", width=10, height=2, font="arial 14 bold", command=hide_data).place(x=20, y=30)
Button(frame4, text="Show Data", width=10, height=2, font="arial 14 bold", command=show_data).place(x=180, y=30)
Label(frame4, text="Picture, Image, Photo File", bg="#2f4155", fg="yellow").place(x=20, y=5)

root.mainloop()
