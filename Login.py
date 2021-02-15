from tkinter import *
from tkinter import messagebox
import sys

#login method
def login_method():

    #destroy main menu screen
    mainmenu.destroy()

    #check if login button is clicked
    def button_click():

        #declarations
        global name_file
        loop = True
        username = username_login.get("1.0", "end-1c")
        password = password_login.get("1.0", "end-1c")

        #open file as read
        with open('Database.txt','r') as file:
            
            #loop through file
            while loop:
                line = file.readline()

                #check if there is text in the line
                if not line:
                    messagebox.showinfo('Error', 'Wrong username or password!')
                    loop = False

                #check if username and password are correct, if yes go to app()
                else:
                    name_file, username_file, password_file = line.split(" ")
                    if username == username_file and password == password_file.strip():
                        login.destroy()
                        app()

    #declaration
    global login

    #Canvas
    login = Tk()
    login.title('login')
    login.geometry('400x200+400+100')

    #Labels
    username_label = Label(login, text = 'Username:',font = 20)
    Password_label = Label(login, text = 'Password:',font = 20)
    username_label.grid(column = 0, row = 0)
    Password_label.grid(column = 0, row = 1)

    #buttons and textboxes
    username_login = Text(login, width = 15, height = 1)
    password_login = Text(login, width = 15, height = 1)
    btnLogin = Button(login, height = 1, width = 10, text="Login", command = button_click)
    back = Button(login, height = 1, width = 10, text="back", command = back_login)

    #position on grid
    username_login.grid(column = 1, row = 0)
    password_login.grid(column = 1, row = 1)
    btnLogin.grid(column = 0, row = 2)
    back.grid(column= 0, row = 5)

    login.mainloop()


#sign up method
def signup_method():

    #destroy main menu screen
    mainmenu.destroy()
    
    #check if signup button is clicked
    def button_click():

        #decleratinos
        name = name_signup.get("1.0", "end-1c")
        username = username_signup.get("1.0", "end-1c")
        password = password_signup.get("1.0", "end-1c")

        #save info to file
        with open('Database.txt', 'a') as file:
            file.write(f"{name} {username} {password}\n")
        signup.destroy()
        main()

    #declare
    global signup

    #canvas
    signup = Tk()
    signup.title('Main Menu')
    signup.geometry('400x200+400+100')

    #Labels
    name_label = Label(signup, text = 'Name:', font = 20)
    username_label = Label(signup, text = 'Username:',font = 20)
    Password_label = Label(signup, text = 'Password:',font = 20)
 
    
    #create texboxes and button
    name_signup = Text(signup, width = 15, height = 1)
    username_signup = Text(signup, width = 15, height = 1)
    password_signup = Text(signup, width = 15, height = 1)
    btnsignup = Button(signup, height = 1, width = 10, text="Signup", command = button_click)
    back = Button(signup, height = 1, width = 10, text="back", command = back_signup)

    #positions on canvas
    name_label.grid(column = 0, row = 1)
    username_label.grid(column = 0, row = 2)
    Password_label.grid(column = 0, row = 3)
    name_signup.grid(column = 1, row = 1)
    username_signup.grid(column = 1, row = 2)
    password_signup.grid(column = 1, row = 3)
    btnsignup.grid(column = 0, row = 4)   
    back.grid(column= 0, row = 5)

    signup.mainloop()

#post login screen
def app():

    #canvas
    home = Tk()
    home.title('Hello!')
    home.geometry('400x200+400+100')

    #label
    label = Label(home, text = f"Welcome {name_file}")

    #button
    button = Button(home, height = 1, width = 10, text="Exit", command = close)

    #positions on grid
    label.grid(column = 0, row = 1)
    button.grid(column = 0, row = 2)

    home.mainloop()

#close program
def close():
    exit()

#close signup window and go to main menu
def back_signup():
    signup.destroy()
    main()

#close login window and go to main menu
def back_login():
    login.destroy()
    main()

def main():
    global mainmenu

    #create canvas
    mainmenu = Tk()
    mainmenu.title('Main Menu')
    mainmenu.geometry('400x200+400+100')
    
    #buttons
    btnLogin = Button(mainmenu, height = 1, width = 10, text="Login", command = login_method)
    btnsignup = Button(mainmenu, height = 1, width = 10, text="Sign up", command = signup_method)
    
    #positions on grid
    btnLogin.grid(column = 0, row = 0)
    btnsignup.grid(column = 0, row = 1)

    mainmenu.mainloop()

main()
