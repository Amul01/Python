from tkinter import *
from functools import partial

import pymysql

conn=pymysql.connect(host='localhost', user='root', password='', db='gst')
cur=conn.cursor()


#--------------------------------------------------------------------------ENTRY
def submit(name,city,gstin,agent,cno,ent):
    global cur
    #print("Value of agent = ", agent)
    query='insert into custgst (Name, `City`, `GSTIN`, `Agent`, `Contact No.`) values (%s,%s,%s,%s,%s)'
    cur.execute(query,(name,city,gstin,agent,cno))
    cur.execute('SELECT Name FROM custgst ORDER BY ID DESC LIMIT 1')
    #print(cur.fetchall()[0][0])
    if(cur.fetchall()[0][0]==name):
        l1=Label(ent, text='Entry Successful.')
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=6)
    #print(name," ",city," ",gstin," ",agent," ",cno)
    conn.commit()
def entry(self):
    ent=Tk()
    ent.title("New Entry!")
    ent.focus_set()
    #global e1,e2
    l1=Label(ent, text='Name', width=15)
    l1.config(font=("Times New Roman", 15))
    l1.grid(row=0) 
    l2=Label(ent, text='City', width=15)
    l2.config(font=("Times New Roman", 15))
    l2.grid(row=1)
    l3=Label(ent, text='GST No.', width=15)
    l3.config(font=("Times New Roman", 15))
    l3.grid(row=2)
    l4=Label(ent, text='Agent', width=15)
    l4.config(font=("Times New Roman", 15))
    l4.grid(row=3)
    l5=Label(ent, text='Contact Number', width=15)
    l5.config(font=("Times New Roman", 15))
    l5.grid(row=4)
    
    e1 = Entry(ent, font=('Times New Roman',14))
    e2 = Entry(ent, font=('Times New Roman',14))
    e3 = Entry(ent, font=('Times New Roman',14))
    e4 = Entry(ent, font=('Times New Roman',14))
    e5 = Entry(ent, font=('Times New Roman',14))
    e5.bind('<Return>', lambda event:submit(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),ent))
    e1.grid(row=0, column=1)
    e2.grid(row=1, column=1)
    e3.grid(row=2, column=1)
    e4.grid(row=3, column=1)
    e5.grid(row=4, column=1)

    #print("Value of agent = ", e4.get())
    #ent.bind("<FocusIn>", lambda event: handle_focus(e1,ent))
    ent.after(1, lambda: e1.focus_force())

    b1 = Button(ent, text='Submit', width=10, command=lambda:submit(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),ent))
    b2 = Button(ent, text='Done', width=10, command=ent.destroy)
    b1.config(font=("Times New Roman", 15))
    b2.config(font=("Times New Roman", 15))
    b1.grid(row=5, column=1)
    b2.grid(row=5, column=2)
    

#--------------------------------------------------------------------------SEARCH
def srch(text,ent,x):
    global cur

    #query='select * from `gstcontact` where Name like %%({n})%%.format(n=name)'.format(n=name)
    #row_count=cur.execute(query)

    #query='select * from `gstcontact` where Name like %(pl)s'
    #query % {'pl':'%name%'}
    #row_count=cur.execute(query)

    #query='select * from gstcontact where Name like %{0:s}'
    #query.format(name)
    #row_count=cur.execute(query)
    
    #query='select * from `gstcontact` where Name=%s'
    #row_count=cur.execute(query,name)

    
    row_count = cur.execute('select Name,City,GSTIN,Agent,`Contact No.` from custgst')
    allrows = cur.fetchall()
    #print(allrows)
    c=5
    flag=0
    for i in allrows:
        #print(i[0],i[1])
        if text.lower() in i[x]:
            #l0=Label(ent, text="Name")
            #l0.config(font=("Times New Roman", 15))
            #l0.grid(row=c,column=0)
            l1=Label(ent, text=i[0])
            l1.config(font=("Times New Roman", 15))
            l1.grid(row=c+1,column=0)
            l2=Label(ent, text=i[1])
            l2.config(font=("Times New Roman", 15))
            l2.grid(row=c+1,column=1)
            l3=Label(ent, text=i[3])
            l3.config(font=("Times New Roman", 15))
            l3.grid(row=c+1,column=2)
            if(i[4]==0): l4=Label(ent, text=" -- ")
            else: l4=Label(ent, text=i[4])
            l4.config(font=("Times New Roman", 15))
            l4.grid(row=c+1,column=3)
            #Label(ent, text=data[2], state='disabled').grid(row=c,column=1)
            t=Text(ent, height=1, borderwidth=1, width=20, font=("Times New Roman", 15))
            t.tag_configure("center", justify='center')
            t.insert(END,i[2].upper())
            t.tag_add("center", "1.0", "end")
            t.grid(row=c+1,column=5)
            t.configure(state='disabled')
            t.see(END)
            #Entry(ent,text=data[2],fg="black",bg="white",state='readonly').grid(row=c,column=1)
            c=c+1
            flag=1
    if(flag==0):
        l1=Label(ent, text='Record not found')
        l1.config(font=("Times New Roman", 14))
        l1.grid(row=3)

    #row=cur.fetchall()
    #print(row)
    #if(row_count==0):
        #print('no record')
        #Label(ent, text='Record not found').grid(row=3)
    #c=4
    #for index,data in enumerate(row):
        #Label(ent, text=data[1]).grid(row=c,column=0)
        #Label(ent, text=data[2], state='disabled').grid(row=c,column=1)
        #t=Text(ent, height=1, borderwidth=0.5, width=20)
        #t.tag_configure("center", justify='center')
        #t.insert(END,data[2])
        #t.tag_add("center", "1.0", "end")
        #t.grid(row=c,column=1)
        #t.configure(state='disabled')
        #t.see(END)
        ##Entry(ent,text=data[2],fg="black",bg="white",state='readonly').grid(row=c,column=1)
        #c=c+1
        
def search(self):
    ent=Tk()
    ent.title("Search by Name!")
    
    global e1
    l1=Label(ent, text='Enter the name to be searched - ')
    l1.config(font=("Times New Roman", 15))
    l1.grid(row=0)
    e1=Entry(ent, font=('Times New Roman',14))
    e1.bind('<Return>', (lambda event: srch(e1.get(),ent,0)))
    e1.grid(row=0, column=1)

    l2=Label(ent, text='Enter the city to be searched - ')
    l2.config(font=("Times New Roman", 15))
    l2.grid(row=1)
    e2=Entry(ent, font=('Times New Roman',14))
    e2.bind('<Return>', (lambda event: srch(e2.get(),ent,1)))
    e2.grid(row=1, column=1)

    l3=Label(ent, text='Enter the agent to be searched - ')
    l3.config(font=("Times New Roman", 15))
    l3.grid(row=2)
    e3=Entry(ent, font=('Times New Roman',14))
    e3.bind('<Return>', (lambda event: srch(e3.get(),ent,3)))
    e3.grid(row=2, column=1)

    ent.after(1, lambda: e1.focus_force())
    
    b1=Button(ent, text='Search', width=10, command=(lambda:srch(e1.get(),ent,0)))
    b1.config(font=("Times New Roman", 15))
    b1.grid(row=0,column=2)
    b2=Button(ent, text='Search', width=10, command=(lambda:srch(e2.get(),ent,1)))
    b2.config(font=("Times New Roman", 15))
    b2.grid(row=1,column=2)
    b3=Button(ent, text='Search', width=10, command=(lambda:srch(e3.get(),ent,3)))
    b3.config(font=("Times New Roman", 15))
    b3.grid(row=2,column=2)
    b4=Button(ent, text='Done', width=10, command=ent.destroy)
    b4.config(font=("Times New Roman", 15))
    b4.grid(row=3,column=2)
    
    Label(ent, text=' ').grid(row=2)
    Label(ent, text=' ').grid(row=3)



#-------------------------------------------------------------------------------MODIFY

#def bt_dest
        
def modname(name,newname,ent):
    global cur
    query='update `custgst` set `Name`=%s where `Name`=%s'
    cur.execute(query,(newname,name))
    srch(newname,ent,0)
def modcity(name,city,ent):
    global cur
    query='update `custgst` set `City`=%s where `Name`=%s'
    cur.execute(query,(city,name))
    srch(city,ent,1)
def modgstin(name,gst,ent):
    global cur
    query='update `custgst` set `GSTIN`=%s where `Name`=%s'
    cur.execute(query,(gst,name))
    srch(gst,ent,2)
def modagent(name,agent,ent):
    global cur
    query='update `custgst` set `Agent`=%s where `Name`=%s'
    cur.execute(query,(agent,name))
    srch(agent,ent,3)
def modcno(name,cno,ent):
    global cur
    query='update `custgst` set `Contact No.`=%s where `Name`=%s'
    cur.execute(query,(cno,name))
    srch(cno,ent,4)
def check(name,ent):
    global cur
    #bt_dest()
    b1.destroy()
    row_count=cur.execute('select * from custgst where Name=%s',name)
    if(row_count==0):
        ent2=Tk()
        ent2.title("!!")
        l1=Label(ent2, text='Record not found')
        l1.config(font=("Times New Roman", 13))
        l1.pack()
    else:
        l1=Label(ent, text='New Name')
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=1,column=0)
        l2=Label(ent, text='New City')
        l2.config(font=("Times New Roman", 15))
        l2.grid(row=2,column=0)
        l3=Label(ent, text='New GST No.')
        l3.config(font=("Times New Roman", 15))
        l3.grid(row=3,column=0)
        l4=Label(ent, text='New Agent')
        l4.config(font=("Times New Roman", 15))
        l4.grid(row=4,column=0)
        l5=Label(ent, text='New Contact No.')
        l5.config(font=("Times New Roman", 15))
        l5.grid(row=5,column=0)
        
        e2=Entry(ent, font=('Times New Roman',14))
        e2.grid(row=1,column=1)
        e2.bind('<Return>', (lambda event: modname(name,e2.get(),ent)))
        e3=Entry(ent, font=('Times New Roman',14))
        e3.grid(row=2,column=1)
        e3.bind('<Return>', (lambda event: modcity(name,e3.get(),ent)))
        e4=Entry(ent, font=('Times New Roman',14))
        e4.grid(row=3,column=1)
        e4.bind('<Return>', (lambda event: modgstin(name,e4.get(),ent)))
        e5=Entry(ent, font=('Times New Roman',14))
        e5.grid(row=4,column=1)
        e5.bind('<Return>', (lambda event: modagent(name,e5.get(),ent)))
        e6=Entry(ent, font=('Times New Roman',14))
        e6.grid(row=5,column=1)
        e6.bind('<Return>', (lambda event: modcno(name,e6.get(),ent)))
        
        
        b2=Button(ent, text='Modify', command=lambda:modname(name,e2.get(),ent))
        b2.config(font=("Times New Roman", 15))
        b2.grid(row=1,column=2)
        b3=Button(ent, text='Modify', command=lambda:modcity(name,e3.get(),ent))
        b3.config(font=("Times New Roman", 15))
        b3.grid(row=2,column=2)
        b4=Button(ent, text='Modify', command=lambda:modgstin(name,e4.get(),ent))
        b4.config(font=("Times New Roman", 15))
        b4.grid(row=3,column=2)
        b5=Button(ent, text='Modify', command=lambda:modagent(name,e5.get(),ent))
        b5.config(font=("Times New Roman", 15))
        b5.grid(row=4,column=2)
        b6=Button(ent, text='Modify', command=lambda:modcno(name,e6.get(),ent))
        b6.config(font=("Times New Roman", 15))
        b6.grid(row=5,column=2)
def modify(self):
    ent=Tk()
    ent.title("Modify Record!")
    #global e1,e2,e3
    l1=Label(ent, text='Enter the name whose record is to be modified - ')
    l1.config(font=("Times New Roman", 15))
    l1.grid(row=0,column=0)
    e1=Entry(ent, font=('Times New Roman',14))
    e1.grid(row=0,column=1)
    e1.bind('<Return>', (lambda event: check(e1.get(),ent)))
    ent.after(1, lambda: e1.focus_force())
    
    b1=Button(ent, text='Enter', command=lambda:check(e1.get(),ent))
    b1.config(font=("Times New Roman", 15))
    b1.grid(row=1,column=4)
    #b1.destroy()
    
    #call=partial(modname,e1.get(),e2.get(),ent)


    
#------------------------------------------------------------------------------DELETE
def delete(name,ent):
    global cur
    row_count=cur.execute('select * from custgst where Name=%s',name)
    #row1=cur.fetchone()
    if(row_count==0):
        l1=Label(ent, text='Record not found').grid(row=2)
        l1.config(font=("Times New Roman", 15))
    else:
        query='delete from custgst where Name=%s'
        cur.execute(query,name)
        l1=Label(ent, text='Record Deleted!')
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=2)
def remove(self):
    ent=Tk()
    ent.title('Delete record!')
    e1=Entry(ent, font=('Times New Roman',14))
    ent.after(1, lambda: e1.focus_force())
    
    l1=Label(ent, text='Enter the name whose record is to be deleted - ')
    l1.config(font=("Times New Roman", 15))
    l1.grid(row=0,column=0)
    
    e1.bind('<Return>', (lambda event:delete(e1.get(),ent)))
    e1.grid(row=0,column=1)
    b1=Button(ent, text='Delete', command=lambda:delete(e1.get(),ent))
    b1.config(font=("Times New Roman", 15))
    b1.grid(row=1,column=1)
    b2=Button(ent, text='Done', command=ent.destroy)
    b2.config(font=("Times New Roman", 15))
    b2.grid(row=1,column=2)
    

#---------------------------------------------------------------DISPLAY ALL
def displayall(self):
    ent=Tk()
    ent.title('All Records!')
    row_count=cur.execute('select * from custgst')
    row=cur.fetchall()
    scrollbar = Scrollbar(ent,orient=VERTICAL)
    scrollbar.grid(rowspan=row_count,column=3, sticky='ns')

    #listbox = tk.Listbox(root, width=20, height=6)
    #listbox.grid(row=0, column=0)
        
    if(row_count==0):
        #print('no record')
        l1=Label(ent, text='Record not found')
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=3)
    for index,data in enumerate(row):
        #Label(ent, text=data[0]).grid(row=index+1,column=0)
        l1=Label(ent, text=data[1])
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=index+1,column=1)
        #Label(ent, text=data[2], state='disabled').grid(row=c,column=1)
        t=Text(ent, height=1, borderwidth=0.5, width=20, yscrollcommand=scrollbar.set, font=("Times New Roman", 15))
        scrollbar.config(command=t.yview)
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
    m.title("Customer GST")
    l1=Label(m, text="Welcome!", fg="red")
    l1.config(font=("Times New Roman", 27))
    l1.pack()
    
    l2=Label(m, text=" ", width=30)
    l2.pack()

    m.bind('n',entry)
    b1=Button(m, text="New Entry", width=30, command=entry, height=2)
    b1.config(font=("Times New Roman", 15))
    b1.pack()

    m.bind('s',search)
    b2=Button(m, text="Search by name", width=30, command=search, height=2)
    b2.config(font=("Times New Roman", 15))
    b2.pack()

    m.bind('m',modify)
    b3=Button(m, text="Modify", width=30, command=modify, height=2)
    b3.config(font=("Times New Roman", 15))
    b3.pack()

    m.bind('r',remove)
    b4=Button(m, text="Remove", width=30, command=remove, height=2)
    b4.config(font=("Times New Roman", 15))
    b4.pack()

    m.bind('d',displayall)
    b5=Button(m, text="Display all records", width=30, command=displayall, height=2)
    b5.config(font=("Times New Roman", 15))
    b5.pack()

    b6=Button(m, text='Close', width=30, command=m.destroy, height=2)
    b6.config(font=("Times New Roman", 15))
    b6.pack()

    m.mainloop()
