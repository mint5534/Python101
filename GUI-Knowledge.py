from tkinter import *
from tkinter import ttk #theme of tk
from tkinter import messagebox


GUI = Tk() # นี่คือหน้าจอหลักของโปรแกรม
GUI.title('โปรแกรมบันทึกข้อมูล') #นี่คือชื่อโปรแกรม
GUI.geometry('500x400') #นี่คือขนาดโปรแกรม



L1 = Label(GUI,text='โปรแกรมบันทึกความรู้',font=('Angsana New',30),fg='green')
L1.place(x=30,y=30)         
####################
def Button2():
    text = 'วันที่ 25-26 ก.พ.'
    messagebox.showinfo('ไปต่างจังหวัด',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=300)
B2 = ttk.Button(FB1,text='ไปต่างจังหวัดวันที่',command=Button2)
B2.pack(ipadx=20,ipady=20)
####################
def Button3():
    text = 'science, Math'
    messagebox.showinfo('วิชาเรียนวันที่ 10-20 ก.พ.',text)

FB1 = Frame(GUI) #คล้ายกระดาน
FB1.place(x=100,y=180)
B3 = ttk.Button(FB1,text='สัปดาห์เรียนวิชาอะไร',command=Button3)
B3.pack(ipadx=20,ipady=20)


GUI.mainloop()
