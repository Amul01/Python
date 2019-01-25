from tkinter import *
import pymysql

class customer:
    #def __init__(self,m):
        #ent=m

    def submit(self,name,city,gstin,agent,cno,ent):
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
        e5.bind('<Return>', lambda event: self.submit(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),ent))
        e1.grid(row=0, column=1)
        e2.grid(row=1, column=1)
        e3.grid(row=2, column=1)
        e4.grid(row=3, column=1)
        e5.grid(row=4, column=1)

        #print("Value of agent = ", e4.get())
        #ent.bind("<FocusIn>", lambda event: handle_focus(e1,ent))
        ent.after(1, lambda: e1.focus_force())

        b1 = Button(ent, text='Submit', width=10, command=lambda: self.submit(e1.get(),e2.get(),e3.get(),e4.get(),e5.get(),ent))
        b2 = Button(ent, text='Done', width=10, command=ent.destroy)
        b1.config(font=("Times New Roman", 15))
        b2.config(font=("Times New Roman", 15))
        b1.grid(row=5, column=1)
        b2.grid(row=5, column=2)
        

    #--------------------------------------------------------------------------SEARCH
    def srch(self,text,ent,x):
        global cur
        
        row_count = cur.execute('select Name,City,GSTIN,Agent,`Contact No.` from custgst')
        allrows = cur.fetchall()
        #print(allrows)
        c=5
        flag=0
        for i in allrows:
            #print(i[0],i[1])
            if text.lower() in i[x]:
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
            
    def search(self):
        ent=Tk()
        ent.title("Search by Name!")
        
        global e1
        l1=Label(ent, text='Enter the name to be searched - ')
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=0)
        e1=Entry(ent, font=('Times New Roman',14))
        e1.bind('<Return>', (lambda event: self.srch(e1.get(),ent,0)))
        e1.grid(row=0, column=1)

        l2=Label(ent, text='Enter the city to be searched - ')
        l2.config(font=("Times New Roman", 15))
        l2.grid(row=1)
        e2=Entry(ent, font=('Times New Roman',14))
        e2.bind('<Return>', (lambda event: self.srch(e2.get(),ent,1)))
        e2.grid(row=1, column=1)

        l3=Label(ent, text='Enter the agent to be searched - ')
        l3.config(font=("Times New Roman", 15))
        l3.grid(row=2)
        e3=Entry(ent, font=('Times New Roman',14))
        e3.bind('<Return>', (lambda event: self.srch(e3.get(),ent,3)))
        e3.grid(row=2, column=1)

        ent.after(1, lambda: e1.focus_force())
        
        b1=Button(ent, text='Search', width=10, command=(lambda: self.srch(e1.get(),ent,0)))
        b1.config(font=("Times New Roman", 15))
        b1.grid(row=0,column=2)
        b2=Button(ent, text='Search', width=10, command=(lambda: self.srch(e2.get(),ent,1)))
        b2.config(font=("Times New Roman", 15))
        b2.grid(row=1,column=2)
        b3=Button(ent, text='Search', width=10, command=(lambda: self.srch(e3.get(),ent,3)))
        b3.config(font=("Times New Roman", 15))
        b3.grid(row=2,column=2)
        b4=Button(ent, text='Done', width=10, command=ent.destroy)
        b4.config(font=("Times New Roman", 15))
        b4.grid(row=3,column=2)
        
        Label(ent, text=' ').grid(row=2)
        Label(ent, text=' ').grid(row=3)



    #-------------------------------------------------------------------------------MODIFY

    #def bt_dest

    def check(self,name,ent):
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
            e2.bind('<Return>', (lambda event: self.modname(name,e2.get(),ent)))
            e3=Entry(ent, font=('Times New Roman',14))
            e3.grid(row=2,column=1)
            e3.bind('<Return>', (lambda event: self.modcity(name,e3.get(),ent)))
            e4=Entry(ent, font=('Times New Roman',14))
            e4.grid(row=3,column=1)
            e4.bind('<Return>', (lambda event: self.modgstin(name,e4.get(),ent)))
            e5=Entry(ent, font=('Times New Roman',14))
            e5.grid(row=4,column=1)
            e5.bind('<Return>', (lambda event: self.modagent(name,e5.get(),ent)))
            e6=Entry(ent, font=('Times New Roman',14))
            e6.grid(row=5,column=1)
            e6.bind('<Return>', (lambda event: self.modcno(name,e6.get(),ent)))
            
            
            b2=Button(ent, text='Modify', command=lambda: self.modname(name,e2.get(),ent))
            b2.config(font=("Times New Roman", 15))
            b2.grid(row=1,column=2)
            b3=Button(ent, text='Modify', command=lambda: self.modcity(name,e3.get(),ent))
            b3.config(font=("Times New Roman", 15))
            b3.grid(row=2,column=2)
            b4=Button(ent, text='Modify', command=lambda: self.modgstin(name,e4.get(),ent))
            b4.config(font=("Times New Roman", 15))
            b4.grid(row=3,column=2)
            b5=Button(ent, text='Modify', command=lambda: self.modagent(name,e5.get(),ent))
            b5.config(font=("Times New Roman", 15))
            b5.grid(row=4,column=2)
            b6=Button(ent, text='Modify', command=lambda: self.modcno(name,e6.get(),ent))
            b6.config(font=("Times New Roman", 15))
            b6.grid(row=5,column=2)
            
    def modname(self,name,newname,ent):
        global cur
        query='update `custgst` set `Name`=%s where `Name`=%s'
        cur.execute(query,(newname,name))
        self.srch(newname,ent,0)
    def modcity(self,name,city,ent):
        global cur
        query='update `custgst` set `City`=%s where `Name`=%s'
        cur.execute(query,(city,name))
        self.srch(city,ent,1)
    def modgstin(self,name,gst,ent):
        global cur
        query='update `custgst` set `GSTIN`=%s where `Name`=%s'
        cur.execute(query,(gst,name))
        self.srch(gst,ent,2)
    def modagent(self,name,agent,ent):
        global cur
        query='update `custgst` set `Agent`=%s where `Name`=%s'
        cur.execute(query,(agent,name))
        self.srch(agent,ent,3)
    def modcno(self,name,cno,ent):
        global cur
        query='update `custgst` set `Contact No.`=%s where `Name`=%s'
        cur.execute(query,(cno,name))
        self.srch(cno,ent,4)
    def modify(self):
        ent=Tk()
        ent.title("Modify Record!")
        #global e1,e2,e3
        l1=Label(ent, text='Enter the name whose record is to be modified - ')
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=0,column=0)
        e1=Entry(ent, font=('Times New Roman',14))
        e1.grid(row=0,column=1)
        e1.bind('<Return>', (lambda event: self.check(e1.get(),ent)))
        ent.after(1, lambda: e1.focus_force())
        
        b1=Button(ent, text='Enter', command=lambda: self.check(e1.get(),ent))
        b1.config(font=("Times New Roman", 15))
        b1.grid(row=1,column=4)
        #b1.destroy()
        
        #call=partial(modname,e1.get(),e2.get(),ent)


        
    #------------------------------------------------------------------------------DELETE
    def delete(self,name,ent):
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
        
        e1.bind('<Return>', (lambda event: self.delete(e1.get(),ent)))
        e1.grid(row=0,column=1)
        b1=Button(ent, text='Delete', command=lambda: self.delete(e1.get(),ent))
        b1.config(font=("Times New Roman", 15))
        b1.grid(row=1,column=1)
        b2=Button(ent, text='Done', command=ent.destroy)
        b2.config(font=("Times New Roman", 15))
        b2.grid(row=1,column=2)



#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------




class transport:
    def submit(name,gstin,ent):
        global cur
        query='insert into gstcontact (Name, GSTIN) values (%s,%s)'
        cur.execute(query,(name,gstin))
        cur.execute('SELECT Name FROM gstcontact ORDER BY ID DESC LIMIT 1')
        #print(cur.fetchall()[0][0])
        if(cur.fetchall()[0][0]==name):
            l1=Label(ent, text='Entry Successful')
            l1.config(font=("Times New Roman", 15))
            l1.grid(row=3)
        conn.commit()
    def entry(self):
        ent=Tk()
        ent.title("New Entry!")
        ent.focus_set()
        #global e1,e2
        l1=Label(ent, text='Name', width=15)
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=0) 
        l2=Label(ent, text='GST No.', width=15)
        l2.config(font=("Times New Roman", 15))
        l2.grid(row=1) 
        e1 = Entry(ent, font=('Times New Roman',14))
        e2 = Entry(ent, font=('Times New Roman',14))
        e2.bind('<Return>', lambda event: submit(e1.get(),e2.get(),ent))
        e1.grid(row=0, column=1)
        #e1.focus_set()
        e2.grid(row=1, column=1)

        #ent.bind("<FocusIn>", lambda event: handle_focus(e1,ent))
        ent.after(1, lambda: e1.focus_force())

        b1 = Button(ent, text='Submit', width=10, command=lambda:submit(e1.get(),e2.get(),ent))
        b2 = Button(ent, text='Done', width=10, command=ent.destroy)
        b1.config(font=("Times New Roman", 15))
        b2.config(font=("Times New Roman", 15))
        b1.grid(row=2, column=1)
        b2.grid(row=2, column=2)



    #--------------------------------------------------------------------------SEARCH
    def srch(self,name,ent):
        global cur
        row_count = cur.execute('select Name,GSTIN from gstcontact')
        allrows = cur.fetchall()
        #print(allrows)
        c=4
        flag=0
        for i in allrows:
            #print(i[0],i[1])
            if name in i[0]:
                l1=Label(ent, text=i[0])
                l1.config(font=("Times New Roman", 15))
                l1.grid(row=c,column=0)
                #Label(ent, text=data[2], state='disabled').grid(row=c,column=1)
                t=Text(ent, height=1, borderwidth=1, width=20, font=("Times New Roman", 15))
                t.tag_configure("center", justify='center')
                t.insert(END,i[1])
                t.tag_add("center", "1.0", "end")
                t.grid(row=c,column=1)
                t.configure(state='disabled')
                t.see(END)
                #Entry(ent,text=data[2],fg="black",bg="white",state='readonly').grid(row=c,column=1)
                c=c+1
                flag=1
        if(flag==0):
            l1=Label(ent, text='Record not found')
            l1.config(font=("Times New Roman", 14))
            l1.grid(row=3)
            
    def search(self):
        ent=Tk()
        ent.title("Search by Name!")
        
        global e1
        l1=Label(ent, text='Enter the name to be searched - ')
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=0)
        e1=Entry(ent, font=('Times New Roman',14))
        e1.bind('<Return>', (lambda event: self.srch(e1.get(),ent)))
        e1.grid(row=0, column=1)

        ent.after(1, lambda: e1.focus_force())
        
        b1=Button(ent, text='Search', width=10, command=(lambda: self.srch(e1.get(),ent)))
        b1.config(font=("Times New Roman", 15))
        b1.grid(row=1,column=1)
        b2=Button(ent, text='Done', width=10, command=ent.destroy)
        b2.config(font=("Times New Roman", 15))
        b2.grid(row=1,column=2)
        
        Label(ent, text=' ').grid(row=2)
        Label(ent, text=' ').grid(row=3)



    #-------------------------------------------------------------------------------MODIFY
    def check(name,ent):
        global cur
        row_count=cur.execute('select * from gstcontact where Name=%s',name)
        if(row_count==0):
            l1=Label(ent, text='Record not found')
            l1.config(font=("Times New Roman", 13))
            l1.grid(row=2)
        else:
            l1=Label(ent, text='New Name')
            l1.config(font=("Times New Roman", 15))
            l1.grid(row=1,column=0)
            l2=Label(ent, text='New GST No.')
            l2.config(font=("Times New Roman", 15))
            l2.grid(row=2,column=0)
            e2=Entry(ent, font=('Times New Roman',14))
            e2.grid(row=1,column=1)
            e2.bind('<Return>', (lambda event: self.modname(name,e2.get(),ent)))
            e3=Entry(ent, font=('Times New Roman',14))
            e3.grid(row=2,column=1)
            e3.bind('<Return>', (lambda event: self.modgstin(name,e3.get(),ent)))
            b2=Button(ent, text='Modify', command=lambda: self.modname(name,e2.get(),ent))
            b2.config(font=("Times New Roman", 15))
            b2.grid(row=1,column=2)
            b3=Button(ent, text='Modify', command=lambda: self.modgstin(name,e3.get(),ent))
            b3.config(font=("Times New Roman", 15))
            b3.grid(row=2,column=2)
    def modname(name,newname,ent):
        global cur
        query='update `gstcontact` set `Name`=%s where `Name`=%s'
        cur.execute(query,(newname,name))
        self.srch(newname,ent)
    def modgstin(name,gst,ent):
        global cur
        query='update `gstcontact` set `GSTIN`=%s where `Name`=%s'
        cur.execute(query,(gst,name))
        self.srch(name,ent)
    def modify(self):
        ent=Tk()
        ent.title("Modify Record!")

        #global e1,e2,e3
        l1=Label(ent, text='Enter the name whose record is to be modified - ')
        l1.config(font=("Times New Roman", 15))
        l1.grid(row=0,column=0)
        e1=Entry(ent, font=('Times New Roman',14))
        e1.grid(row=0,column=1)
        e1.bind('<Return>', (lambda event: self.check(e1.get(),ent)))
        ent.after(1, lambda: e1.focus_force())
        
        b1=Button(ent, text='Enter', command=lambda: self.check(e1.get(),ent))
        b1.config(font=("Times New Roman", 15))
        b1.grid(row=2,column=1)
        
        #call=partial(modname,e1.get(),e2.get(),ent)
    
    #------------------------------------------------------------------------------DELETE
    def delete(name,ent):
        global cur
        row_count=cur.execute('select * from gstcontact where Name=%s',name)
        #row1=cur.fetchone()
        if(row_count==0):
            l1=Label(ent, text='Record not found').grid(row=2)
            l1.config(font=("Times New Roman", 15))
        else:
            query='delete from gstcontact where Name=%s'
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
        
        e1.bind('<Return>', (lambda event: self.delete(e1.get(),ent)))
        e1.grid(row=0,column=1)
        b1=Button(ent, text='Delete', command=lambda: self.delete(e1.get(),ent))
        b1.config(font=("Times New Roman", 15))
        b1.grid(row=1,column=1)
        b2=Button(ent, text='Done', command=ent.destroy)
        b2.config(font=("Times New Roman", 15))
        b2.grid(row=1,column=2)
        

#--------------------------------------------------------------------------------------------------------------------------------------
#--------------------------------------------------------------------------------------------------------------------------------------
        
    
if __name__ == "__main__":
    conn=pymysql.connect(host='localhost', user='root', password='', db='gst')
    cur=conn.cursor()

    C=customer()
    T=transport()
    
    m=Tk()
    m.title("INFORMATION")

    menu=Menu(m)
    cm=Menu(m,tearoff=0)
    cm.add_command(label='New Customer', command=C.entry)
    cm.add_command(label='Search', command=C.search)
    #cm.add_command(label='Search by city')
    cm.add_command(label='Remove', command=C.remove)
    menu.add_cascade(label='Customer', menu=cm)
    
    tm=Menu(m,tearoff=0)
    tm.add_command(label='New Transport', command=T.entry)
    tm.add_command(label='Search', command=T.search)
    tm.add_command(label='Remove', command=T.remove)
    menu.add_cascade(label='Transport', menu=tm)

    m.config(menu=menu, padx=50, pady=50)

    Label(m,text='WELCOME SAREES').grid(row=1)
    #Label(m,text='')
    Label(m,text='D/1195-96, MTM').grid(row=2)
    m.mainloop()
