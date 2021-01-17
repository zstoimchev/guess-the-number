import tkinter as tk
import random

randombroj=random.randint(0, 10)

def check():
   result=int(glvnes.get())            #the value of entry  widget
   if result==randombroj:
      gldugme.grid_forget()            #hide check button widget
      glvnes.grid_forget()             #hide entry widget

      bravo=tk.Label(root, text="Congratulations! You guessed the number  ;)", font=("arial italic", 15), bg="yellow")      #congratulations widget
      bravo.config(width=33, heigh=1)
      bravo.grid(pady=0, row=1)

      def restart():       #restart function located in check function
         global randombroj
         glvnes.delete(0, "end")
         randombroj=random.randint(0, 10)      #get new random number
         bravo.destroy()                       #destroy congratulations widget
         weset.destroy()                       #destroy restart button
         gldugme.grid(pady=20, row=2)          #display again  check button
         glvnes.grid(pady=0, row=1)            #display again entry widget

      weset=tk.Button(root, text="Restart", font=("arial italic", 18), bg='#6BDF63', command=restart)                 #the restart button
      weset.config(width=13, heigh=2)
      weset.grid(pady=8, row=2)

root=tk.Tk()
root.title("Guess The  Secret Number")
root.geometry('450x250')
root.config(bg="#F2E06B")

glmeni=tk.Label(root, text="Can  you gess the secret number?", bg='#8CCEC0', font=("arial italic", 19))        #main  widget
glmeni.config(heigh=2)
glmeni.grid(pady=30, padx=28, row=0)

glvnes=tk.Entry(root, text="Enter number here:")       #entry box
glvnes.config(width=40)
glvnes.grid(pady=0, row=1)

gldugme=tk.Button(root, text="Check", font=("arial italic", 18), 
bg='#6BDF63', command=check)            #check button
gldugme.config(width=13, heigh=2)
gldugme.grid(pady=20, row=2)

root.mainloop()
