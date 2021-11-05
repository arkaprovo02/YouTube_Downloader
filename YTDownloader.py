from tkinter import *
from tkinter import ttk
from tkinter import filedialog
from tkinter.font import BOLD
from pytube import YouTube #pip install pytube3
from tkinter import filedialog
Folder_Name = ""

#file location
def openLocation():
    download_name.config(text="")
    download_size.config(text="")
    global Folder_Name
    Folder_Name = filedialog.askdirectory()
    if(len(Folder_Name) > 1):
        locationError.config(text=Folder_Name,fg="green", font="bold")

    else:
        locationError.config(text="Please Choose Folder!!",fg="red")

#donwload video
def DownloadVideo():
    
    choice = ytdchoices.get()
    url = ytdEntry.get()
    try:
        if(len(url)<1):
            ytdError.config(text="Please insert valid url", fg="red",bg="white")
        else:
           
            try:
                yt = YouTube(url)

            

                if(choice == choices[0]):
                    select = yt.streams.filter(progressive=True).first()

                elif(choice == choices[1]):
                    select = yt.streams.filter(progressive=True,file_extension='mp4').last()

                elif(choice == choices[2]):
                    select = yt.streams.filter(only_audio=True).first()

                else:
                    ytdError.config(text="Paste Link again!!",fg="red")


                #download function
                try:
                    select.download(Folder_Name)
                    
                    nameVideo=select.title
                    size=select.filesize/1024000
                    ytdError.config(text="Download Completed!!")
                    download_name.config(text="The Video is  : "+nameVideo)
                    download_size.config(text="Size  of dowloaded video="+size)

                except:
                    ytdError.config("Invalid link! Please Enter a valid link", fg="red")

            except: 
                ytdError.config(text="PROCESS COMPLETED! CHECK THE FOLDER!!")

    except:
        ytdError.config("Error in url",fg="red")


root = Tk()
root.title("YT Downloader")
root.geometry("1000x650") #set window
root.config(bg="gray3")
root.columnconfigure(0,weight=0)#set all content in center.

#Heading
heading = Label(root,text="YOUTUBE Video Downloader",bg="gray3",fg="yellow", font=("Bohnshrift semibold",25,"bold"))
heading.pack(anchor="center", pady=10)


#Ytd Link Label
ytdLabel = Label(root,text="Enter the URL of the Video",bg="gray3",fg="dark orange", font=("sans",15,"bold"))
ytdLabel.pack(anchor="w",padx=10,pady=10)

#Entry Box
ytdEntryVar = StringVar()
ytdEntry = Entry(root,width=55,textvariable=ytdEntryVar)
ytdEntry.place(x=300,y=80)

#Error Msg
ytdError = Label(root,text="Please Enter a valid YouTube URL!",bg="gray3",fg="red", font=("Bohnshrift semibold",10))
ytdError.place(x=650,y=80)

#Asking save file label
saveLabel = Label(root,text="Save the Video File",bg="gray3",fg="dark orange",font=("jost",15,"bold"))
saveLabel.pack(anchor="w",padx=10,pady=55)

#btn of save file
saveEntry = Button(root,width=25,bg="blue",fg="white",text="Choose Download Location",font=("jost",10,"bold"),command=openLocation)
saveEntry.place(x=350, y=155)

#Error Msg location
locationError = Label(root,text="Please select valid Path!",bg="gray3",fg="red",font=("jost",10))
locationError.place(x=600,y=155)

#Download Quality
ytdQuality = Label(root,text="Select Quality",bg="gray3",fg="dark orange",font=("jost",15,"bold"))
ytdQuality.pack(anchor="w",padx=10,pady=15)

#combobox
choices = ["720p","144p","Only Audio"]
ytdchoices = ttk.Combobox(root,values=choices,width=25)
ytdchoices.place(x=370,y=280)

#Error Msg quality
qualityError = Label(root,text="Please select valid Quality!",bg="gray3",fg="red",font=("jost",10))
qualityError.place(x=600,y=285)

#donwload btn
downloadbtn = Button(root,text="Download Video",width=20,bg="green",fg="white",font=("jost",15,"bold"),command=DownloadVideo)
downloadbtn.place(x=330,y=400)

#Title of video
download_name = Label(root,text="FILL UP THE DETAILS!",bg="gray3",fg="dark orange",font=("sans",15))
download_name.place(y=500,anchor="nw")

#Size of video
download_size = Label(root,text="And wait Patiently :)",bg="gray3",fg="dark orange",font=("sans",12))
download_size.place(x=400,y=550,anchor="nw")

#developer Label
developerlabel = Label(root,text="Developed by Arkaprovo",bg="gray3",fg="white",font=("sans",10))
developerlabel.place(x=400,y=600)
root.mainloop()