import os
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
import cv2
from PIL import Image,ImageTk
import pymysql.cursors
from datetime import datetime

connection = pymysql.connect(host='localhost',
                             user='root',
                             password='',
                             db='ndkm_tktt',
                             cursorclass=pymysql.cursors.DictCursor)
print("connect successful!!")
class Example(Frame):
    def __init__(self, parent):
        Frame.__init__(self, parent)
        self.parent = parent
        self.bind("<Control-l>", lambda x: self.hide())
        self.initUI()
    def initUI(self):
        self.parent.title("Tìm kiếm thông tin")
        self.top_frame = Frame(self, bg='#99FFCC', height=100, pady=10, relief=RAISED, borderwidth=1)
        self.pack(fill=BOTH, expand=1)
        self.center = Frame(self, height=600, padx=3, pady=10, relief=RAISED, borderwidth=1)
        self.pack(fill=BOTH, expand=1)
        self.btm_frame2 = Frame(self, bg='lavender', height=100, pady=10, relief=RAISED, borderwidth=1)
        self.pack(fill=BOTH, expand=1)
        self.grid_rowconfigure(1, weight=1)
        self.grid_columnconfigure(0, weight=1)

        self.top_frame.grid(row=0, sticky="ew")
        self.center.grid(row=1, sticky="nsew")
        self.btm_frame2.grid(row=2, sticky="ew")

        clearButton = Button(self.btm_frame2, text="   Clear   ", font='Times 17', bg="#808000", command=self.clearInformation)
        clearButton.pack(side=RIGHT, padx=5, pady=5)
        closeButton = Button(self.btm_frame2, text="   Close   ",font='Times 17',bg="#880000", command=self.closeInformation)
        closeButton.pack(side=RIGHT, padx=5, pady=5)
        okButton = Button(self.btm_frame2, text="   Save   ",font='Times 17',bg="#008080",command=self.saveInformation)
        okButton.pack(side=RIGHT)
        width_label = Label(self.top_frame, text='     Name: ',font='Times 17',bg="#99FFCC")
        gioitinh = Label(self.top_frame, text="        Gender: ",font='Times 17',bg="#99FFCC")
        ngaysinh = Label(self.top_frame, text="        Date of birth: ",font='Times 17',bg="#99FFCC")

        pic = ImageTk.PhotoImage(Image.open("file1.png"))
        file1_bt = Button(self.top_frame, text='  Choose Image  ', image=pic, compound=LEFT, bg='yellow', fg='red', command=self.browseFile,font='Times 15')
        file1_bt.image = pic
        file1_bt.place(x=0,y=0)

        self.textName = Entry(self.top_frame,font='Times 17')
        self.textGioiTinh = Entry(self.top_frame,font='Times 17')
        self.textNgaySinh = Entry(self.top_frame,font='Times 17')

        width_label.grid(row=1, column=0)
        gioitinh.grid(row=1, column=2)
        file1_bt.grid(row=1, column=15,padx=30)
        self.textName.grid(row=1, column=1)
        self.textGioiTinh.grid(row=1, column=4)
        ngaysinh.grid(row=1, column=6)
        self.textNgaySinh.grid(row=1, column=8)
        self.center.grid_rowconfigure(0, weight=1)
        self.center.grid_columnconfigure(1, weight=1)

    def browseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype = (("JPG File", "*.jpg"), ("JPEG File", "*.jpeg"), ("PNG File", "*.png"), ("All Files", "*.*")))
        print("NAME FILE: ", self.filename)
        self.img = Image.open(self.filename)
        pic = ImageTk.PhotoImage(Image.open(self.filename))
        self.center.anh_hien_lb = Label(self.center, image=pic)
        self.center.anh_hien_lb.image = pic
        w, h = self.img.size
        scrW = self.center.winfo_screenwidth() # lấy chiều rộng khung ảnh
        self.center.anh_hien_lb.place(x=(scrW//2)-(w//2), y=0, width=w, height=h)

    def saveInformation(self):
        imgs = cv2.imread(self.filename)
        arrFileName = self.filename.split("/")
        name=arrFileName[len(arrFileName) - 1]
        arrName = name.split(".",1)
        file=arrName[len(arrName)-1]
        dt_string = (datetime.now()).strftime("%Y/%m/%d %H:%M:%S") #lấy ngày và giờ hiện tại
        self.nameImage = str(self.textName.get()).replace(" ","_")+"_"+(dt_string.replace("/","_")).replace(" ","_").replace(":","_")+"."+file
        print("Đây là fileNameName mới: "+ self.nameImage)
        try:
            with connection.cursor() as cursor:
                # SQL
                print("self.textName.get(): ", self.textName.get())
                print("self.textGioiTinh.get(): ", self.textGioiTinh.get())
                print("self.nameImage: ", self.nameImage)
                sql = "INSERT INTO information(name,gender,image,date_of_birth) VALUE("+ "'"+self.textName.get()+ "'"+","+"'"+self.textGioiTinh.get()+ "'"+","+"'"+self.nameImage+ "'"+","+"'"+self.textNgaySinh.get()+"'"+")"

                print("sql: ", sql)
                # Thực thi câu lệnh truy vấn (Execute Query).
                number_of_rows = cursor.execute(sql)
                print("AAAAAAAAAAAAAA: ", number_of_rows)
                #connection.close()
        except pymysql.Error as e:
            print("ERROR: ", e)
        #finally:
            # Đóng kết nối (Close connection).
            #connection.close()
        path = "know/"+str(self.textName.get().strip()).replace(" ","")
        if not os.path.exists(path):
            os.mkdir(path)
        cv2.imwrite(path + "/" + self.nameImage, imgs)
        messagebox.askquestion("Thông báo", "Bạn đã thêm thành công")
    def closeInformation(self):
        sys.exit()
    def clearInformation(self):
        self.initUI()
        print("Xóa thành công")
root = Tk()
scrollbar = Scrollbar(root)
root.geometry("1000x1000+600+100")
app = Example(root)
root.mainloop()
