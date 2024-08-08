
import json
import os
from datetime import datetime
from tkinter import *
from tkinter import messagebox,simpledialog,Label
from PIL import Image,ImageTk

expfile='exp_file1.json'

def loadfile():
    if os.path.exists(expfile):
        with open(expfile,'r') as file:
            return json.load(file)
    return []

def save(expense_file):
    with open(expfile,'w') as file:
        json.dump(expense_file,file,indent=4)

def ins(name,cat,amt,date):
    file=loadfile()
    expense={
        'product': name,
        'amount': amt,
        'date': date.strftime('%Y-%m-%d'),
        'category': cat
    }
    file.append(expense)
    save(file)
    messagebox.showinfo("Success","Great! Your expense has been added successfully!")


def ins_gui():
    def submit():
        try:
            name=name_ins.get()
            cat=cat_ins.get()
            amt=float(prc_ins.get())
            date_str=dt_ins.get()
            date=datetime.strptime(date_str,'%Y-%m-%d')
            ins(name,cat,amt,date)
            name_ins.delete(0,END)
            cat_ins.delete(0,END)
            prc_ins.delete(0,END)
            dt_ins.delete(0,END)
        except ValueError:
            messagebox.showerror("Error","Enter a valid amount and date (YYYY-MM-DD).")
   
    root_ins=Tk()
    root_ins.title("Expense Tracker")
    root_ins.configure(bg='light slate gray')
    root_ins.geometry("500x600")
    root_ins.wm_iconbitmap('calculator-icon_34473 (1).ico')
    root_ins.maxsize(500,600)

    Label(root_ins,text="Enter Product Name",font=('Arial',12)).grid(row=0,column=0,padx=10,pady=10,sticky="e")
    name_ins=Entry(root_ins,font=('Arial',12))
    name_ins.grid(row=0,column=1,padx=10,pady=10)
    Label(root_ins,text="Enter Category",font=('Arial',12)).grid(row=1,column=0,padx=10,pady=10,sticky="e")
    cat_ins=Entry(root_ins,font=('Arial',12))
    cat_ins.grid(row=1,column=1,padx=10,pady=10)
    Label(root_ins,text="Enter Amount",font=('Arial',12)).grid(row=2,column=0,padx=10,pady=10,sticky="e")
    prc_ins=Entry(root_ins,font=('Arial',12))
    prc_ins.grid(row=2,column=1,padx=10,pady=10)
    Label(root_ins,text="Enter Date(YYYY-MM-DD)",font=('Arial',12)).grid(row=3,column=0,padx=10,pady=10,sticky="e")
    dt_ins=Entry(root_ins,font=('Arial',12))
    dt_ins.grid(row=3,column=1,padx=10,pady=10)

    add_expense_button=Button(root_ins,text="Add Expense",command=submit,width=20,height=2,borderwidth=5,relief="ridge",fg="black",bg="LightGray",activeforeground="black",activebackground="DarkGray",font=('Helvetica',10,'bold'))
    add_expense_button.grid(row=4,column=0,columnspan=2,pady=20)


def list_expenses():
    exp_file1=loadfile()  # Assuming this function loads your expenses

    root=tk.Tk()
    root.withdraw()  # Hide the main window

    user_input=simpledialog.askstring("Input","Please enter category\n(type all if all):")
    
    if user_input is None:
        return  # User canceled the dialog

    if user_input.lower() != "all":
        matches=[item for item in exp_file1 if item.get('category','').lower() == user_input.lower()]
        
        if not matches:
            messagebox.showerror("Error","This category does not exist")
        else:
            rootl=tk.Tk()
            rootl.title("LIST")
            
            rootl.geometry("500x600")  # Set the initial window size
            rootl.wm_iconbitmap('calculator-icon_34473 (1).ico')
            rootl.maxsize(500,600)    # Set the maximum window size

            label1=tk.Label(rootl,text="EXPENSES",font=('Helvetica',14,'bold italic'),padx=20,pady=10,foreground='olive',borderwidth=5,relief="ridge")
            label1.grid(row=0,column=0,columnspan=3,padx=0,pady=20)
            tk.Label(rootl,text=f"Category: {user_input.upper()}",font=('Helvetica',12,'bold')).grid(row=1,column=0,columnspan=3,padx=10,pady=10)
            row_num=2
            tk.Label(rootl,text="NAME",font=('Helvetica',12,'bold'),foreground="DarkGray").grid(row=row_num,column=0,padx=10,pady=5,sticky="w")
            tk.Label(rootl,text="AMOUNT",font=('Helvetica',12,'bold'),foreground="DarkGray").grid(row=row_num,column=1,padx=10,pady=5,sticky="w")
            tk.Label(rootl,text="DATE",font=('Helvetica',12,'bold'),foreground="DarkGray").grid(row=row_num,column=2,padx=10,pady=5,sticky="w")

            for expense in matches:
                row_num += 1
                tk.Label(rootl,text=expense['product'],font=('Helvetica',12)).grid(row=row_num,column=0,padx=10,pady=5,sticky="w")
                tk.Label(rootl,text=str(expense['amount']),font=('Helvetica',12)).grid(row=row_num,column=1,padx=10,pady=5,sticky="w")
                tk.Label(rootl,text=expense['date'],font=('Helvetica',12)).grid(row=row_num,column=2,padx=10,pady=5,sticky="w")

            total=sum(exp['amount'] for exp in matches)
            row_num += 1
            tk.Label(rootl,text=f"Total expenditure for this category: {total}",font=('Helvetica',12,'bold')).grid(row=row_num,column=0,columnspan=3,padx=10,pady=10)

            rootl.mainloop()
    elif user_input.lower() == "all":
        rootl=tk.Tk()
        rootl.title("LIST")
        rootl.configure(bg='light slate gray')
        rootl.geometry("500x600")  # Set the initial window size
        rootl.maxsize(500,600)
        rootl.wm_iconbitmap('calculator-icon_34473 (1).ico')
        canvas=tk.Canvas(rootl)
        frame=tk.Frame(canvas)
        scrollbar=tk.Scrollbar(rootl,orient=tk.VERTICAL,command=canvas.yview)
        canvas.configure(yscrollcommand=scrollbar.set)

        scrollbar.pack(side=tk.RIGHT,fill=tk.Y)
        canvas.pack(side=tk.LEFT,fill=tk.BOTH,expand=True)
        canvas.create_window((0,0),window=frame,anchor='nw')

        frame.bind("<Configure>",lambda event,canvas=canvas: on_frame_configure(canvas))

        label1=tk.Label(frame,text="ALL EXPENSES!",font=('Helvetica',14,'bold italic'),padx=30,pady=10,foreground='olive',borderwidth=5,relief="ridge")
        label1.grid(row=0,column=0,columnspan=3,padx=0,pady=20)

        row_num=1
        cat_dict={}
        for exp in exp_file1:
            if exp['category'] not in cat_dict:
                cat_dict[exp['category']]=[]
            cat_dict[exp['category']].append(exp)

        for cat in sorted(cat_dict.keys()):
            tk.Label(frame,text=f"Category: {cat.upper()}",font=('Helvetica',12,'bold')).grid(row=row_num,column=0,columnspan=3,padx=10,pady=10)
            row_num += 1
            
            tk.Label(frame,text="NAME",font=('Helvetica',12,'bold')).grid(row=row_num,column=0,padx=10,pady=5,sticky="w")
            tk.Label(frame,text="AMOUNT",font=('Helvetica',12,'bold')).grid(row=row_num,column=1,padx=10,pady=5,sticky="w")
            tk.Label(frame,text="DATE",font=('Helvetica',12,'bold')).grid(row=row_num,column=2,padx=10,pady=5,sticky="w")
            row_num += 1

            for expense in cat_dict[cat]:
                tk.Label(frame,text=expense['product'],font=('Helvetica',12)).grid(row=row_num,column=0,padx=10,pady=5,sticky="w")
                tk.Label(frame,text=str(expense['amount']),font=('Helvetica',12)).grid(row=row_num,column=1,padx=10,pady=5,sticky="w")
                tk.Label(frame,text=expense['date'],font=('Helvetica',12)).grid(row=row_num,column=2,padx=10,pady=5,sticky="w")
                row_num += 1

            total=sum(exp['amount'] for exp in cat_dict[cat])
            tk.Label(frame,text=f"Total expenditure for this category: {total}",font=('Helvetica',12,'bold')).grid(row=row_num,column=0,columnspan=3,padx=10,pady=10)
            row_num += 1

        rootl.mainloop()

def on_frame_configure(canvas):
    canvas.configure(scrollregion=canvas.bbox("all"))
import tkinter as tk




def generate_report():
    def submit():
        mnr=month.get()
        yr=year.get()

        # Validate month and year input
        if not (mnr.isdigit() and yr.isdigit()):
            messagebox.showerror("Error","Month and Year should be numeric values.")
            return

        mnr=int(mnr)
        yr=int(yr)

        if not (1 <= mnr <= 12):
            messagebox.showerror("Error","Month should be between 1 and 12.")
            return

        exp_file1=loadfile()  # Ensure this function returns a list of expense dictionaries
        m_exp=[]

        for exp in exp_file1:
            try:
                # Ensure the date format is YYYY-MM-DD
                if exp['date'].startswith(f"{yr}-{mnr:02d}"):
                    m_exp.append(exp)
            except KeyError:
                continue

        if not m_exp:
            messagebox.showerror("Error","No record for this month")
        else:
            # Clear previous report data
            for widget in rep_wind.winfo_children():
                widget.destroy()

            label1=tk.Label(rep_wind,text=f"EXPENSES REPORT {mnr:02d}/{yr}",font=('Helvetica',14,'bold italic'),padx=20,pady=10,foreground='olive',borderwidth=5,relief="ridge")
            label1.grid(row=0,column=0,columnspan=3,padx=0,pady=20)

            row_num=1
            tk.Label(rep_wind,text="NAME",font=('Helvetica',12,'bold'),foreground="DarkGray").grid(row=row_num,column=0,padx=10,pady=5,sticky="w")
            tk.Label(rep_wind,text="AMOUNT",font=('Helvetica',12,'bold'),foreground="DarkGray").grid(row=row_num,column=1,padx=10,pady=5,sticky="w")
            tk.Label(rep_wind,text="DATE",font=('Helvetica',12,'bold'),foreground="DarkGray").grid(row=row_num,column=2,padx=10,pady=5,sticky="w")

            for expense in m_exp:
                print(f"Displaying expense: {expense}")  # Debugging line
                row_num += 1
                tk.Label(rep_wind,text=expense.get('product','N/A'),font=('Helvetica',12)).grid(row=row_num,column=0,padx=10,pady=5,sticky="w")
                tk.Label(rep_wind,text=str(expense.get('amount','N/A')),font=('Helvetica',12)).grid(row=row_num,column=1,padx=10,pady=5,sticky="w")
                tk.Label(rep_wind,text=expense.get('date','N/A'),font=('Helvetica',12)).grid(row=row_num,column=2,padx=10,pady=5,sticky="w")

            total=sum(exp.get('amount',0) for exp in m_exp)
            row_num += 1
            tk.Label(rep_wind,text=f"Total expenditure for this month: {total}",font=('Helvetica',12,'bold')).grid(row=row_num,column=0,columnspan=3,padx=10,pady=10)

            rep_wind.mainloop()

        month.delete(0,tk.END)
        year.delete(0,tk.END)

    rep_wind=tk.Tk()
    rep_wind.title("Expense Report")
    rep_wind.geometry("500x600")
    rep_wind.maxsize(500,600)
    rep_wind.wm_iconbitmap('calculator-icon_34473 (1).ico')
    font_settings=('Arial',12)

    tk.Label(rep_wind,text="Month",font=font_settings).grid(row=0,column=0,padx=10,pady=10,sticky="e")
    month=tk.Entry(rep_wind,font=font_settings)
    month.grid(row=0,column=1,padx=10,pady=10)

    tk.Label(rep_wind,text="YEAR",font=font_settings).grid(row=1,column=0,padx=10,pady=10,sticky="e")
    year=tk.Entry(rep_wind,font=font_settings)
    year.grid(row=1,column=1,padx=10,pady=10)

    tk.Button(rep_wind,text="Submit",command=submit,width=20,height=2,borderwidth=5,relief="ridge",foreground="black",background="LightGray",activeforeground="black",activebackground="DarkGray",font=('Helvetica',10,'bold')).grid(row=4,column=0,columnspan=2,pady=20)


def search_expense():
    exp_file1=loadfile() 
    key= simpledialog.askstring("Input","Enter the product to seacrh:")
    matches=[item for item in exp_file1 if item.get('product').lower() == key.lower()]
    
    if not matches:
        messagebox.showerror("Error","This product does not exist")
    else:
        rootl=Tk()
        rootl.title("LIST")
        rootl.configure(bg='light slate gray')
        



        rootl.geometry("700x600")  # Set the initial window size
        rootl.maxsize(700,600)    # Set the maximum window size
        rootl.wm_iconbitmap('calculator-icon_34473 (1).ico')
        # Create a Canvas widget
        canvas=Canvas(rootl,width=500,height=600)
        canvas.pack(fill=BOTH,expand=True)

       
        canvas.create_text(220,30,text="RECORD OF YOUR SEARCHED PRODUCT",font=('Helvetica',12,'bold'),fill="olive")
        # Add labels and expense information on top of the background
        
        canvas.create_text(90,70,text="NAME",font=('Helvetica',12,'bold'),fill="black")
        canvas.create_text(260,70,text="AMOUNT",font=('Helvetica',12,'bold'),fill="black")
        canvas.create_text(450,70,text="DATE",font=('Helvetica',12,'bold'),fill="black")

        y_position=120
        for expense in matches:
            canvas.create_text(70,y_position,text=expense['product'],font=('Helvetica',12),fill="black",anchor="w")
            canvas.create_text(250,y_position,text=str(expense['amount']),font=('Helvetica',12),fill="black",anchor="w")
            canvas.create_text(430,y_position,text=expense['date'],font=('Helvetica',12),fill="black",anchor="w")
            y_position += 40

        total=sum(exp['amount'] for exp in matches)
        canvas.create_text(250,y_position,text=f"Total expenditure for this product: {total}",font=('Helvetica',12,'bold'),fill="black",anchor="center")

        rootl.mainloop()

root=Tk()
root.title("Expense Tracker")
root.geometry("1000x600")  # Set the initial window size
root.maxsize(1000,600)    # Set the maximum window size
root.wm_iconbitmap('calculator-icon_34473 (1).ico')
# Load the background image
bg_image=Image.open("bg.jpeg")  # Replace with your image file
bg_photo=ImageTk.PhotoImage(bg_image)

# Create a label to hold the background image
bg_label=tk.Label(root,image=bg_photo)
bg_label.place(x=0,y=0,relwidth=1,relheight=1)

# Example widget on top of the background
label=tk.Label(
    root,
    text="Monthly Expense Tracker!",
    font=('Helvetica',24,'bold italic'),
    fg="olive",
    bg="Lightgrey",
    padx=20,
    pady=10,borderwidth=5,
    relief="ridge"
)
label.grid(row=0,column=0,columnspan=6,padx=0,pady=20)

# Configure the grid
root.grid_rowconfigure(0,weight=1)
root.grid_rowconfigure(1,weight=1)
root.grid_columnconfigure(0,weight=1)
root.grid_columnconfigure(1,weight=1)
root.grid_columnconfigure(2,weight=1)
root.grid_columnconfigure(3,weight=1)
root.grid_columnconfigure(4,weight=1)
root.grid_columnconfigure(5,weight=1)

btn_add=tk.Button(root,text="Add Expense",command=ins_gui,width=30,height=3,borderwidth=5,fg="black",bg="LightGray",relief="ridge",activeforeground="black",activebackground="DarkGray",font=('Helvetica',10,'bold'))
btn_add.grid(row=1,column=3,padx=150,pady=60,sticky="ne")

btn_list=tk.Button(root,text="List Expenses",command=list_expenses,width=30,height=3,borderwidth=5,relief="ridge",fg="black",bg="LightGray",activeforeground="black",activebackground="DarkGray",font=('Helvetica',10,'bold'))
btn_list.grid(row=1,column=4,padx=100,pady=60,sticky="nw")

btn_search=tk.Button(root,text="Search Expense",command=search_expense,width=30,height=3,borderwidth=5,relief="ridge",fg="black",bg="LightGray",activeforeground="black",activebackground="DarkGray",font=('Helvetica',10,'bold'))
btn_search.grid(row=2,column=4,padx=100,pady=50,sticky="sw")

btn_report=tk.Button(root,text="Generate Report",command=generate_report,width=30,height=3,borderwidth=5,relief="ridge",fg="black",bg="LightGray",activeforeground="black",activebackground="DarkGray",font=('Helvetica',10,'bold'))
btn_report.grid(row=2,column=3,padx=150,pady=50,sticky="se")

btn_exit=tk.Button(root,text="Exit",command=root.quit,width=20,height=2,borderwidth=5,relief="ridge",fg="black",bg="LightGray",activeforeground="black",activebackground="DarkGray",font=('Helvetica',10,'bold'))
btn_exit.grid(row=3,column=3,columnspan=2,pady=50)

root.mainloop()
