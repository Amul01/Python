from tkinter import *
from functools import partial
import pymysql

conn=pymysql.connect(host='localhost', user='root', password='', db='gst')
cur=conn.cursor()


#--------------------------------------------------------------------------ENTRY
def submit(name,gstin,ent):
    global cur
    query='insert into gstcontact (Name, GSTIN) values (%s,%s)'
    cur.execute(query,(name,gstin))
    cur.execute('SELECT Name FROM gstcontact ORDER BY ID DESC LIMIT 1')
    #print(cur.fetchall()[0][0])
    if(cur.fetchall()[0][0]==name):
        Label(ent, text='Entry Successful').grid(row=3)
    conn.commit()
def entry(self):
    ent=Tk()
    ent.title("New Entry!")
    ent.focus_set()
    #global e1,e2
    Label(ent, text='Name', width=15).grid(row=0) 
    Label(ent, text='GST No.', width=15).grid(row=1) 
    e1 = Entry(ent)
    e2 = Entry(ent)
    e2.bind('<Return>', lambda event: submit(e1.get(),e2.get(),ent))
    e1.grid(row=0, column=1)
    #e1.focus_set()
    e2.grid(row=1, column=1)

    #ent.bind("<FocusIn>", lambda event: handle_focus(e1,ent))
    ent.after(1, lambda: e1.focus_force())

    b1 = Button(ent, text='Submit', width=10, command=lambda:submit(e1.get(),e2.get(),ent))
    b2 = Button(ent, text='Done', width=10, command=ent.destroy)
    b1.grid(row=2, column=1)
    b2.grid(row=2, column=2)



#--------------------------------------------------------------------------SEARCH
def srch(name,ent):
    global cur
    query='select * from `gstcontact` where Name=%s'
    row_count=cur.execute(query,name)
    row=cur.fetchall()
    #print(row)
    if(row_count==0):
        #print('no record')
        Label(ent, text='Record not found').grid(row=3)
    c=4
    for index,data in enumerate(row):
        Label(ent, text=data[1]).grid(row=c,column=0)
        #Label(ent, text=data[2], state='disabled').grid(row=c,column=1)
        t=Text(ent, height=1, borderwidth=0.5, width=20)
        t.tag_configure("center", justify='center')
        t.insert(END,data[2])
        t.tag_add("center", "1.0", "end")
        t.grid(row=c,column=1)
        t.configure(state='disabled')
        t.see(END)
        #Entry(ent,text=data[2],fg="black",bg="white",state='readonly').grid(row=c,column=1)
        c=c+1
        
def search(self):
    ent=Tk()
    ent.title("Search by Name!")
    
    global e1
    Label(ent, text='Enter the name to be searched - ').grid(row=0)
    e1=Entry(ent)
    e1.bind('<Return>', (lambda event: srch(e1.get(),ent)))
    e1.grid(row=0, column=1)

    ent.after(1, lambda: e1.focus_force())
    
    b1=Button(ent, text='Search', width=10, command=(lambda:srch(e1.get(),ent)))
    b1.grid(row=1,column=1)
    b1=Button(ent, text='Done', width=10, command=ent.destroy)
    b1.grid(row=1,column=2)
    
    Label(ent, text=' ').grid(row=2)
    Label(ent, text=' ').grid(row=3)



#-------------------------------------------------------------------------------MODIFY
def check(name,ent):
    global cur
    row_count=cur.execute('select * from gstcontact where Name=%s',name)
    if(row_count==0): Label(ent, text='Record not found').grid(row=2)
    else:
        Label(ent, text='New Name').grid(row=1,column=0)
        Label(ent, text='New GST No.').grid(row=2,column=0)
        e2=Entry(ent)
        e2.grid(row=1,column=1)
        e2.bind('<Return>', (lambda event: modname(name,e2.get(),ent)))
        e3=Entry(ent)
        e3.grid(row=2,column=1)
        e3.bind('<Return>', (lambda event: modgstin(name,e3.get(),ent)))
        b2=Button(ent, text='Modify', command=lambda:modname(name,e2.get(),ent))
        b2.grid(row=1,column=2)
        b3=Button(ent, text='Modify', command=lambda:modgstin(name,e3.get(),ent))
        b3.grid(row=2,column=2)
def modname(name,newname,ent):
    global cur
    query='update `gstcontact` set `Name`=%s where `Name`=%s'
    cur.execute(query,(newname,name))
    srch(newname,ent)
def modgstin(name,gst,ent):
    global cur
    query='update `gstcontact` set `GSTIN`=%s where `Name`=%s'
    cur.execute(query,(gst,name))
    srch(name,ent)
def modify(self):
    ent=Tk()
    ent.title("Modify Record!")

    #global e1,e2,e3
    Label(ent, text='Enter the name whose record is to be modified - ').grid(row=0,column=0)
    e1=Entry(ent)
    e1.grid(row=0,column=1)
    e1.bind('<Return>', (lambda event: check(e1.get(),ent)))
    ent.after(1, lambda: e1.focus_force())
    
    b1=Button(ent, text='Enter', command=lambda:check(e1.get(),ent))
    b1.grid(row=2,column=1)
    
    #call=partial(modname,e1.get(),e2.get(),ent)


    
#------------------------------------------------------------------------------DELETE
def delete(name,ent):
    global cur
    row_count=cur.execute('select * from gstcontact where Name=%s',name)
    #row1=cur.fetchone()
    if(row_count==0): Label(ent, text='Record not found').grid(row=2)
    else:
        query='delete from gstcontact where Name=%s'
        cur.execute(query,name)
        Label(ent, text='Record Deleted!').grid(row=2)
def remove(self):
    ent=Tk()
    ent.title('Delete record!')
    ent.after(1, lambda: e1.focus_force())
    
    Label(ent, text='Enter the name whose record is to be deleted - ').grid(row=0,column=0)
    e1=Entry(ent)
    e1.bind('<Return>', (lambda event:delete(e1.get(),ent)))
    e1.grid(row=0,column=1)
    Button(ent, text='Delete', command=lambda:delete(e1.get(),ent)).grid(row=1,column=1)
    Button(ent, text='Done', command=ent.destroy).grid(row=1,column=2)
    

#----------------------------------------------------DISPLAY ALL
def displayall(self):
    ent=Tk()
    ent.title('All Records!')
    row_count=cur.execute('select * from gstcontact')
    row=cur.fetchall()
    
    if(row_count==0):
        #print('no record')
        Label(ent, text='Record not found').grid(row=3)
    for index,data in enumerate(row):
        #Label(ent, text=data[0]).grid(row=index+1,column=0)
        Label(ent, text=data[1]).grid(row=index+1,column=1)
        #Label(ent, text=data[2], state='disabled').grid(row=c,column=1)
        t=Text(ent, height=1, borderwidth=0.5, width=20)
        t.tag_configure("center", justify='center')
        t.insert(END,data[2])
        t.tag_add("center", "1.0", "end")
        t.grid(row=index+1,column=2)
        t.configure(state='disabled')
        t.see(END)
        #Entry(ent,text=data[2],fg="black",bg="white",state='readonly').grid(row=c,column=1)
        #c=c+1
    


if __name__ == "__main__":
    conn=pymysql.connect(host='localhost', user='root', password='', db='gst')
    cur=conn.cursor()

    m = Tk()
    m.title("Transport GST")
    l1=Label(m, text="Welcome!", fg="red")
    l1.pack()
    l2=Label(m, text=" ", width=30)
    l2.pack()

    m.bind('n',entry)
    b1=Button(m, text="New Entry", width=30, command=entry)
    b1.pack()

    m.bind('s',search)
    b2=Button(m, text="Search by name", width=30, command=search)
    b2.pack()

    m.bind('m',modify)
    b3=Button(m, text="Modify", width=30, command=modify)
    b3.pack()

    m.bind('r',remove)
    b4=Button(m, text="Remove", width=30, command=remove)
    b4.pack()

    m.bind('d',displayall)
    b5=Button(m, text="Display all records", width=30, command=displayall)
    b5.pack()

    b6=Button(m, text='Close', width=30, command=m.destroy())
    b6.pack()

    m.mainloop()
