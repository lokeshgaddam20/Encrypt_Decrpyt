import tkinter
from tkinter import *
import customtkinter
import base64
from tkinter import messagebox
from PIL import ImageTk, Image


# Encoding Function
def encode(key, msg):
    enc = []
    for i in range(len(msg)):
        list_key = key[i % len(key)]
        list_enc = chr((ord(msg[i]) +
                        ord(list_key)) % 256)
        enc.append(list_enc)
    return base64.urlsafe_b64encode("".join(enc).encode()).decode()


# Decoding Function
def decode(key, code):
    dec = []
    enc = base64.urlsafe_b64decode(code).decode()
    for i in range(len(enc)):
        list_key = key[i % len(key)]
        list_dec = chr((256 + ord(enc[i]) - ord(list_key)) % 256)

        dec.append(list_dec)
    return "".join(dec)


# Function that executes on clicking Show Message function
def result():
    msg = Message.get()
    k = key.get()
    i = mode.get()
    if (i == 1):
        Output.set(encode(k, msg))
    elif (i == 2):
        Output.set(decode(k, msg))
    else:
        messagebox.showinfo('ProjectGurukul', 'Please Choose one of Encryption or Decrption. Try again.')


# Function that executes on clicking Reset function
def reset():
    Message.set("")
    key.set("")
    mode.set(0)
    Output.set("")


customtkinter.set_appearance_mode("System")  # Modes: system (default), light, dark
customtkinter.set_default_color_theme("dark-blue")  # Themes: blue (default), dark-blue, green

root = customtkinter.CTk()
root.geometry("800x580")
root.title("Encrypt and Decrypt your Messages")

Message = StringVar()
key = StringVar()
mode = IntVar()
Output = StringVar()

img1 = ImageTk.PhotoImage(Image.open("pattern.png"))
l1 = customtkinter.CTkLabel(master=root, image=img1)
l1.pack()

# creating custom frame
frame_bottom = customtkinter.CTkFrame(master=l1, width=420, height=480, corner_radius=15)
frame_bottom.place(relx=0.5, rely=0.5, anchor=tkinter.CENTER)

l2 = customtkinter.CTkLabel(master=frame_bottom, text="Welcome to \nEncryption and Decryption",
                            font=('Century Gothic', 20))
l2.place(x=75, y=35)
label2 = customtkinter.CTkLabel(master=frame_bottom, text="Enter the Message ", font=("'Century Gothic", 13))
label2.place(x=50, y=100)
entry1 = customtkinter.CTkEntry(master=frame_bottom, width=340, textvariable=Message,
                                placeholder_text='Enter the Message')
entry1.place(x=50, y=130)
label2 = customtkinter.CTkLabel(master=frame_bottom, text="Enter the key ", font=("Century Gothic", 13))
label2.place(x=50, y=165)
entry2 = customtkinter.CTkEntry(master=frame_bottom, width=340, textvariable=key, placeholder_text='Enter the Key',
                                show="*")
entry2.place(x=50, y=195)

radiobutton_1 = customtkinter.CTkRadioButton(master=frame_bottom, text="Encrypt", variable=mode, value=1, hover=True,
                                             hover_color="white")
radiobutton_1.place(x=50, y=250)
radiobutton_2 = customtkinter.CTkRadioButton(master=frame_bottom, text="Decrypt", variable=mode, value=2, hover=True,
                                             hover_color="white")
radiobutton_2.place(x=250, y=250)

button1 = customtkinter.CTkButton(master=frame_bottom, width=340, height=40, text="Result", command=result,
                                  corner_radius=25, font=("Century Gothic", 15, "bold"))
button1.place(x=50, y=300)

label3 = customtkinter.CTkLabel(master=frame_bottom, text="Result...", font=(" Axon ", 15))
label3.place(x=50, y=355)
res = customtkinter.CTkEntry(master=frame_bottom, width=340, height=45, textvariable=Output, corner_radius=20, )
res.place(x=50, y=385)

root.mainloop()
