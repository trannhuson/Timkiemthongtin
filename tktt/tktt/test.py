import face_recognition
import os
import cv2
from collections import Counter
import tkinter
from tkinter import *
from tkinter import filedialog, messagebox
from PIL import Image, ImageTk
import pymysql.cursors
from datetime import datetime

KNOWN_FACES_FOLDER = 'know'
UNKNOWN_FACES_FOLDER = 'unkno'
DIFFERENCE = 0.4
MODEL = 'cnn'

known_faces = []
known_names = []
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

        clearButton = Button(self.btm_frame2, text="   Clear   ", font='Times 17', bg="#808000",
                             command=self.clearInformation)
        clearButton.pack(side=RIGHT, padx=5, pady=5)
        closeButton = Button(self.btm_frame2, text="   Close   ",font='Times 17',bg="#880000", command=self.closeInformation)
        closeButton.pack(side=RIGHT, padx=5, pady=5)

        pic = ImageTk.PhotoImage(Image.open("file1.png"))
        file1_bt = Button(self.top_frame, text='  Choose Image  ', image=pic, compound=LEFT, bg='yellow', fg='red', command=self.browseFile,font='Times 15')
        file1_bt.image = pic
        file1_bt.place(x=0,y=0)
        file1_bt.grid(row=1, column=5,padx=100)

        btn = Button(self.top_frame, text="   Search   ", bg="orange", fg="red", font='Times 15', command=self.searchImages)
        btn.grid(row=1, column=6, padx=50)

        self.center.grid_rowconfigure(0, weight=1)
        self.center.grid_columnconfigure(1, weight=1)

    def browseFile(self):
        self.filename = filedialog.askopenfilename(initialdir="/", title="Select A File", filetype = (("JPG File", "*.jpg"), ("JPEG File", "*.jpeg"), ("PNG File", "*.png"), ("All Files", "*.*")))
        self.img = Image.open(self.filename)
        pic = ImageTk.PhotoImage(Image.open(self.filename))
        self.center.anh_hien_lb = Label(self.center, image=pic, anchor=tkinter.NW)
        self.center.anh_hien_lb.image = pic

        w, h = self.img.size
        scrW = self.center.winfo_screenwidth() # lấy chiều rộng khung ảnh
        self.center.anh_hien_lb.place(x=(scrW//2)-(w//2), y=0, width=w, height=h)

    def closeInformation(self):
        sys.exit()
    def clearInformation(self):
        self.initUI()
    def searchImages(self):
        imgs = cv2.imread(self.filename)
        arrFileName = self.filename.split("/")
        name = arrFileName[len(arrFileName) - 1]
        arrName = name.split(".", 1)
        file = arrName[len(arrName) - 1]
        dt_string = (datetime.now()).strftime("%Y/%m/%d %H:%M:%S")  # lấy ngày và giờ hiện tại
        self.nameImage = str(dt_string.replace("/","_")).replace(" ","_").replace(":","_")+"."+file
        path = "test"
        if not os.path.exists(path):
            os.mkdir(path)
        cv2.imwrite(path + "/" + self.nameImage, imgs)

        for name in os.listdir(KNOWN_FACES_FOLDER):

            for filename in os.listdir(f'{KNOWN_FACES_FOLDER}/{name}'):
                image = face_recognition.load_image_file(f'{KNOWN_FACES_FOLDER}/{name}/{filename}')

                # return list found face
                encoding = face_recognition.face_encodings(image)[0]

                known_faces.append(encoding)
                known_names.append(name)

        # train
        #print(f'Filename {self.fileName}')'
        print("FILE NAME: ", self.nameImage)
        image = face_recognition.load_image_file('test/'+self.nameImage)

        locations = face_recognition.face_locations(image, model=MODEL)

        encodings = face_recognition.face_encodings(image, locations)

        image = cv2.cvtColor(image, cv2.COLOR_RGB2BGR)

        print(f', found {len(encodings)} face(s)')
        for face_encoding, face_location in zip(encodings, locations):

            results = face_recognition.compare_faces(known_faces, face_encoding, DIFFERENCE)

            name = "unknow"
            # print(name)

            if True not in results:

                top_left = (face_location[3], face_location[0])
                bottom_right = (face_location[1], face_location[2])

                cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)

                # pain text
                top_left = (face_location[3], face_location[2])
                bottom_right = (face_location[1], face_location[2] + 22)

                cv2.rectangle(image, top_left, bottom_right, (0, 255, 0), cv2.FILLED)

                cv2.putText(image, name, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5,
                            (200, 200, 200), 3)
            else:
                arr = []
                for i in range(len(known_names)):
                    if results[i] == True:
                        if known_names[i] not in arr:
                            arr.append(known_names[i])
                        else:
                            arr.append(known_names[i])

                # print(arr)
                dem = Counter(arr)
                sl = []

                pt = []
                if len(arr) != 0:
                    sl.append(dem[arr[0]])
                    pt.append(arr[0])
                for i in range(len(arr) - 1):
                    if arr[i] != arr[i + 1]:
                        sl.append(dem[arr[i + 1]])
                        pt.append(arr[i + 1])
                # print(sl)
                # print(pt)

                if len(sl) != 0:
                    max1 = max(sl)

                # print(max1)

                arrName = []
                for i in range(len(pt)):
                    if sl[i] == max1:
                        arrName.append(pt[i])

                # print(arrName)
                name_name = ""
                for i in arrName:
                    name = i
                    print("NAME: ", name)
                    name_name = name
                    print(f' - {name} from {results}')

                    top_left = (face_location[3], face_location[0])
                    bottom_right = (face_location[1], face_location[2])

                    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), 2)

                    top_left = (face_location[3], face_location[2])
                    bottom_right = (face_location[1], face_location[2] + 22)

                    cv2.rectangle(image, top_left, bottom_right, (0, 0, 255), cv2.FILLED)

                    cv2.putText(image, name, (face_location[3] + 10, face_location[2] + 15), cv2.FONT_HERSHEY_SIMPLEX, 0.5, (200, 200, 200), 2)

        cv2.imwrite(path + "/" + name_name + "_"+ self.nameImage, image)
        print("NAME_NAME: ", name_name)
        pic = ImageTk.PhotoImage(Image.open(path + "/" + name_name + "_" + self.nameImage))
        self.initUI()
        self.center.anh_hien_lb = Label(self.center, image=pic, anchor=tkinter.NW)
        self.center.anh_hien_lb.image = pic
        w, h = self.img.size
        scrW = self.center.winfo_screenwidth()  # lấy chiều rộng khung ảnh
        self.center.anh_hien_lb.place(x=(scrW //3) - (w // 3), y=0, width=w, height=h)

        self.center.information_lb = Label(self.center, text='Thông tin cá nhân',font='Times 17',fg="red")
        self.center.information_lb.place(x=(scrW //2) + (w // 2)+20, y=50)

        self.center.ho_ten_lb = Label(self.center, text='Họ và tên: ', font='Times 15', fg="black")
        self.center.ho_ten_lb.place(x=(scrW // 2) + (w // 2), y=90)

        self.hoTen = StringVar()
        self.center.hoTen_lb = Label(self.center, textvariable = self.hoTen, font='Times 15', fg="black")
        self.center.hoTen_lb.place(x=(scrW // 2) + (w // 2)+100, y=90)

        self.center.ngay_sinh_lb = Label(self.center, text='Ngày sinh: ', font='Times 15', fg="black")
        self.center.ngay_sinh_lb.place(x=(scrW // 2) + (w // 2), y=125)

        self.ngaySinh = StringVar()
        self.center.ngaySinh_lb = Label(self.center, textvariable=self.ngaySinh, font='Times 15', fg="black")
        self.center.ngaySinh_lb.place(x=(scrW // 2) + (w // 2) + 100, y=125)

        self.center.gioi_tinh_lb = Label(self.center, text='Giới tính: ', font='Times 15', fg="black")
        self.center.gioi_tinh_lb.place(x=(scrW // 2) + (w // 2), y=155)

        self.gioiTinh = StringVar()
        self.center.gioiTinh_lb = Label(self.center, textvariable=self.gioiTinh, font='Times 15', fg="black")
        self.center.gioiTinh_lb.place(x=(scrW // 2) + (w // 2) + 100, y=155)

        try:
            with connection.cursor() as cursor:
                # SQL
                sql = "SELECT * FROM information"

                print("sql: ", sql)
                # Thực thi câu lệnh truy vấn (Execute Query).
                number_of_rows = cursor.execute(sql)
                for i in cursor:
                    nameX = i["name"].replace(" ", "")
                    if (nameX.strip() == name_name):
                        self.hoTen.set(i["name"])
                        self.ngaySinh.set(i["date_of_birth"])
                        self.gioiTinh.set(i["gender"])
                # connection.close()
        except pymysql.Error as e:
            print("ERROR: ", e)
        #cv2.imshow(self.filename, image)
        #cv2.waitKey(0)
        #cv2.destroyWindow(filename)
root = Tk()
scrollbar = Scrollbar(root)
root.geometry("1000x1000+600+100")
app = Example(root)
root.mainloop()