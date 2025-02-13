from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import MySQLError


background="#FFF7D1"
framebg="#FFF0DC"
farmefg="#FFF7D1"

root=Tk()
root.title("New User Registration")
root.geometry("1050x700+210+100")
root.config(bg=background)
root.resizable(False,False)
# Set window size (resolution: 1200x600)
window_width = 1050
window_height = 700
screen_width = root.winfo_screenwidth()
screen_height = root.winfo_screenheight()

# Calculate center position
position_top = int(screen_height / 2 - window_height / 2)
position_left = int(screen_width / 2 - window_width / 2)

# Set the window geometry with center position
root.geometry(f"{window_width}x{window_height}+{position_left}+{position_top}")

def register():
    username=user.get()
    password=code.get()
    admincode=adminaccess.get()

    print(admincode,username,password)

    if admincode=="1234":

        if (username=="") or (password=="" or password==""):
            messagebox.showerror("Entry Error!!","Type username or password !!")


        else:
            try:
                # Using PyMySQL to connect to the database
                mydb = pymysql.connect(host='localhost', user='root', password='Tanu@0203')
                mycursor = mydb.cursor()
                print("Connected to Database!!")



            except:
                message.showerror("Connection","Database connection not Established!!")


            try:
                command="create database balaji"
                mycursor.execute(command)

                command="use balaji"
                mycursor.execute(command)

                command="create table login (user int auto_increment key not null, username varchar(30),Password varchar(100))"
                mycursor.execute(command)


            except:
                mycursor.execute("use balaji")
                mydb = pymysql.connect(host='localhost', user='root', password='Tanu@0203',database="balaji")
                mycursor = mydb.cursor()


                command="insert into login(username,Password) values(%s,%s)"

                mycursor.execute(command,(username,password))
                mydb.commit()
                mydb.close()
                messagebox.showinfo("Registeration","New User Added Successfully!!!")



    else:
        messagebox.showerror("Admin Access","Please enter valid Admin Password!!")
                





def login():
    root.destroy()      #To Close Registration Window
    import Login


#icon image
image_icon=PhotoImage(file="Reg_img/icon1.png")
root.iconphoto(False,image_icon)


#Background image
frame=Frame(root,bg="red")
frame.pack(fill=Y)


backgroundimage=PhotoImage(file="Reg_img/Reg2.png")
Label(frame,image=backgroundimage).pack()


##Labels for admin pass, username pass.
Label(root,text="Please verify Admin's permission",width=27,height=1,bg="#F2F9FF",fg='#2A3335',font='arial 12 bold').place(x=390,y=274)
Label(root,text="with entering its Password below !!",width=27,height=1,bg="#F2F9FF",fg='#2A3335',font='arial 12 bold').place(x=390,y=298)


Label(root,text="Username:",width=9,height=1,bg="#FADA7A",fg='#000',font='arial 13 bold').place(x=357,y=367)
Label(root,text="Password:",width=9,height=1,bg="#FADA7A",fg='#000',font='arial 13 bold').place(x=357,y=405)


adminaccess=Entry(frame,width=24,fg="#000",border=2,bg="#ffffff",font=("Arial Bold",18),show="*",justify="center")
adminaccess.focus()
adminaccess.place(x=370,y=325)



##User Entry

user=Entry(frame,width=16,fg="#000000",bg="#ffffff",border=2,font='arial 14 bold',justify="center")
user.place(x=460,y=364)


##Password entry

code=Entry(frame,width=16,fg="#000000",bg="#ffffff",border=2,font='arial 14 bold',justify="center",show="*")
code.place(x=460,y=403)



##Hide and show button
button_mode=False

def hide():
    global button_mode

    if button_mode:
        eyeButton.config(image=closeeye,activebackground="white")
        code.config(show="*")
        button_mode=False
              
    else:
        eyeButton.config(image=openeye,activebackground="white")
        code.config(show="")
        button_mode=True
        
openeye=PhotoImage(file="Reg_img/openeye.png")
closeeye=PhotoImage(file="Reg_img/closeeye.png")
eyeButton=Button(frame,image=openeye,bg="#375174",bd=0,command=hide)
eyeButton.place(x=650,y=409)


## Regester Button

reg_button=Button(root,text="Add New User",bg="#FADA7A",fg="black",width=12,height=1,font='arial 12 bold',bd=0,command=register)
reg_button.place(x=465,y=457)


back_button_img=PhotoImage(file="Reg_img/Back.png")
BackButon=Button(root,image=back_button_img,bd=0,width=30,height=30,fg="#deeefb",command=login)
BackButon.place(x=15,y=10)

root.mainloop()
