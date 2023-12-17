from tkinter import *
from tkinter import messagebox
from random import choice, randint, shuffle
import pyperclip
import json
def generate_password():
    letters = ['a', 'b', 'c', 'd', 'e', 'f', 'g', 'h', 'i', 'j', 'k', 'l', 'm', 'n', 'o', 'p', 'q', 'r', 's', 't', 'u', 'v', 'w', 'x', 'y', 'z', 'A', 'B', 'C', 'D', 'E', 'F', 'G', 'H', 'I', 'J', 'K', 'L', 'M', 'N', 'O', 'P', 'Q', 'R', 'S', 'T', 'U', 'V', 'W', 'X', 'Y', 'Z']
    numbers = ['0', '1', '2', '3', '4', '5', '6', '7', '8', '9']
    symbols = ['!', '#', '$', '%', '&', '(', ')', '*', '+']

    password_letters = [choice(letters) for _ in range(randint(8, 10))]
    password_symbols = [choice(symbols) for _ in range(randint(2, 4))]
    password_numbers = [choice(numbers) for _ in range(randint(2, 4))]

    password_list = password_letters + password_symbols + password_numbers
    shuffle(password_list)

    password = "".join(password_list)
    password_entry.insert(0, password)
    pyperclip.copy(password)


def save():
    website=website_entry.get()
    email=email_entry.get()
    password=password_entry.get()
    new_data={website:{"email":email,
                       "password":password}}
    if len(website)==0 or len(password)==0:
        messagebox.showinfo(title="oops",message="please dont leave the field empty")
    else:
        # is_ok=messagebox.askokcancel(title=website,message=f"these are the detail entered:\n email :{email}\n password :{password}\n do you wanna add this?")
        # if is_ok:
        try:
            with open("data.json","r") as data_file:
                # json.dump(new_data,data_file,indent=4)
                datas=json.load(data_file)
        except FileNotFoundError:
            with open("data.json","w") as data_file:
                json.dump(new_data,data_file,intend=4)
        else:
             datas.update(new_data)


             with open("data.json","w") as data_file:
                json.dump(datas,data_file,indent=4)


            # or data_file=open("data.txt","a")
        finally: # data_file.write(f"{website} | {email} | {password}\n")
                website_entry.delete(0,END)
                email_entry.delete(0,END)
                password_entry.delete(0,END)
def find_password():
    website=website_entry.get()
    with open("data.json","r") as data_file:
        data=json.load(data_file)
        # data gets the dictionary of data
    if website in data:
        email=data[website]["email"]
        password=data[website]["password"]
        messagebox.showinfo(title="record",message=f"email:{email}\n password:{password}\n")

window=Tk()
window.title("password manager")
window.config(padx=50,pady=50)
canvas=Canvas(height=200,width=200)#the picture reside in canvas
logo_img=PhotoImage(file="logo.png")#creating image
canvas.create_image(100,100,image=logo_img)

# canvas.pack()
# if grid used the no need to pack
canvas.grid(row=0,column=1,columnspan=2)
website_label=Label(text="website:")
website_label.grid(row=1,column=0)
email_label=Label(text="email:")
email_label.grid(row=2,column=0)
password_label=Label(text="password:")
password_label.grid(row=3,column=0)
website_entry=Entry(width=21)
website_entry.grid(row=1,column=1)
website_entry.focus()
search_button=Button(text="Search",width=13,command=find_password)
search_button.grid(row=1,column=2)
email_entry=Entry(width=40)
email_entry.grid(row=2,column=1,columnspan=2)
email_entry.insert(0,"anujth345@gmail.com")
password_entry=Entry(width=21)
password_entry.grid(row=3,column=1)
generate_password_button=Button(text="generate password",command=generate_password)
generate_password_button.grid(row=3,column=2)
add_button=Button(text="add",width=34,command=save)
add_button.grid(row=4,column=1,columnspan=2)
window.mainloop()
# while using columnspan overall columnsize get minimized but the button gets spanened in both column so
# that we can see generate password button and email entry coming closer because column size get squuzed