# Importing required modules of Python for YouTube Video Downloader project
from tkinter import *
from tkinter import messagebox as mb
from pytube import YouTube


# Defining the downloader function
def downloader(link, directory, filename):
    link = link.get()
    save_path = directory.get()
    save_filename = filename.get()

    try:
        yt = YouTube(link)
        video = yt.streams.first()
        video.download(save_path, save_filename)
    except:
        mb.showerror('Error', 'Something went wrong!')


def reset(l_var, d_var, fn_var):
    l_var.set('')
    d_var.set('')
    fn_var.set('')


# Initializing the window
root = Tk()
root.title('Youtube Video Downloader')
root.geometry('900x400')
root.resizable(0, 0)
root.config(bg='gray')

# Heading label
Label(root, text='Youtube Video Downloader', font=("Comic Sans MS", 25), bg='gray').place(relx=0.25,
                                                                                          rely=0.0)

# Creating the main window
Label(root, text='Youtube link:', font=("Comic Sans MS", 20), bg='gray').place(relx=0.05, rely=0.2)

link_var = StringVar(root)
link_entry = Entry(root, width=60, textvariable=link_var)
link_entry.place(relx=0.5, rely=0.2)

Label(root, text='Save location:', font=("Comic Sans MS", 20), bg='gray').place(relx=0.05, rely=0.4)

dir_var = StringVar(root)
dir_entry = Entry(root, width=60, textvariable=dir_var)
dir_entry.place(relx=0.5, rely=0.4)

Label(root, text='Filename (Add extension):', font=("Comic Sans MS", 20), bg='gray').place(relx=0.05, rely=0.6)

filename_var = StringVar(root)
filename_entry = Entry(root, width=60, textvariable=filename_var)
filename_entry.place(relx=0.5, rely=0.6)

# Creating the buttons
download_btn = Button(root, text='Download', font=7, bg='#007fff',
                      command=lambda: downloader(link_entry, dir_entry, filename_entry)).place(relx=0.3, rely=0.75)

reset_btn = Button(root, text='Reset', font=7, bg='#007fff',
                   command=lambda: reset(link_var, dir_var, filename_var)).place(relx=0.5, rely=0.75)

# Finalizing the window
root.update()
root.mainloop()
