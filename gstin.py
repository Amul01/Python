import pymysql
conn=pymysql.connect(host='amul01.000webhost.com', user='id8115473_amul', password='dbgst', db='id8115473_gst')
cur=conn.cursor()

exit=1
while(exit!=0):
    print("\n--------------MENU--------------\n1. Add new\n2. Search by name")
    print("3. Modify\n4. Remove\n5. Display all records\n6. Exit")
    ch=int(input("Enter your choice: "))
    if(ch==1):
        print("---------------------------------")
        name=input("Enter name: ")
        gstin=input("Enter the GST number: ")
        query='insert into gstcontact (Name, GSTIN) values (%s,%s)'
        cur.execute(query,(name,gstin))
        #query='select max(Sr. No.) from gstcontact'
        #cur.execute(query)
        #maxi=cur.fetchone()
        #cur.execute('select * from gstcontact where ID=%s',maxi)
        #cur.execute('select * from gstcontact order by ID desc limit 1')
        #cur.execute('select top 1 * from gstcontact order by ID desc')
        #row1=cur.fetchone()
        #print("Inserted values: ", row1)
        conn.commit()

        
    elif(ch==2):
        print("---------------------------------")
        name=input("Enter search name: ")
        query='select * from `gstcontact` where Name=%s'
        cur.execute(query,name)
        row=cur.fetchall()
        if(row==None): print("Name not found")
        else:
            for row1 in row:
                print(row1[0],"\t",row1[1],"\t",row1[2])
                    
    elif(ch==3):
        print("---------------------------------")
        name=input("Enter the name whose record is to be modified:")
        cur.execute('select * from gstcontact where Name=%s',name)
        row1=cur.fetchone()
        if(row1==None): print("Name not found")
        else:
            print("1. Modify name?\n2. Modify GST no.?")
            ch=int(input("Enter your choice: "))
            if(ch==1):
                newname=input("Enter new name: ")
                query='update `gstcontact` set `Name`=%s where `Name`=%s'
                cur.execute(query,(newname,name))
                print("Succesfully updated!!")
            elif(ch==2):
                newgst=input("Enter new GST No.: ")
                query='update gstcontact set GSTIN=%s where Name=%s'
                cur.execute(query,(newgst,name))
                print("Succesfully updated!!")
            else:
                print("Wrong choice entered")
            
    elif(ch==4):
        print("---------------------------------")
        name=input("Enter the name whose record is to be deleted:")
        cur.execute('select * from gstcontact where Name=%s',name)
        row1=cur.fetchone()
        if(row1==None): print("Name not found")
        else:
            query='delete from gstcontact where Name=%s'
            cur.execute(query,name)

    elif(ch==5):
        cur.execute('select * from gstcontact')
        for row in cur:
            print(row)

    elif(ch==6): exit=0
    else: print("Wrong choice entered.")

conn.commit()
