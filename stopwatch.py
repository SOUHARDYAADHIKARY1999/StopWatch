import tkinter as Tkinter
counter =-1
runnning=False
def counter_label(label):
    def count():
        if running:
            global counter
            if counter==-1:
                display="STARTING..."
            else:
                display=str(counter)
            label['text']=display
            label.after(1000,count)
            counter+=1
    count()
def Start(label):
    global running
    running=True
    counter_label(label)
    start['state']='disabled'
    stop['state']='normal'
    reset['state']='normal'
def Stop():
    global running
    start['state']='normal'
    stop['state']='disabled'
    reset['state']='normal'
    running=False
def Reset(lable):
    global counter
    counter=-1
    if running==False:
        reset['state']='disabled'
        label['text']="WELCOME!"
    else:
        label['text']='STARTING...'

root=Tkinter.Tk()
root.title("STOPWATCH")

root.minsize(width=250,height=70)
label=Tkinter.Label(root,text="WELCOME!",fg="black",font="Verdana 30 bold")
label.pack()
start=Tkinter.Button(root,text='START',width=15,command=lambda:Start(label))
start.pack()
stop=Tkinter.Button(root,text="STOP",width=15,state="disabled",command=Stop)
stop.pack()
reset=Tkinter.Button(root,text="RESET",width=15,state="disabled",command=lambda:Reset(label))
reset.pack()

root.mainloop()

