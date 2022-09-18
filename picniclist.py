from tkinter import*
import random
root=Tk()
root.title("List")
root.geometry("400x400")

random_number_list=Label(root)
random_number_sorted_list=Label(root)
list1=["bottle","tiffin","chocolates","chips","sandwhich","handkerchief","Idcard"]
random_number_list["text"]=str(list1)

def randomlist():
    random_list=random.sample(range(0,7),1)
    random_number_sorted_list["text"]="put item number: " + str(random_list)+" in bag"
    
btn=Button(root,text="which item to put in bag", command=randomlist)
btn.place(relx=0.5, rely=0.4, anchor=CENTER)

random_number_list.place(relx=0.5,rely=0.5,anchor=CENTER)
random_number_sorted_list.place(relx=0.5,rely=0.6,anchor=CENTER)

root.mainloop()