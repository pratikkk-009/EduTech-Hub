from tkinter import *
from tkinter import messagebox
import pymysql
from pymysql import MySQLError

background="#FFF7D1"
framebg="#FFF0DC"
farmefg="#FFF7D1"

global Try_no
Try_no=0

def trial():
    global Try_no

    Try_no +=1
    print("Attempt Number: ",Try_no)
    if Try_no==3:
        messagebox.showwarning("WARNING","You have tried more than a limit")
        root.destroy()
        #program closed


def loginuser():
    username = user.get()
    password = code.get()

    if (username == "" or username == "User_Name") or (password == "" or password == "Password"):
        messagebox.showerror("Entry Error", "Type username or password!!")
    else:
        try:
            # Using PyMySQL to connect to the database
            mydb = pymysql.connect(host='localhost', user='root', password='Tanu@0203', database="balaji")
            mycursor = mydb.cursor()
            print("Connected to Database!!")
        except pymysql.MySQLError as err:
            # Catching specific MySQL error
            messagebox.showerror("Connection", f"Database is not connected: {err}")
        except Exception as e:
            # Handling other unexpected errors
            messagebox.showerror("Error", f"An unexpected error occurred: {e}")
       

   
        command="use balaji"
        mycursor.execute(command)

        command="select * from login where username=%s and Password=%s"
        mycursor.execute(command,(username,password))
        myresult =mycursor.fetchone()
        print(myresult)

        if myresult==None:
             messagebox.showinfo("Invalid","Invalid Username And Password!!")

             #but user can try many ties and crack password, so make user try only 3 times

             trial()

        else:
            messagebox.showinfo("Login","Login Successful!!!")

            root.destroy()

            import Main

def register():
    root.destroy()
    import Register
            

root=Tk()
root.title("Login Form")
root.geometry("1050x700+210+100")
root.config(bg=background)
root.resizable(False, False)

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


#icon image
image_icon=PhotoImage(file="Reg_img/icon1.png")
root.iconphoto(False,image_icon)


#Background iamge
frame=Frame(root,bg="red")
frame.pack(fill=Y)


backgroundimage=PhotoImage(file="Reg_img/login.png")
Label(frame,image=backgroundimage).pack()


##User entry

def user_enter(e):
    user.delete(0,'end')

def user_leave(e):
    name=user.get()
    if name=='':
        user.insert(0,'User_Name')
        
user=Entry(frame,width=12,fg="#0B192C",border=1,bg="#FFFFFF",font=('Arial Bold',17))
user.insert(0,'User_Name')
user.bind("<FocusIn>", user_enter)
user.bind("<FocusOut>", user_leave)
user.place(x=530,y=283)


##Password entry

def password_enter(e):
    code.delete(0,'end')

def password_leave(e):
    if code.get()=='':
        code.insert(0,'Password')
        
code=Entry(frame,width=12,fg="#0B192C",border=1,bg="#FFFFFF",font=('Arial Bold',17),show="*")
code.insert(0,'Password')
code.bind("<FocusIn>", password_enter)
code.bind("<FocusOut>", password_leave)
code.place(x=530,y=348)

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
eyeButton.place(x=698,y=358)

#####Login Button


loginButton=Button(root,text="LOGIN",bg="#0B192C",fg="white",width=14,height=1,font=("arial",16,'bold'),bd=0,command=loginuser)
loginButton.place(x=533,y=413)
label=Label(root,text="Don't have an Account?",fg="black",bg="white",font=("Microsoft VaHei UI Light",12))
label.place(x=340,y=465)

registerButton=Button(root,width=15,text="ADD NEW USER",border=0,bg="#FFC145",cursor='hand2',fg="black",font=("arial",12),command=register)
registerButton.place(x=555,y=460)



root.mainloop()
