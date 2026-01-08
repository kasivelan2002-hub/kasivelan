from tkinter import *
import random
import time
from tkinter import ttk
from tkinter import messagebox
import mysql.connector as mysql
import os



def system():
    root = Tk()
    root.geometry("1700x800")
    root.title("Cafe Invoice System")
    root.config(bg = "azure2")
    

    def Database():
        global connectn, cursor
        connectn = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database = "jones"
            )
        cursor = connectn.cursor()
        
        cursor.execute(
            "CREATE TABLE IF NOT EXISTS records(ordno text,muf text,bro text,dou text,cof text,ct text,sb text,tax text,sr text,tot text)")

    
    orderno = StringVar()
    muffin = StringVar()
    brownie = StringVar()
    doughnut = StringVar()
    coffee = StringVar()
    cost = StringVar()
    subtotal = StringVar()
    tax = StringVar()
    service = StringVar()
    total = StringVar()

    
    def tottal():
        
        order = (orderno.get())
        muf = float(muffin.get())
        bro = float(brownie.get())
        dou = float(doughnut.get())
        cof = float(coffee.get())
        

        

        costmuf = muf * 160
        costbro = bro * 150
        costdou = dou *100
        costcof = cof * 75
        

        
        costofmeal = (costmuf + costbro + costdou + costcof )
        ptax = ((costmuf + costbro + costdou + costcof ) * 0.18)
        sub = (costmuf + costbro + costdou + costcof )
        ser = ((costmuf + costbro + costdou + costcof ) / 99)
        paidtax = str(ptax)
        Service = str(ser)
        overall = str(ptax + ser + sub)

        
        cost.set(costofmeal)
        tax.set(ptax)
        subtotal.set(sub)
        service.set(ser)
        total.set(overall)

    
    def reset():
        orderno.set("")
        muffin.set("")
        brownie.set("")
        doughnut.set("")
        coffee.set("")
        cost.set("")
        subtotal.set("")
        tax.set("")
        service.set("")
        total.set("")

    
    def exit():
        root.destroy()

   
    topframe = Frame(root, bg="white", width=1600, height=50)
    topframe.pack(side=TOP)

    leftframe = Frame(root,bg='azure2', width=900, height=700)
    leftframe.pack(side=LEFT)

    
    rightframe = Frame(root,bg="azure2", width=400, height=700)
    rightframe.pack(side=RIGHT)

    
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor  =connectn.cursor()
        cursor.execute("SELECT * FROM records")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    style = ttk.Style()
    style.configure("Treeview",
                    foreground="black",
                    rowheight=40,
                    fieldbackground="white"
                    )
    style.map('Treeview',
              background=[('selected', 'lightblue')])

    
    my_tree = ttk.Treeview(rightframe)
    my_tree['columns'] = ("ordno", "muf","bro", "dou", "cof","ct", "sb", "tax", "sr", "tot")

    
    horizontal_bar = ttk.Scrollbar(rightframe, orient="horizontal")
    horizontal_bar.configure(command=my_tree.xview)
    my_tree.configure(xscrollcommand=horizontal_bar.set)
    horizontal_bar.pack(fill=X, side=BOTTOM)

    vertical_bar = ttk.Scrollbar(rightframe, orient="vertical")
    vertical_bar.configure(command=my_tree.yview)
    my_tree.configure(yscrollcommand=vertical_bar.set)
    vertical_bar.pack(fill=Y, side=RIGHT)

    
    my_tree.column("#0", width=0, minwidth=0)
    my_tree.column("ordno", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("muf", anchor=CENTER, width=60, minwidth=25)
    my_tree.column("bro", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("dou", anchor=CENTER, width=80, minwidth=25)
    my_tree.column("cof", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("ct", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sb", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tax", anchor=CENTER, width=50, minwidth=25)
    my_tree.column("sr", anchor=CENTER, width=100, minwidth=25)
    my_tree.column("tot", anchor=CENTER, width=50, minwidth=25)

    
    my_tree.heading("ordno", text="Order No", anchor=CENTER)
    my_tree.heading("muf", text="Muffin", anchor=CENTER)
    my_tree.heading("bro", text="Brownie", anchor=CENTER)
    my_tree.heading("dou", text="Doughnut", anchor=CENTER)
    my_tree.heading("cof", text="coffee", anchor=CENTER)
    my_tree.heading("ct", text="Cost", anchor=CENTER)
    my_tree.heading("sb", text="Subtotal", anchor=CENTER)
    my_tree.heading("tax", text="Tax", anchor=CENTER)
    my_tree.heading("sr", text="Service", anchor=CENTER)
    my_tree.heading("tot", text="Total", anchor=CENTER)

    my_tree.pack()
    DisplayData()

    
    def add():
        Database()
      
        orders = orderno.get()
        muffins = muffin.get()
        brownies = brownie.get()
        doughnuts = doughnut.get()
        coffees = coffee.get()
        costs = cost.get()
        subtotals = subtotal.get()
        taxs = tax.get()
        services = service.get()
        totals = total.get()
        if orders == "" or muffins == "" or brownies == "" or doughnuts == "" or coffees == "" or costs == "" or subtotals == "" or taxs == "" or services == "" or totals == "":

            messagebox.showinfo("Warning", "Please fill the empty field!!!")
        else:
            connectn = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database = "jones"
            )
            cursor = connectn.cursor()
            sql='INSERT INTO records ( ordno, muf, bro, dou, cof, ct, sb, tax, sr, tot)VALUES (%s,%s,%s,%s,%s,%s,%s,%s,%s,%sval =(orders,muffins,brownies,doughnut,coffees,costs,subtotals,taxs,services, totals)'
            val=(orders, muffins, brownies, doughnuts, coffees, costs, subtotals, taxs, services, totals);
            cursor.execute(sql, val)
            connectn.commit()
            messagebox.showinfo("Message", "Stored successfully")
        
        DisplayData()
        connectn.close()

    
    def DisplayData():
        Database()
        my_tree.delete(*my_tree.get_children())
        cursor = connectn.cursor()
        cursor.execute("SELECT * FROM records")
        fetch = cursor.fetchall()
        for data in fetch:
            my_tree.insert('', 'end', values=(data))
        cursor.close()
        connectn.close()

    
    def Delete():
       
        Database()
        if not my_tree.selection():
            messagebox.showwarning("Warning", "Select data to delete")
        else:
            result = messagebox.askquestion('Confirm', 'Are you sure you want to delete this record?',
                                            icon="warning")
        if result == 'yes':
            curItem = my_tree.focus()
            contents = (my_tree.item(curItem))
            selecteditem = contents['values']
            my_tree.delete(curItem)
            cursor=connectn.cursor()
            cursor.execute("DELETE FROM records WHERE ordno= %s" % selecteditem[0])
            connectn.commit()
            cursor.close()
            connectn.close()

    
    localtime = time.asctime(time.localtime(time.time()))
    
    main_lbl = Label(topframe, font=('Gabriola', 25, 'bold'),bg="azure2", text="Cafe Invoice System", fg="red",
                   anchor=W)
    main_lbl.grid(row=0, column=0)
    main_lbl = Label(topframe, font=('Calibri', 15,'bold'), bg="azure2",text=localtime, fg="black", anchor=W)
    main_lbl.grid(row=1, column=0)

    
    ordlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Order No.", fg="black",bg="azure2", bd=5, anchor=W).grid(row=1,
                                                                                                             column=0)
    ordtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=orderno).grid(row=1, column=1)
    
    muflbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Muffin", fg="black", bd=5,bg="azure2",anchor=W).grid(row=2,
                                                                                                         column=0)
    muftxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=muffin).grid(row=2, column=1)
    
    brolbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Brownie", fg="black", bd=5, bg="azure2",anchor=W).grid(row=3,
                                                                                                          column=0)
    brotxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=brownie).grid(row=3, column=1)

    
    doulbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Doughnut", fg="black", bd=5,bg="azure2", anchor=W).grid(row=4,
                                                                                                             column=0)
    doutxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                   textvariable=doughnut).grid(row=4, column=1)
    
    coffeelbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Coffee", fg="black", bd=5, bg="azure2",anchor=W).grid(row=5,
                                                                                                            column=0)
    coffeetxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                     textvariable=coffee).grid(row=5, column=1)
   
    
    costlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Cost", bd=5,bg="azure2",anchor=W).grid(row=7, column=0)
    costtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                    textvariable=cost).grid(row=7, column=1)
    sublbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Subtotal", bd=5,bg="azure2",anchor=W).grid(row=8, column=0)
    subtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',textvariable=subtotal).grid(row=8, column=1)
    
    taxlbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Tax", bd=5, bg="azure2",anchor=W).grid(row=9, column=0)
    taxtxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',                   textvariable=tax).grid(row=9, column=1)
    
    servicelbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Service", bd=5, bg="azure2",anchor=W).grid(row=10,
                                                                                                              column=0)
    servicetxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                       textvariable=service).grid(row=10, column=1)
    
    totallbl = Label(leftframe, font=('Calibri', 16, 'bold'), text="Total", bd=5, bg="azure2",anchor=W).grid(row=11,
                                                                                                          column=0)
    totaltxt = Entry(leftframe, font=('Calibri', 16, 'bold'), bd=6, insertwidth=4, justify='right',
                     textvariable=total).grid(row=11, column=1)
  


    totbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Total", bg="Lightgrey", fg="black", bd=3, padx=5, pady=5,
                    width=6, command=tottal).grid(row=6, column=3)

    resetbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Reset", bg="lightgrey", fg="black", bd=3, padx=5,
                      pady=5, width=6, command=reset).grid(row=4, column=3)

    exitbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Exit The System", bg="lightgrey", fg="black", bd=3, padx=5,
                     pady=5, width=12, command=exit).grid(row=6, column=2)

    addbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Add", bg="lightgrey", fg="black", bd=3, padx=5, pady=5,
                    width=6, command=add).grid(row=2, column=3)

    deletebtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Delete Record", bg="lightgrey", fg="black", bd=3,
                       padx=5, pady=5, width=12, command=Delete).grid(row=4, column=2)

    

    def feedbackk():
        feed = Tk()
        feed.geometry("600x500")
        feed.title("Submit Feedback form")
       
        connectn = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database = "jones"
            )
        cursor = connectn.cursor()
        cursor.execute("CREATE TABLE IF NOT EXISTS feedback(n text,eid text,feedback5 text,com text)")
        
        name = StringVar()
        email = StringVar()
        com = StringVar()
        
        def submit():
            n = name.get()
            eid = email.get()
            com = txt.get('1.0', END)
            feedback1 = ""
            feedback2 = ""
            feedback3 = ""
            feedback4 = ""
            if (checkvar1.get() == "1"):
                feedback1 = "Excellent"
            if (checkvar2.get() == "1"):
                feedback2 = "Good"
            if (checkvar3.get() == "1"):
                feedback2 = "Average"
            if (checkvar4.get() == "1"):
                feedback2 = "Poor"
            feedback5 = feedback1 + " " + feedback2 + " " + feedback3 + " " + feedback4
            conn = mysql.connect(
            host="localhost",
            user="root",
            password="",
            database = "jones"
            )
            cursor = conn.cursor()
            
            sql='INSERT INTO feedback (n,eid,feedback5,com) VALUES (%s,%s,%s,%s)';
            val=(n,eid,com,feedback5);
            cursor.execute(sql, val)


            
            conn.commit()
            messagebox.showinfo("message", "data inserted !")
            feed.destroy()

        
        def cancel():
            feed.destroy()

        
        lb1 = Label(feed, font=("Calisto MT", 15, "bold"), text="Thanks for Visiting!", fg="black").pack(side=TOP)
        lbl2 = Label(feed, font=("calisto MT", 15), text="We're glad you chose us ! Please tell us how it was!",
                     fg="black").pack(side=TOP)
        
        namelbl = Label(feed, font=('vardana', 15), text="Name:-", fg="black", bd=10, anchor=W).place(x=10, y=150)
        nametxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                        textvariable=name).place(x=15, y=185)
        
        emaillbl = Label(feed, font=('vardana', 15), text="Email:-", fg="black", bd=10, anchor=W).place(x=280, y=150)
        emailtxt = Entry(feed, font=('vardana', 15), bd=6, insertwidth=2, bg="white", justify='right',
                         textvariable=email).place(x=285, y=185)
        
        ratelbl = Label(feed, font=('vardana', 15), text="How would you rate us?", fg="black", bd=10, anchor=W).place(
            x=10, y=215)
        checkvar1 = StringVar()
        checkvar2 = StringVar()
        checkvar3 = StringVar()
        checkvar4 = StringVar()
        c1 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Excellent", bg="white", variable=checkvar1)
        c1.deselect()
        c1.place(x=15, y=265)
        c2 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="Good", bg="white", variable=checkvar2, )
        c2.deselect()
        c2.place(x=120, y=265)
        c3 = Checkbutton(feed, font=('Calibri', 10, "bold"), text=" Average", bg="white", variable=checkvar3, )
        c3.deselect()
        c3.place(x=220, y=265)
        c4 = Checkbutton(feed, font=('Calibri', 10, "bold"), text="   Poor  ", bg="white", variable=checkvar4, )
        c4.deselect()
        c4.place(x=320, y=265)
        
        commentslbl = Label(feed, font=('Calibri', 15), text="Comments", fg="black", bd=10, anchor=W).place(x=10, y=300)
        txt = Text(feed, width=50, height=5)
        txt.place(x=15, y=335)
        
        submit = Button(feed, font=("Calibri", 15), text="Submit", fg="black", bg="green", bd=2, command=submit).place(
            x=145, y=430)
        cancel = Button(feed, font=("Calibri", 15), text="Cancel", fg="black", bg="red", bd=2, command=cancel).place(
            x=245, y=430)
        feed.mainloop()

    
    feedbtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Feedback Form", fg="black", bg="lightgrey", bd=3, padx=10,
                     pady=10, width=10, command=feedbackk).grid(row=8, column=2, columnspan=1)

    
    def menu():
        roott = Tk()
        roott.title("Price Menu")
        roott.geometry("300x300")
        lblinfo = Label(roott, font=("Calibri", 20, "bold"), text="ITEM LIST", fg="black", bd=10)
        lblinfo.grid(row=0, column=0)
        lblprice = Label(roott, font=("Calibri", 20, "bold"), text="Prices", fg="black", bd=10)
        lblprice.grid(row=0, column=3)
        lblmuffin = Label(roott, font=("Calibri", 20, "bold"), text="Muffin", fg="Blue", bd=10)
        lblmuffin.grid(row=1, column=0)
        lblpricem = Label(roott, font=("Calibri", 20, "bold"), text="160/-", fg="blue", bd=10)
        lblpricem.grid(row=1, column=3)
        lblbrownie = Label(roott, font=("Calibri", 20, "bold"), text="Brownie", fg="Blue", bd=10)
        lblbrownie.grid(row=3, column=0)
        lblpriceb = Label(roott, font=("Calibri", 20, "bold"), text="150/-", fg="blue", bd=10)
        lblpriceb.grid(row=3, column=3)
        lbldoughnut = Label(roott, font=("Calibri", 20, "bold"), text="Doughnut", fg="Blue", bd=10)
        lbldoughnut.grid(row=4, column=0)
        lblpriced = Label(roott, font=("Calibri", 20, "bold"), text="100/-", fg="blue", bd=10)
        lblpriced.grid(row=4, column=3)
        lblcoffee = Label(roott, font=("Calibri", 20, "bold"), text="Coffee", fg="Blue", bd=10)
        lblcoffee.grid(row=5, column=0)
        lblpricec = Label(roott, font=("Calibri", 20, "bold"), text="75/-", fg="blue", bd=10)
        lblpricec.grid(row=5, column=3)
        roott.mainloop()

        roott.mainloop()

 
    menubtn = Button(leftframe, font=('Calibri', 16, 'bold'), text="Menu Card", bg="lightgrey", fg="black", bd=3, padx=6,
                     pady=6, width=12, command=menu).grid(row=2, column=2)
root.mainloop()
system()
