from tkinter import *


# WINDOW - ROOT
window = Tk()
window.title("GasUsage Calculator")
window.minsize(602,400)
window.resizable(width=False,height=False)
# BACKGROUND
background_img = PhotoImage(file="images/background.png")
canvas = Canvas(window, width=602,height=400)
canvas.create_image(0, 0, anchor=NW, image=background_img)
canvas.pack()



# FUNCTION
def result():
    cubic = float(entry_cubic.get())
    result_kwh = cubic * 40 * 1.02264 / 3.6
    label_kwh_result.config(text=f"{result_kwh:.2f}")

    result_eu = 0.0292 * result_kwh
    label_euro_result.config(text=f"{result_eu:.2f}")


def clear():
    entry_cubic.delete(0, END)         
    label_kwh_result.config(text="")
    label_euro_result.config(text="")


# ENTRY - CUBIC METERS
entry_cubic = Entry(bg="white",fg="black",font=("Roboto",20,),width=12, borderwidth=6, relief="sunken")
entry_cubic.focus()
entry_cubic.place(x=38,y=150)
# NAME LABEL- CUBIC METERS
label_cubic = Label(text="m\u00B3",bg="#EFDC1E",fg="black",font=("Roboto",20 ))
label_cubic.place(x=260,y=156)



# RESULT LABEL - kWh 
label_kwh_result = Label(bg="white",fg="black",font=("Helvetica",20,),width=12, borderwidth=8,relief="solid")
label_kwh_result.place(x=310,y=150)
# NAME LABEL - kWh 
label_kwh = Label(text="kWh",bg="#EFDC1E",fg="black",font=("Roboto",20))
label_kwh.place(x=510,y=156)



# RESULT LABEL - EURO/kWh
label_euro_result = Label(bg="white",fg="black",font=("Helvetica",20,),width=12, borderwidth=8, relief="solid")
label_euro_result.place(x=38,y=250)
# NAME LABEL - EURO/kWh 
label_euro_kwh = Label(text="\u20AC/kWh",bg="#EFDC1E",fg="black",font=("Roboto",20))
label_euro_kwh.place(x=240,y=256)



# BUTTON - RESULT
button_result = Button(text="Result",bg="#3CB043",fg="white",font=("Helvetica",16,"bold"),width=11, borderwidth=7,relief="raised", command=result, activebackground="#028A0F",activeforeground="white",cursor="hand2")
button_result.place(x=340,y=247)

# BUTTON - CLEAR
button_clear = Button(text="Clear",bg="#E52B50",fg="white",font=("Helvetica",16,"bold"),width=11, borderwidth=7,relief="raised", command=clear, activebackground="#D10056",activeforeground="white",cursor="hand2")
button_clear.place(x=340,y=300)



window.mainloop()






