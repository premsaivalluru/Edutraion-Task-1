import tkinter as tk
from tkinter import messagebox
incomplete_tasks=[]
complete_tasks=[]

def refresh_listbox():
    to_do_listbox.delete(0,tk.END)
    for index, task in enumerate(incomplete_tasks):
        to_do_listbox.insert(tk.END,f"{index}) {task}")

def add_task():
    task = task_entry.get()
    if not task.strip():
        messagebox.showwarning("Warning","Enter the task!!!")
        return
    incomplete_tasks.append(task)

    refresh_listbox()
    task_entry.delete(0,tk.END)

def update_task():
    try:
        task_index = to_do_listbox.curselection()[0]
        task = incomplete_tasks[task_index]
        task_label.config(text="Update Task:")
        task_entry.delete(0,tk.END)
        task_entry.insert(0,task)
        def update():
            new_task = task_entry.get()
            if not new_task.strip():
                messagebox.showwarning("Warning","Enter the task!!!")
                return
            incomplete_tasks[task_index] = new_task
            to_do_listbox.delete(task_index)
            task_entry.delete(0,tk.END)
            messagebox.showinfo("Success","Task updated successfully!!!")
            refresh_listbox()
            task_label.config(text="Enter task:")
            add_button.config(text="Add Task", command=add_task)
            return
        add_button.config(text="Submit",command=update)
        return
    except:
        messagebox.showwarning("Warning","Select a task to update!!!")
        
def delete_task():
    try:
        task_index = to_do_listbox.curselection()[0]
        del incomplete_tasks[task_index]
        to_do_listbox.delete(task_index)
        messagebox.showinfo("Success","Task deleted successfully!!!")
        refresh_listbox()
        return
    except:
        messagebox.showwarning("Warning","Select a task to delete!!!")

def mark_done():
    try:
        task_index = to_do_listbox.curselection()[0]
        task = incomplete_tasks[task_index]
        to_do_listbox.delete(task_index)
        del incomplete_tasks[task_index]
        complete_tasks.append(task)
        done_listbox.insert(tk.END,f"{task}")
        messagebox.showinfo("Success","Task marked as done successfully!!!")
        refresh_listbox()
    except:
        messagebox.showwarning("Warning","Select a task to mark as done!!!")

root=tk.Tk()
root.title("To-Do List")
root.geometry("500x650")
root.config(bg="black")

title_label = tk.Label(root,text="To-Do List",font=("Times New Roman",20,"bold"),fg="orange",bg="black")
title_label.grid(row=0,column=0,columnspan=3,padx=10,pady=10)

task_frame = tk.Frame(root,width=500,bg="black")
task_frame.grid(row=1,column=0,columnspan=3,padx=10,pady=10,sticky="w")

task_label = tk.Label(task_frame,text="Enter task:",fg="white",bg="black",font=(11))
task_label.pack(side=tk.LEFT,padx=10)

task_entry = tk.Entry(task_frame,width=40)
task_entry.pack(side=tk.LEFT,padx=10,fill=tk.X)

add_button = tk.Button(task_frame,text="Add Task",bg="yellow",command=add_task,width=10)
add_button.pack(side=tk.LEFT,padx=10)

button_frame = tk.Frame(root,bg="black",width=500)
button_frame.grid(row=2,column=0,columnspan=3,padx=10,pady=10,sticky="ew")

update_button = tk.Button(button_frame,text="Update Task",bg="yellow",command=update_task)
update_button.pack(side=tk.LEFT,padx=10,expand=True,fill=tk.X)

delete_button = tk.Button(button_frame,text="Delete Task",bg="yellow",command=delete_task)
delete_button.pack(side=tk.LEFT,padx=10,expand=True,fill=tk.X)

done_button = tk.Button(button_frame,text="Mark As Done",bg="yellow",command=mark_done)
done_button.pack(side=tk.LEFT,padx=10,expand=True,fill=tk.X)

label1=tk.Label(root,text="Incomplete Tasks:",font=(12),fg="white",bg="black")
label1.grid(row=3,column=0,padx=10,pady=5,sticky="w")

to_do_frame = tk.Frame(root,bg="black",width=500)
to_do_frame.grid(row=4,column=0,columnspan=3,padx=10,pady=5,sticky="w")

to_do_listbox = tk.Listbox(to_do_frame,width=75)
to_do_listbox.pack(side=tk.LEFT,fill=tk.BOTH)

to_do_scroll_bar = tk.Scrollbar(to_do_frame,command=to_do_listbox.yview)
to_do_scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
to_do_listbox.config(yscrollcommand=to_do_scroll_bar.set)

label2 = tk.Label(root,text="Completed Tasks:",font=(11),fg="white",bg="black")
label2.grid(row=5,column=0,sticky="w",padx=10,pady=5)

done_frame = tk.Frame(root,bg="black",width=500)
done_frame.grid(row=6,column=0,columnspan=3,padx=10,pady=5,sticky="w")

done_listbox = tk.Listbox(done_frame,width=75)
done_listbox.pack(side=tk.LEFT,fill=tk.BOTH)

done_scroll_bar = tk.Scrollbar(done_frame,command=done_listbox.yview)
done_scroll_bar.pack(side=tk.RIGHT,fill=tk.Y)
done_listbox.config(yscrollcommand=done_scroll_bar.set)

exit_button = tk.Button(root,text="Exit",bg="yellow",command=root.destroy,width=65)
exit_button.grid(row=7,column=0,columnspan=3,padx=12,pady=10,sticky="w")

root.mainloop()