from tkinter import *
from tkinter import ttk, filedialog, messagebox
# filedialog is gave us a pop up window through which we select the folder like in some app

import os, shutil
# shutil ---> folder jo files he unko move krne me help krega

class FileSorting:
    def __init__(self, root):
        self.root= root
        self.root.title('File Sorting App | Developed By Ram | Alpha')
        self.root.geometry('1350x700+80+40')
        self.root.maxsize(1350,700)
        self.root.minsize(1350,700)
        self.root.config(bg='white')

        self.logo_icon= PhotoImage(file='fileHead.png')
        Label(self.root, text='File Sorting Application', image=self.logo_icon, compound=LEFT, font=('impact', 40, 'bold'), padx=40, bg='#023548', fg='white', anchor=W).place(x=0 ,y=0, relwidth=1)
        
        # Section-1 Selecting folder -->
        self.var_foldername= StringVar()
        Label(self.root, text='Select Folder', font=('times new roman',25,'bold'), bg='white').place(x=50, y=100)
        Entry(self.root, textvariable=self.var_foldername ,font=('times new roman', 15, 'bold'), bg='lightyellow').place(x=270, y=100, height=38, width=500)
        Button(self.root, text='Browse', command=self.BrowseFunction, font=('times new roman',18,'bold'), bg='#262626', fg='lightyellow', activebackground='#262626', activeforeground='red', cursor='hand2').place(x=800, y=98, height=40, width=155)
        Label(self.root, bg='lightgrey').place(x=50, y=160, height=2, width=1250)  # Drawing horizontal line after taking input
        # Section-1 Selecting folder -->


        # Section-2 (Adding Extension)
        # All Extensions
        self.image_extension= ['Image Extensions', '.png', '.jpg']
        self.audio_extension= ['Audio Extensions', '.amr', '.mp3']
        self.video_extension= ['Video Extensions', '.mp4', '.avi', 'mpeg4', '3gp', '.mkv', '.wmv']
        self.doc_extension= ['Docs Extensions', '.doc', '.txt', '.xlsx', '.ppt', '.pptx', '.xls', '.pdf', '.zip', '.rar', '.csv', '.docx']

        self.folders = {
            'videos': self.video_extension,
            'audios': self.audio_extension,
            'images': self.image_extension,
            'documents': self.doc_extension
        }

        Label(self.root, text='Various Extension Supports', font=('times new roman',25,'bold'), bg='white').place(x=50, y=175)
        self.image_box= ttk.Combobox(self.root, font=('times new roman', 15, 'bold'), state='readonly', justify=CENTER, values=self.image_extension)
        self.image_box.place(x=60, y=240)
        self.image_box.current(0)

        self.audio_box= ttk.Combobox(self.root, font=('times new roman', 15, 'bold'), state='readonly', justify=CENTER, values=self.audio_extension)
        self.audio_box.place(x=410, y=240)
        self.audio_box.current(0)

        self.video_box= ttk.Combobox(self.root, font=('times new roman', 15, 'bold'), state='readonly', justify=CENTER, values=self.video_extension)
        self.video_box.place(x=750, y=240)
        self.video_box.current(0)

        self.doc_box= ttk.Combobox(self.root, font=('times new roman', 15, 'bold'), state='readonly', justify=CENTER, values=self.doc_extension)
        self.doc_box.place(x=1070, y=240)
        self.doc_box.current(0)
        # Section-2 (Adding Extension)

        # Section-3 Icons
        # All Icons
        self.image_icon= PhotoImage(file='photo.png')
        self.audio_icon= PhotoImage(file='headphone.png')
        self.video_icon= PhotoImage(file='video.png')
        self.document_icon= PhotoImage(file='docs.png')
        self.other_icon= PhotoImage(file='others.png')

        frame1= Frame(self.root, bd=2, relief=RIDGE, bg='lightblue')
        frame1.place(x=50, y=295, width=1250, height=290)
        self.lbl_total_files= Label(frame1, text='Total Files : ', font=('times new roman', 20), bg='lightblue')
        self.lbl_total_files.place(x=20, y=10)

        self.lbl_image_files= Label(frame1, bd=2, relief=RAISED, font=('times new roman', 20), bg='lightpink', image=self.image_icon, compound=TOP)
        self.lbl_image_files.place(x=20, y=70, height=200, width=210)

        self.lbl_audio_files= Label(frame1, bd=2, relief=RAISED, font=('times new roman', 20), bg='#038cfc', image=self.audio_icon, compound=TOP)
        self.lbl_audio_files.place(x=267, y=70, height=200, width=210)

        self.lbl_video_files= Label(frame1, bd=2, relief=RAISED, font=('times new roman', 20), bg='orange', image=self.video_icon, compound=TOP)
        self.lbl_video_files.place(x=521, y=70, height=200, width=210)

        self.lbl_document_files= Label(frame1, bd=2, relief=RAISED, font=('times new roman', 20), bg='#db6060', image=self.document_icon, compound=TOP)
        self.lbl_document_files.place(x=770, y=70, height=200, width=210)

        self.lbl_other_files= Label(frame1, bd=2, relief=RAISED, font=('times new roman', 20), bg='#e63939', image=self.other_icon, compound=TOP)
        self.lbl_other_files.place(x=1015, y=70, height=200, width=210)
        # Section-3 Icons

        # Section-4 status bar
        Label(self.root, text='STATUS', font=('times new roman', 22, 'bold'), bg='white').place(x=50, y=620)
        self.status_total= Label(self.root, text='', font=('times new roman', 22, 'bold'), bg='white', fg='orange')
        self.status_total.place(x=210, y=620)

        self.status_moved= Label(self.root, text='', font=('times new roman', 22, 'bold'), bg='white', fg='blue')
        self.status_moved.place(x=420, y=620)

        self.status_left= Label(self.root, text='', font=('times new roman', 22, 'bold'), bg='white', fg='green')
        self.status_left.place(x=650, y=620)

        # Buttons (clear and start)
        self.clearBtn= Button(self.root, command=self.clearBtn, text='Clear', font=('times new roman',18,'bold'), bg='#607d8b', fg='lightyellow', activebackground='#607d8b', activeforeground='orange', cursor='hand2')
        self.clearBtn.place(x=910, y=620, height=40, width=155)

        self.startBtn= Button(self.root, text='Start', state=DISABLED, command= self.start_button_function, font=('times new roman',18,'bold'), bg='#ff5722', fg='lightyellow', activebackground='#ff5722', activeforeground='blue', cursor='hand2')
        self.startBtn.place(x=1100, y=620, height=40, width=155)
        # Section-4 status bar


    # Making some functions

    def total_count(self):
        images=0
        videos=0
        audios=0
        doc=0
        others=0
        self.count=0
        combine_list=[]
        for fileName in self. allFiles:
            if os.path.isfile(os.path.join(self.directory, fileName)) == True:
                self.count+=1
                extension = "." + fileName.split('.')[-1]
                for folderName in self. folders.items():
                    # print(folderName)

                    for x in folderName[1]:
                        combine_list.append(x)

                    if extension.lower() in folderName[1] and folderName[0] == 'images':
                        images+=1
                    if extension.lower() in folderName[1] and folderName[0] == 'audios':
                        audios+=1
                    if extension.lower() in folderName[1] and folderName[0] == 'videos':
                        videos+=1
                    if extension.lower() in folderName[1] and folderName[0] == 'documents':
                        doc+=1

        # Calculating other files
        for fileName in self. allFiles:
            if os.path.isfile(os.path.join(self.directory, fileName)) == True:
                extension = "." + fileName.split('.')[-1]
                if extension.lower() not in combine_list:
                    others+=1
     
        self.lbl_image_files.config(text=f'Total Images\n{str(images)}')
        self.lbl_video_files.config(text=f'Total Videos\n{str(videos)}')
        self.lbl_audio_files.config(text=f'Total Audios\n{str(audios)}')
        self.lbl_document_files.config(text=f'Total Docs\n{str(doc)}')
        self.lbl_other_files.config(text=f'Total Others\n{str(others)}')

        self.lbl_total_files.config(text=f'Total Files : {str(self.count)}')

    def BrowseFunction(self):
        op= filedialog.askdirectory(title= 'SELECT FOLDER FOR SORTING')
        if op != None:
            # print(op)
            self.var_foldername.set(str(op))
            # ************************************
            self.directory= self.var_foldername.get()
            self.Other_name= 'Others'
            self.renameFolderNameIfSame()

            self. allFiles= os.listdir(self.directory)
            lenght= len(self.allFiles)
            self.total_count()
            self.startBtn.config(state=NORMAL)
            # print(allFiles)


    def clearBtn(self):
        '''This is function is for clear buuton to clear its var'''

        self.startBtn.config(state=DISABLED)
        self.var_foldername.set('')

        self.lbl_image_files.config(text='')
        self.lbl_video_files.config(text='')
        self.lbl_audio_files.config(text='')
        self.lbl_document_files.config(text='')
        self.lbl_other_files.config(text='')
        self.lbl_total_files.config(text='Total Files : ')

        self.status_total.config(text= '')
        self.status_moved.config(text= '')
        self.status_left.config(text= '')



    def start_button_function(self):
        if self.var_foldername.get() != "":
            self.clearBtn.config(state= DISABLED)
            c=0
            for fileName in self. allFiles:
                if os.path.isfile(os.path.join(self.directory, fileName)) == True:
                    c=c+1
                    print('yes')   
                    self.moveFiles(fileName.split('.')[-1], fileName)
                    self.status_total.config(text= f'TOTAL: {str(self.count)}')
                    self.status_moved.config(text= f'MOVED: {str(c)}')
                    self.status_left.config(text= f'LEFT: {str(self.count - c)}')

                    self.status_total.update()
                    self.status_moved.update()
                    self.status_left.update()                  
            messagebox.showinfo('Success', 'All Files are moved successfully !')
            self.startBtn.config(state= DISABLED)
            self.clearBtn.config(state= NORMAL)
        else:
            messagebox.showerror('Error', 'Please select the folder !')


    def renameFolderNameIfSame(self):
        for folder in os.listdir(self.directory):
            if os.path.isdir(os.path.join(self.directory, folder)) == True:
                os.rename(os.path.join(self.directory, folder), os.path.join(self.directory, folder.lower()))



    def moveFiles(self, ext, file_name):
        find=False
        for folderName in self. folders:
            if "." + ext in self. folders[folderName]:
                # print('found', folderName)
                if folderName not in os.listdir(self.directory):
                    os.mkdir(os.path.join(self.directory, folderName))
                # shutil.move(source, destination)
                shutil.move(os.path.join(self.directory, file_name), os.path.join(self.directory, folderName))
                find= True
                break
        # Moving Other extension files which are not found in folders    
        if find == False:
            if self.Other_name not in os.listdir(self.directory):
                os.mkdir(os.path.join(self.directory, self.Other_name))
            shutil.move(os.path.join(self.directory, file_name), os.path.join(self.directory, self.Other_name))     

    # Making some functions

# Creating object of FileSorting Class
root= Tk()
FileSortingObj= FileSorting(root)
root.mainloop()