from tkinter import*
import random
window.Tk()

window.title("Picnic Bag List")
window.geometry("500x500")

List1 = ["pen , pencil , chocolate , biscuits , chips , tiffin  , clothes , phone , id card , bottle "]

label1 = Label(window)

label2 = Label(window)
label1["text"] = "LISTED ITEMS :" + str(List1)
label1.place(relx = 0.5 , rely = 0.5, anchor = CENTER)


def randomList():
  random_list = random.sample(range(1 , 10),1 )
    label2['text']= "Put item no. "+ str(random_list)+"in bag"
    



btn = Button(window , text = " Which item to put in bag" , command = randomList())
btn.place(relx = 0.5 , rely = 0.4 , anchor = CENTER)

label2.place(relx = 0.5 , rely = 0.6 , anchor = CENTER)





window.mainloop()