import tkinter as tk                
from tkinter import font as tkfont 
from PIL import ImageTk, Image
import random

class Person:
    def __init__(self ,nId ,fn ,ln ,age ,sex ,email ,phone ,address ,city ,password):
        if len(nId) == 10:
            self.nationalId = nId
        else:
            self.nationalId = 0
        self.firstName = fn
        self.lastName = ln
        if len(age) == 2:
            self.age = age
        else:
            self.age = 0
        self.sex = sex
        if '@' in email:
            self.email = email
        else:
            self.email = ''
        self.phone = phone
        self.address = address
        self.city = city
        if len(password) == 8:
            self.password = password
        else:
            self.password = '00000000'
    def getNationalId(self):
        print(self.nationalId)
    def getFirstName(self):
        print(self.firstName)
    def getLastName(self):
        print(self.lastName)
    def getAge(self):
        print(self.age)
    def getSex(self):
        print(self.sex)
    def getEmail(self):
        print(self.email)
    def getPhone(self):
        print(self.phone)
    def getAddress(self):
        print(self.address)
    def getCity(self):
        print(self.city)
    def getPassword(self):
        print(self.password)
    
    def setNationalId(self ,nId):
        if len(nId) == 10 and type(nId) is int:
            self.nationalId = nId
        else:
            print('invalid national id!!!')
    def setFirstName(self ,fn):
        self.firstName = fn
    def setLastName(self ,ln):
        self.lastName = ln
    def setAge(self ,age):
        if len(age) == 2 and type(age) is int:
            self.age = age
        else:
            print('invalid national id!!!')
    def setSex(self ,sex):
        self.sex = sex
    def setEmail(self ,email):
        if '@' in email:
            self.email = email
        else:
            print('Email is not valid!!')
    def setPhone(self ,ph_num):
        if len(ph_num) == 11:
            self.phone_number = ph_num
        else:
            print('Phone number is not valid !!!')
    def setAddress(self ,add):
        self.address = add
    def setCity(self ,city):
        self.city = city
    def setPassword(self ,password):
        if len(password) == 8:
            self.password = password
        else:
            print('password lenght is not correct')
    def __repr__(self):
        return self.nationalId
    def showInfo(self):
        print(self.nationalId ,self.firstName ,self.lastName ,self.age ,self.sex ,self.email ,
              self.phone ,self.address ,self.city ,self.password)
        
class Doctor(Person):
    def __init__(self ,nId ,fn ,ln ,age ,sex ,email ,phone ,address ,city ,password ,dId ,specialty):
        self.doctorId = dId
        self.specialty = specialty
        Person.__init__(self ,nId ,fn ,ln ,age ,sex ,email ,phone ,address ,city ,password)
        
    def getDoctorId(self):
        print(self.doctorId)
    def getSpecialty(self):
        print(self.specialty)
    
    def setDoctorId(self ,dId):
        self.doctorId = dId
    
    def setSpecialty(self ,specialty):
        self.specialty = specialty
    def __repr__(self):
        return self.doctorId
    def showInfo(self):
        print(self.nationalId ,self.firstName ,self.lastName ,self.age ,self.sex ,self.email ,
              self.phone ,self.address ,self.city ,self.password ,self.doctorId ,self.specialty)
        
class Nurse(Person):
    def __init__(self ,nId ,fn ,ln ,age ,sex ,email ,phone ,address ,city ,password ,nurseId ,level):
        self.nurseId = nurseId
        self.level = level
        Person.__init__(self ,nId ,fn ,ln ,age ,sex ,email ,phone ,address ,city ,password)
        
    def getNurseId(self):
        return self.nurseId
    def getlevel(self):
        return self.level
    
    def setNurseId(self ,nId):
        self.nurseId = nId

    def setSpecialty(self ,level):
        self.level = level
    def __repr__(self):
        return self.nurseId
    def showInfo(self):
        print(self.nationalId ,self.firstName ,self.lastName ,self.age ,self.sex ,self.email ,
              self.phone ,self.address ,self.city ,self.password ,self.nurseId ,self.level)
class Doctor_list:
    def __init__(self ,doc_1 = []):
        if type(doc_1) is list: 
            self.doctor_list = doc_1
        else:
            self.doctor_list = []
            
    def getDoctor_list(self):
        return self.doctor_list
    
    def add_doctor(self ,obj_doc):
        if (type(obj_doc) is Doctor):
            for obj in self.doctor_list:
                if obj is obj_doc:
                    print('This doctor inserted')
                    return
            self.doctor_list.append(obj_doc)
        else:
            print('input is not type of doctor')
    def displayinfo(self):
        for obj in self.doctor_list:
            obj.showInfo() 
            
class Nurse_list:
    def __init__(self ,nurse_1 = []):
        if type(nurse_1) is list: 
            self.nurse_list = nurse_1
        else:
            self.nurse_list = []
            
    def getnurse_list(self):
        return self.nurse_list
    
    def add_nurse(self ,obj_nurse):
        if (type(obj_nurse) is Nurse):
            for obj in self.nurse_list:
                if obj is obj_nurse:
                    print('This nurse inserted')
                    return
            self.nurse_list.append(obj_nurse)
        else:
            print('input is not type of nurse')
    def displayinfo(self):
        for obj in self.nurse_list:
            obj.showInfo()

class Patient(Person):
    def __init__(self ,nId ,fn ,ln ,age ,sex ,email ,phone ,address ,city ,password ,illness ,dname
                ,nname ,pyment):
        self.illness = illness
        self.dname = dname
        self.nname = nname
        self.pyment = pyment
        Person.__init__(self ,nId ,fn ,ln ,age ,sex ,email ,phone ,address ,city ,password)
        
    def getillness(self):
        return self.illness
    
    def setSpecialty(self ,illness):
        self.illness = illness
    def showInfo(self):
        print(self.nationalId ,self.firstName ,self.lastName ,self.age ,self.sex ,self.email ,
              self.phone ,self.address ,self.city ,self.password ,self.illness)
        
class P_list:
    def __init__(self ,p_1 = []):
        if type(p_1) is list: 
            self.p_list = p_1
        else:
            self.p_list = []
            
    def getp_list(self):
        return self.p_list
    
    def add_p(self ,obj_p):
        if (type(obj_p) is Patient):
            for obj in self.p_list:
                if obj is obj_p:
                    print('This p inserted')
                    return
            self.p_list.append(obj_p)
        else:
            print('input is not type of p')
    def displayinfo(self):
        for obj in self.p_list:
            obj.showInfo()

doctorlist = Doctor_list()
doctorlist2 = list()
nurselist = Nurse_list()
nurselist2 = list()
plist = P_list()
plist2 = list()
######################################################################

class HospitalApp(tk.Tk):

    def __init__(self, *args, **kwargs):
        tk.Tk.__init__(self, *args, **kwargs)

        self.title_font = tkfont.Font(family = 'Helvetica' ,size = 30 ,weight = 'bold' ,slant = 'italic')

        container = tk.Frame(self)
        container.pack(side='top', fill='both', expand=True)
        container.grid_rowconfigure(0, weight=1)
        container.grid_columnconfigure(0, weight=1)

        self.frames = {}
        for F in (MainPage, DoctorPage, NursePage, PatientPart, LoginDoctor,
                 changePasswordDoctor , searchPatientD, searchNurseD ,RegisterD 
                 ,LoginNurse ,changePasswordNurse ,searchPatientN ,searchNurseN ,RegisterN
                 ,LoginPatient ,changePasswordPatient ,RegisterP):
            page_name = F.__name__
            frame = F(parent=container, controller=self)
            self.frames[page_name] = frame
            frame.config(bg = 'purple')

            frame.grid(row=0, column=0, sticky='nsew')

        self.show_frame('MainPage')
        self.title('Hospital Management')
        self.geometry('500x600')


    def show_frame(self, page_name):
        frame = self.frames[page_name]
        frame.tkraise()

class MainPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        
        label = tk.Label(self, text='Wellcom to our Hospital', font=controller.title_font)
        label.config(bg = 'gray')
        label.pack(side = 'top' ,fill = 'x' ,pady = 0)
        
        #your path of photo 
        self.photo1 = ImageTk.PhotoImage(Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\hospital.png'))
        l1 = tk.Label(self ,image = self.photo1)
        l1.config(bg = 'purple')
        l1.pack(side = 'top' ,fill = 'x' ,pady = 40)
        
        button1 = tk.Button(self, text = 'Doctor', width = 15 ,
                            command=lambda: controller.show_frame( 'DoctorPage'))
        l2 = tk.Label(self)
        l2.config(bg = 'purple')
        button2 = tk.Button(self ,text = 'Nurse', width = 15 ,
                           command = lambda :controller.show_frame('NursePage'))
        l3 = tk.Label(self)
        l3.config(bg = 'purple')
        button3 = tk.Button(self, text = 'Patient', width = 15 ,
                            command=lambda: controller.show_frame('PatientPart'))
        
        button1.pack(side = 'top')
        l2.pack(side = 'top')
        button2.pack(side = 'top')
        l3.pack(side = 'top')
        button3.pack(side = 'top')

class DoctorPage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        #your path of photo 
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\doctor.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'doctor' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,command=lambda: controller.show_frame("MainPage"))
        button.place(x = 385 ,y = 35)
        b1 = tk.Button(self ,text = 'login' ,width = 16 ,
                      command = lambda : controller.show_frame('LoginDoctor'))
        b1.place(x = 170 ,y = 250)
        b2 = tk.Button(self ,text = 'Register' ,width = 16 ,
                      command = lambda : controller.show_frame('RegisterD'))
        b2.place(x = 170 ,y = 300)

class PatientPart(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        #your path of photo 
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\user.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'patient' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,command=lambda: controller.show_frame("MainPage"))
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'National Id :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 95 ,y = 150)
        e1 = tk.Entry(self)
        e1.place(x = 170 ,y = 150)
        l4 = tk.Label(self ,text = 'Password :' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 100 ,y = 200)
        e2 = tk.Entry(self)
        e2.place(x = 170 ,y = 200)
        b1 = tk.Button(self ,text = 'login' ,width = 16,
                      command = lambda :controller.show_frame('LoginPatient'))
        b1.place(x = 170 ,y = 250)
        b2 = tk.Button(self ,text = 'Register' ,width = 16,
                      command = lambda :controller.show_frame('RegisterP'))
        b2.place(x = 170 ,y = 300)
        b3 = tk.Button(self ,text = 'clear' ,width = 16)
        b3.place(x = 170 ,y = 350)
        
        
class NursePage(tk.Frame):

    def __init__(self, parent, controller):
        tk.Frame.__init__(self, parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        #your path of photo 
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\nurse.jpg')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'nurse' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,command=lambda: controller.show_frame("MainPage"))
        button.place(x = 385 ,y = 35)
        b1 = tk.Button(self ,text = 'login' ,width = 16
                      , command = lambda :controller.show_frame('LoginNurse'))
        b1.place(x = 170 ,y = 250)
        b2 = tk.Button(self ,text = 'Register' ,width = 16
                      , command = lambda :controller.show_frame('RegisterN'))
        b2.place(x = 170 ,y = 300)
        

######################################################################################
class LoginDoctor(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        #your path of photo 
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\doctor.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'doctor' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("DoctorPage"))
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'doctor ID :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        self.e1 = tk.Entry(self)
        self.e1.place(x = 85 ,y = 130)
        l4 = tk.Label(self ,text = 'password :' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 220 ,y = 130)
        self.e2 = tk.Entry(self)
        self.e2.place(x = 295 ,y = 130)
        b5 = tk.Button(self ,text = 'login' ,width = 16 ,command = self.logindoctor)
        b5.place(x = 295 ,y = 160)
        
        l5 = tk.Label(self ,text = 'national ID :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        self.e3 = tk.Entry(self)
        self.e3.place(x = 85 ,y = 190)
        l6 = tk.Label(self ,text = 'first name :' ,font = ('Helvetica' ,10))
        l6.config(bg = 'purple')
        l6.place(x = 10 ,y = 220)
        self.e4 = tk.Entry(self)
        self.e4.place(x = 85 ,y = 220)
        l7 = tk.Label(self ,text = 'last name :' ,font = ('Helvetica' ,10))
        l7.config(bg = 'purple')
        l7.place(x = 10 ,y = 250)
        self.e5 = tk.Entry(self)
        self.e5.place(x = 85 ,y = 250)
        l8 = tk.Label(self ,text = 'age :' ,font = ('Helvetica' ,10))
        l8.config(bg = 'purple')
        l8.place(x = 10 ,y = 280)
        self.e6 = tk.Entry(self)
        self.e6.place(x = 85 ,y = 280)
        l9 = tk.Label(self ,text = 'sex :' ,font = ('Helvetica' ,10))
        l9.config(bg = 'purple')
        l9.place(x = 10 ,y = 310)
        self.e7 = tk.Entry(self)
        self.e7.place(x = 85 ,y = 310)
        l10 = tk.Label(self ,text = 'email :' ,font = ('Helvetica' ,10))
        l10.config(bg = 'purple')
        l10.place(x = 10 ,y = 340)
        self.e8 = tk.Entry(self)
        self.e8.place(x = 85 ,y = 340)
        l11 = tk.Label(self ,text = 'phone :' ,font = ('Helvetica' ,10))
        l11.config(bg = 'purple')
        l11.place(x = 220 ,y = 190)
        self.e9 = tk.Entry(self)
        self.e9.place(x = 295,y = 190)
        l12 = tk.Label(self ,text = 'address :' ,font = ('Helvetica' ,10))
        l12.config(bg = 'purple')
        l12.place(x = 220 ,y = 220)
        self.e10 = tk.Entry(self)
        self.e10.place(x = 295 ,y = 220)
        l13 = tk.Label(self ,text = 'city :' ,font = ('Helvetica' ,13))
        l13.config(bg = 'purple')
        l13.place(x = 220 ,y = 250)
        self.e11 = tk.Entry(self)
        self.e11.place(x = 295 ,y = 250)
        l14 = tk.Label(self ,text = 'specialty :' ,font = ('Helvetica' ,10))
        l14.config(bg = 'purple')
        l14.place(x = 220 ,y = 280)
        self.e12 = tk.Entry(self)
        self.e12.place(x = 295 ,y = 280)
        b2 = tk.Button(self ,text = 'change password' ,width = 16 ,
                      command = lambda : controller.show_frame('changePasswordDoctor'))
        b2.place(x = 295 ,y = 340)
        b3 = tk.Button(self ,text = 'search in patient' ,width = 16 ,
                      command = lambda : controller.show_frame('searchPatientD'))
        b3.place(x = 85 ,y = 400)
        b4 = tk.Button(self ,text = 'search in nurse' ,width = 16 ,
                      command = lambda : controller.show_frame('searchNurseD'))
        b4.place(x = 295 ,y = 400)
        self.list2 = tk.Listbox(self ,width = 30 ,height = 5)
        self.list2.place(x = 150,y = 450)
        
    def logindoctor(self):
        doctorlId = self.e1.get()
        password = self.e2.get()
        for obj in doctorlist2:
            if obj.doctorId == doctorlId and obj.password == password:
                self.e3.delete(0 ,'end')
                self.e3.insert(0 ,str(obj.nationalId))
                self.e4.delete(0 ,'end')
                self.e4.insert(0 ,str(obj.firstName))
                self.e5.delete(0 ,'end')
                self.e5.insert(0 ,str(obj.lastName))
                self.e6.delete(0 ,'end')
                self.e6.insert(0 ,str(obj.age))
                self.e7.delete(0 ,'end')
                self.e7.insert(0 ,str(obj.sex))
                self.e8.delete(0 ,'end')
                self.e8.insert(0 ,str(obj.email))
                self.e9.delete(0 ,'end')
                self.e9.insert(0 ,str(obj.phone))
                self.e10.delete(0 ,'end')
                self.e10.insert(0 ,str(obj.address))
                self.e11.delete(0 ,'end')
                self.e11.insert(0 ,str(obj.city))
                self.e12.delete(0 ,'end')
                self.e12.insert(0 ,str(obj.specialty))
                self.list2.insert(0 ,str('doctor found'))
                break
            else:
                self.list2.insert(0 ,str('user not found'))       

        
class changePasswordDoctor(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\doctor.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'doctor' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("LoginDoctor")) 
        button.place(x = 385 ,y = 35)
        l2 = tk.Label(self ,text = 'new password :' ,font = ('Helvetica' ,10))
        l2.config(bg = 'purple')
        l2.place(x = 170 ,y = 130)
        self.e1 = tk.Entry(self)
        self.e1.place(x = 270 ,y = 130)
        l3 = tk.Label(self ,text = 'old password :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 170 ,y = 160)
        self.e2 = tk.Entry(self)
        self.e2.place(x = 270 ,y = 160)
        b1 = tk.Button(self ,text = 'update password' ,width = 16 ,
                      command = self.changepass)
        b1.place(x = 270 ,y = 190)
        self.list3 = tk.Listbox(self ,width = 30 ,height = 5)
        self.list3.place(x = 150,y = 450)
    
    def changepass(self):
        new = self.e1.get()
        old = self.e2.get()
        for obj in doctorlist2:
            if obj.password == old:
                obj.password = new
                self.list3.insert(0 ,str('update sucess'))
            else:
                self.list3.insert(0 ,str('update fail'))
        
class searchPatientD(tk.Frame):
      def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\doctor.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'doctor' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("LoginDoctor")) 
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'national ID:' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        e1 = tk.Entry(self)
        e1.place(x = 85 ,y = 130)
        b1 = tk.Button(self ,text = 'search' ,width = 16)
        b1.place(x = 85 ,y = 160)
        l4 = tk.Label(self ,text = 'blood group:' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 220 ,y = 130)
        e2 = tk.Entry(self)
        e2.place(x = 295,y = 130)
        b2 = tk.Button(self ,text = 'search' ,width = 16)
        b2.place(x = 295 ,y = 160)
        l5 = tk.Label(self ,text = 'deses:' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        e3 = tk.Entry(self)
        e3.place(x = 85 ,y = 190)
        b2 = tk.Button(self ,text = 'search' ,width = 16)
        b2.place(x = 85 ,y = 220)
        list1 = tk.Listbox(self ,width=50 ,height=20)
        list1.place(x = 85 ,y = 250)
        
class searchNurseD(tk.Frame):
      def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\doctor.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'doctor' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("LoginDoctor")) 
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'nurse ID:' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        e1 = tk.Entry(self)
        e1.place(x = 85 ,y = 130)
        b1 = tk.Button(self ,text = 'search' ,width = 16)
        b1.place(x = 85 ,y = 160)
        l5 = tk.Label(self ,text = 'level:' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        e3 = tk.Entry(self)
        e3.place(x = 85 ,y = 190)
        b2 = tk.Button(self ,text = 'search' ,width = 16)
        b2.place(x = 85 ,y = 220)
        list1 = tk.Listbox(self ,width=50 ,height=20)
        list1.place(x = 85 ,y = 250)
        
class RegisterD(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\doctor.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'doctor' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("DoctorPage"))
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'national ID :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        self.e1 = tk.Entry(self)
        self.e1.place(x = 85 ,y = 130)
        l4 = tk.Label(self ,text = 'first name :' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 10 ,y = 160)
        self.e2 = tk.Entry(self)
        self.e2.place(x = 85 ,y = 160)
        l5 = tk.Label(self ,text = 'last name :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        self.e3 = tk.Entry(self)
        self.e3.place(x = 85 ,y = 190)
        l5 = tk.Label(self ,text = 'age :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 220)
        self.e4 = tk.Entry(self)
        self.e4.place(x = 85 ,y = 220)
        l6 = tk.Label(self ,text = 'sex :' ,font = ('Helvetica' ,10))
        l6.config(bg = 'purple')
        l6.place(x = 10 ,y = 250)
        self.e5 = tk.Entry(self)
        self.e5.place(x = 85 ,y = 250)
        l7 = tk.Label(self ,text = 'email :' ,font = ('Helvetica' ,10))
        l7.config(bg = 'purple')
        l7.place(x = 10 ,y = 280)
        self.e6 = tk.Entry(self)
        self.e6.place(x = 85 ,y = 280)
        l8 = tk.Label(self ,text = 'phone :' ,font = ('Helvetica' ,10))
        l8.config(bg = 'purple')
        l8.place(x = 220 ,y = 130)
        self.e7 = tk.Entry(self)
        self.e7.place(x = 295,y = 130)
        l9 = tk.Label(self ,text = 'address :' ,font = ('Helvetica' ,10))
        l9.config(bg = 'purple')
        l9.place(x = 220 ,y = 160)
        self.e8 = tk.Entry(self)
        self.e8.place(x = 295 ,y = 160)
        l10 = tk.Label(self ,text = 'city :' ,font = ('Helvetica' ,10))
        l10.config(bg = 'purple')
        l10.place(x = 220 ,y = 190)
        self.e9 = tk.Entry(self)
        self.e9.place(x = 295 ,y = 190)
        l11 = tk.Label(self ,text = 'password :' ,font = ('Helvetica' ,10))
        l11.config(bg = 'purple')
        l11.place(x = 220 ,y = 220)
        self.e10 = tk.Entry(self)
        self.e10.place(x = 295 ,y = 220)
        l12 = tk.Label(self ,text = 'doctorId :' ,font = ('Helvetica' ,10))
        l12.config(bg = 'purple')
        l12.place(x = 220 ,y = 250)
        self.e11 = tk.Entry(self)
        self.e11.place(x = 295 ,y = 250)
        l13 = tk.Label(self ,text = 'specialty :' ,font = ('Helvetica' ,10))
        l13.config(bg = 'purple')
        l13.place(x = 220 ,y = 280)
        self.e12 = tk.Entry(self)
        self.e12.place(x = 295 ,y = 280)
        b1 = tk.Button(self ,text = 'save' ,width = 16 ,command = self.savedoctor)
        b1.place(x = 180 ,y = 310)
        self.list1 = tk.Listbox(self ,width = 30 ,height = 10)
        self.list1.place(x = 150,y = 340)
        
    def savedoctor(self):
        nationalId = self.e1.get()
        firstName = self.e2.get()
        lastName = self.e3.get()
        age = self.e4.get()
        sex = self.e5.get()
        email = self.e6.get()
        phone = self.e7.get()
        address = self.e8.get()
        city = self.e9.get()
        password = self.e10.get()
        doctorId = self.e11.get()
        spe = self.e12.get()
        doctor = Doctor(nationalId ,firstName ,lastName ,age ,sex ,email ,phone ,address ,city , 
                        password, doctorId, spe)
        doctorlist.add_doctor(doctor)
        doctorlist2.append(doctor)
        self.list1.insert(0 ,doctorId ,str('doctor registerd'))

        
#######################################################################################
class LoginNurse(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\nurse.jpg')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'nurse' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("NursePage"))
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'nurse ID :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        self.e1 = tk.Entry(self)
        self.e1.place(x = 85 ,y = 130)
        l4 = tk.Label(self ,text = 'password :' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 220 ,y = 130)
        self.e2 = tk.Entry(self)
        self.e2.place(x = 295 ,y = 130)
        b5 = tk.Button(self ,text = 'login' ,width = 16 ,command = self.loginnurse)
        b5.place(x = 295 ,y = 160)
        
        l5 = tk.Label(self ,text = 'national ID :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        self.e3 = tk.Entry(self)
        self.e3.place(x = 85 ,y = 190)
        l6 = tk.Label(self ,text = 'first name :' ,font = ('Helvetica' ,10))
        l6.config(bg = 'purple')
        l6.place(x = 10 ,y = 220)
        self.e4 = tk.Entry(self)
        self.e4.place(x = 85 ,y = 220)
        l7 = tk.Label(self ,text = 'last name :' ,font = ('Helvetica' ,10))
        l7.config(bg = 'purple')
        l7.place(x = 10 ,y = 250)
        self.e5 = tk.Entry(self)
        self.e5.place(x = 85 ,y = 250)
        l8 = tk.Label(self ,text = 'age :' ,font = ('Helvetica' ,10))
        l8.config(bg = 'purple')
        l8.place(x = 10 ,y = 280)
        self.e6 = tk.Entry(self)
        self.e6.place(x = 85 ,y = 280)
        l9 = tk.Label(self ,text = 'sex :' ,font = ('Helvetica' ,10))
        l9.config(bg = 'purple')
        l9.place(x = 10 ,y = 310)
        self.e7 = tk.Entry(self)
        self.e7.place(x = 85 ,y = 310)
        l10 = tk.Label(self ,text = 'email :' ,font = ('Helvetica' ,10))
        l10.config(bg = 'purple')
        l10.place(x = 10 ,y = 340)
        self.e8 = tk.Entry(self)
        self.e8.place(x = 85 ,y = 340)
        l11 = tk.Label(self ,text = 'phone :' ,font = ('Helvetica' ,10))
        l11.config(bg = 'purple')
        l11.place(x = 220 ,y = 190)
        self.e9 = tk.Entry(self)
        self.e9.place(x = 295,y = 190)
        l12 = tk.Label(self ,text = 'address :' ,font = ('Helvetica' ,10))
        l12.config(bg = 'purple')
        l12.place(x = 220 ,y = 220)
        self.e10 = tk.Entry(self)
        self.e10.place(x = 295 ,y = 220)
        l13 = tk.Label(self ,text = 'city :' ,font = ('Helvetica' ,13))
        l13.config(bg = 'purple')
        l13.place(x = 220 ,y = 250)
        self.e11 = tk.Entry(self)
        self.e11.place(x = 295 ,y = 250)
        l14 = tk.Label(self ,text = 'level :' ,font = ('Helvetica' ,10))
        l14.config(bg = 'purple')
        l14.place(x = 220 ,y = 280)
        self.e12 = tk.Entry(self)
        self.e12.place(x = 295 ,y = 280)
        b2 = tk.Button(self ,text = 'change password' ,width = 16 ,
                      command = lambda : controller.show_frame('changePasswordNurse'))
        b2.place(x = 295 ,y = 340)
        b3 = tk.Button(self ,text = 'search in patient' ,width = 16 ,
                      command = lambda : controller.show_frame('searchPatientN'))
        b3.place(x = 85 ,y = 400)
        b4 = tk.Button(self ,text = 'search in nurse' ,width = 16 ,
                      command = lambda : controller.show_frame('searchNurseN'))
        b4.place(x = 295 ,y = 400)
        self.list2 = tk.Listbox(self ,width = 30 ,height = 5)
        self.list2.place(x = 150,y = 450)
        
    def loginnurse(self):
        nurselId = self.e1.get()
        password = self.e2.get()
        for obj in nurselist2:
            if obj.nurseId == nurselId and obj.password == password:
                self.e3.delete(0 ,'end')
                self.e3.insert(0 ,str(obj.nationalId))
                self.e4.delete(0 ,'end')
                self.e4.insert(0 ,str(obj.firstName))
                self.e5.delete(0 ,'end')
                self.e5.insert(0 ,str(obj.lastName))
                self.e6.delete(0 ,'end')
                self.e6.insert(0 ,str(obj.age))
                self.e7.delete(0 ,'end')
                self.e7.insert(0 ,str(obj.sex))
                self.e8.delete(0 ,'end')
                self.e8.insert(0 ,str(obj.email))
                self.e9.delete(0 ,'end')
                self.e9.insert(0 ,str(obj.phone))
                self.e10.delete(0 ,'end')
                self.e10.insert(0 ,str(obj.address))
                self.e11.delete(0 ,'end')
                self.e11.insert(0 ,str(obj.city))
                self.e12.delete(0 ,'end')
                self.e12.insert(0 ,str(obj.level))
                self.list2.insert(0 ,str('nurse found'))
                break
            else:
                self.list2.insert(0 ,str('user not found'))   

class changePasswordNurse(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\nurse.jpg')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'nurse' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("LoginNurse")) 
        button.place(x = 385 ,y = 35)
        l2 = tk.Label(self ,text = 'new password :' ,font = ('Helvetica' ,10))
        l2.config(bg = 'purple')
        l2.place(x = 170 ,y = 130)
        self.e1 = tk.Entry(self)
        self.e1.place(x = 270 ,y = 130)
        l3 = tk.Label(self ,text = 'old password :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 170 ,y = 160)
        self.e2 = tk.Entry(self)
        self.e2.place(x = 270 ,y = 160)
        b1 = tk.Button(self ,text = 'update password' ,width = 16 ,
                      command = self.changepassn)
        b1.place(x = 270 ,y = 190)
        self.list3 = tk.Listbox(self ,width = 30 ,height = 5)
        self.list3.place(x = 150,y = 450)
        
    def changepassn(self):
        new = self.e1.get()
        old = self.e2.get()
        for obj in nurselist2:
            if obj.password == old:
                obj.password = new
                self.list3.insert(0 ,str('update sucess'))
            else:
                self.list3.insert(0 ,str('update fail'))
        
        
class searchPatientN(tk.Frame):
      def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\nurse.jpg')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'nurse' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("LoginNurse")) 
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'national ID:' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        e1 = tk.Entry(self)
        e1.place(x = 85 ,y = 130)
        b1 = tk.Button(self ,text = 'search' ,width = 16)
        b1.place(x = 85 ,y = 160)
        l4 = tk.Label(self ,text = 'blood group:' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 220 ,y = 130)
        e2 = tk.Entry(self)
        e2.place(x = 295,y = 130)
        b2 = tk.Button(self ,text = 'search' ,width = 16)
        b2.place(x = 295 ,y = 160)
        l5 = tk.Label(self ,text = 'deses:' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        e3 = tk.Entry(self)
        e3.place(x = 85 ,y = 190)
        b2 = tk.Button(self ,text = 'search' ,width = 16)
        b2.place(x = 85 ,y = 220)
        list1 = tk.Listbox(self ,width=50 ,height=20)
        list1.place(x = 85 ,y = 250)
        
class searchNurseN(tk.Frame):
      def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\nurse.jpg')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'nurse' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("LoginNurse")) 
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'doctor ID:' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        e1 = tk.Entry(self)
        e1.place(x = 85 ,y = 130)
        b1 = tk.Button(self ,text = 'search' ,width = 16)
        b1.place(x = 85 ,y = 160)
        l5 = tk.Label(self ,text = 'specialty:' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        e3 = tk.Entry(self)
        e3.place(x = 85 ,y = 190)
        b2 = tk.Button(self ,text = 'search' ,width = 16)
        b2.place(x = 85 ,y = 220)
        list1 = tk.Listbox(self ,width=50 ,height=20)
        list1.place(x = 85 ,y = 250)
class RegisterN(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\nurse.jpg')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'nurse' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("NursePage"))
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'national ID :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        self.e1 = tk.Entry(self)
        self.e1.place(x = 85 ,y = 130)
        l4 = tk.Label(self ,text = 'first name :' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 10 ,y = 160)
        self.e2 = tk.Entry(self)
        self.e2.place(x = 85 ,y = 160)
        l5 = tk.Label(self ,text = 'last name :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        self.e3 = tk.Entry(self)
        self.e3.place(x = 85 ,y = 190)
        l5 = tk.Label(self ,text = 'age :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 220)
        self.e4 = tk.Entry(self)
        self.e4.place(x = 85 ,y = 220)
        l6 = tk.Label(self ,text = 'sex :' ,font = ('Helvetica' ,10))
        l6.config(bg = 'purple')
        l6.place(x = 10 ,y = 250)
        self.e5 = tk.Entry(self)
        self.e5.place(x = 85 ,y = 250)
        l7 = tk.Label(self ,text = 'email :' ,font = ('Helvetica' ,10))
        l7.config(bg = 'purple')
        l7.place(x = 10 ,y = 280)
        self.e6 = tk.Entry(self)
        self.e6.place(x = 85 ,y = 280)
        l8 = tk.Label(self ,text = 'phone :' ,font = ('Helvetica' ,10))
        l8.config(bg = 'purple')
        l8.place(x = 220 ,y = 130)
        self.e7 = tk.Entry(self)
        self.e7.place(x = 295,y = 130)
        l9 = tk.Label(self ,text = 'address :' ,font = ('Helvetica' ,10))
        l9.config(bg = 'purple')
        l9.place(x = 220 ,y = 160)
        self.e8 = tk.Entry(self)
        self.e8.place(x = 295 ,y = 160)
        l10 = tk.Label(self ,text = 'city :' ,font = ('Helvetica' ,10))
        l10.config(bg = 'purple')
        l10.place(x = 220 ,y = 190)
        self.e9 = tk.Entry(self)
        self.e9.place(x = 295 ,y = 190)
        l11 = tk.Label(self ,text = 'password :' ,font = ('Helvetica' ,10))
        l11.config(bg = 'purple')
        l11.place(x = 220 ,y = 220)
        self.e10 = tk.Entry(self)
        self.e10.place(x = 295 ,y = 220)
        l12 = tk.Label(self ,text = 'nurseId :' ,font = ('Helvetica' ,10))
        l12.config(bg = 'purple')
        l12.place(x = 220 ,y = 250)
        self.e11 = tk.Entry(self)
        self.e11.place(x = 295 ,y = 250)
        l13 = tk.Label(self ,text = 'level :' ,font = ('Helvetica' ,10))
        l13.config(bg = 'purple')
        l13.place(x = 220 ,y = 280)
        self.e12 = tk.Entry(self)
        self.e12.place(x = 295 ,y = 280)
        b1 = tk.Button(self ,text = 'save' ,width = 16 ,command = self.savenurse)
        b1.place(x = 180 ,y = 310)
        self.list1 = tk.Listbox(self ,width = 30 ,height = 10)
        self.list1.place(x = 150,y = 340)
        
    def savenurse(self):
        nationalId = self.e1.get()
        firstName = self.e2.get()
        lastName = self.e3.get()
        age = self.e4.get()
        sex = self.e5.get()
        email = self.e6.get()
        phone = self.e7.get()
        address = self.e8.get()
        city = self.e9.get()
        password = self.e10.get()
        nurseid = self.e11.get()
        level = self.e12.get()
        nurse = Nurse(nationalId ,firstName ,lastName ,age ,sex ,email ,phone ,address ,city , 
                        password, nurseid ,level)
        nurselist.add_nurse(nurse)
        nurselist2.append(nurse)
        self.list1.insert(0 ,nurseid ,str('nurse registerd'))
                
                
#######################################################################################
class LoginPatient(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\user.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'Patient' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("PatientPart"))
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'national ID :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        self.e1 = tk.Entry(self)
        self.e1.place(x = 85 ,y = 130)
        l4 = tk.Label(self ,text = 'password :' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 220 ,y = 130)
        self.e2 = tk.Entry(self)
        self.e2.place(x = 295 ,y = 130)
        b5 = tk.Button(self ,text = 'login' ,width = 16 ,command = self.loginp)
        b5.place(x = 295 ,y = 160)
        
        l5 = tk.Label(self ,text = 'national ID :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        self.e3 = tk.Entry(self)
        self.e3.place(x = 85 ,y = 190)
        l6 = tk.Label(self ,text = 'first name :' ,font = ('Helvetica' ,10))
        l6.config(bg = 'purple')
        l6.place(x = 10 ,y = 220)
        self.e4 = tk.Entry(self)
        self.e4.place(x = 85 ,y = 220)
        l7 = tk.Label(self ,text = 'last name :' ,font = ('Helvetica' ,10))
        l7.config(bg = 'purple')
        l7.place(x = 10 ,y = 250)
        self.e5 = tk.Entry(self)
        self.e5.place(x = 85 ,y = 250)
        l8 = tk.Label(self ,text = 'age :' ,font = ('Helvetica' ,10))
        l8.config(bg = 'purple')
        l8.place(x = 10 ,y = 280)
        self.e6 = tk.Entry(self)
        self.e6.place(x = 85 ,y = 280)
        l9 = tk.Label(self ,text = 'sex :' ,font = ('Helvetica' ,10))
        l9.config(bg = 'purple')
        l9.place(x = 10 ,y = 310)
        self.e7 = tk.Entry(self)
        self.e7.place(x = 85 ,y = 310)
        l10 = tk.Label(self ,text = 'email :' ,font = ('Helvetica' ,10))
        l10.config(bg = 'purple')
        l10.place(x = 10 ,y = 340)
        self.e8 = tk.Entry(self)
        self.e8.place(x = 85 ,y = 340)
        l11 = tk.Label(self ,text = 'phone :' ,font = ('Helvetica' ,10))
        l11.config(bg = 'purple')
        l11.place(x = 220 ,y = 190)
        self.e9 = tk.Entry(self)
        self.e9.place(x = 295,y = 190)
        l12 = tk.Label(self ,text = 'address :' ,font = ('Helvetica' ,10))
        l12.config(bg = 'purple')
        l12.place(x = 220 ,y = 220)
        self.e10 = tk.Entry(self)
        self.e10.place(x = 295 ,y = 220)
        l13 = tk.Label(self ,text = 'city :' ,font = ('Helvetica' ,13))
        l13.config(bg = 'purple')
        l13.place(x = 220 ,y = 250)
        self.e11 = tk.Entry(self)
        self.e11.place(x = 295 ,y = 250)
        l14 = tk.Label(self ,text = 'payment :' ,font = ('Helvetica' ,10))
        l14.config(bg = 'purple')
        l14.place(x = 220 ,y = 280)
        self.e12 = tk.Entry(self)
        self.e12.place(x = 295 ,y = 280)
        b2 = tk.Button(self ,text = 'change password' ,width = 16 ,
                      command = lambda : controller.show_frame('changePasswordPatient'))
        b2.place(x = 295 ,y = 340)
        self.list2 = tk.Listbox(self ,width = 30 ,height = 5)
        self.list2.place(x = 150,y = 450)
        
    def loginp(self):
        nationalId = self.e1.get()
        password = self.e2.get()
        for obj in plist2:
            if obj.nationalId == nationalId and obj.password == password:
                self.e3.delete(0 ,'end')
                self.e3.insert(0 ,str(obj.nationalId))
                self.e4.delete(0 ,'end')
                self.e4.insert(0 ,str(obj.firstName))
                self.e5.delete(0 ,'end')
                self.e5.insert(0 ,str(obj.lastName))
                self.e6.delete(0 ,'end')
                self.e6.insert(0 ,str(obj.age))
                self.e7.delete(0 ,'end')
                self.e7.insert(0 ,str(obj.sex))
                self.e8.delete(0 ,'end')
                self.e8.insert(0 ,str(obj.email))
                self.e9.delete(0 ,'end')
                self.e9.insert(0 ,str(obj.phone))
                self.e10.delete(0 ,'end')
                self.e10.insert(0 ,str(obj.address))
                self.e11.delete(0 ,'end')
                self.e11.insert(0 ,str(obj.city))
                self.e12.delete(0 ,'end')
                self.e12.insert(0 ,str(obj.payment))
                self.list2.insert(0 ,str('patent found'))
                break
            else:
                self.list2.insert(0 ,str('user not found'))   
        
        
class changePasswordPatient(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\user.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'Patient' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("LoginPatient")) 
        button.place(x = 385 ,y = 35)
        l2 = tk.Label(self ,text = 'new password :' ,font = ('Helvetica' ,10))
        l2.config(bg = 'purple')
        l2.place(x = 170 ,y = 130)
        

class RegisterP(tk.Frame):
    def __init__(self ,parent ,controller):
        tk.Frame.__init__(self ,parent)
        self.controller = controller
        f1 = tk.Frame(self ,width = 500 ,height = 110)
        f1.grid(row = 0 ,column = 0 ,pady = 0)
        f1.config(bg = 'gray')
        image = Image.open('C:\\Users\\hannane\\OneDrive\\Pictures\\Saved Pictures\\user.png')
        resize_image = image.resize((100 ,100))
        self.photo1 = ImageTk.PhotoImage(resize_image)
        l1 = tk.Label(f1 ,image = self.photo1)
        l1.place(x = 5 ,y = 5)
        l2 = tk.Label(f1 ,text = 'Patient' ,font = controller.title_font)
        l2.config(bg = 'gray')
        l2.place(x = 150 ,y = 25)
        button = tk.Button(f1, text="back", width = 10,
                           command=lambda: controller.show_frame("PatientPart"))
        button.place(x = 385 ,y = 35)
        l3 = tk.Label(self ,text = 'national ID :' ,font = ('Helvetica' ,10))
        l3.config(bg = 'purple')
        l3.place(x = 10 ,y = 130)
        self.e1 = tk.Entry(self)
        self.e1.place(x = 85 ,y = 130)
        l4 = tk.Label(self ,text = 'first name :' ,font = ('Helvetica' ,10))
        l4.config(bg = 'purple')
        l4.place(x = 10 ,y = 160)
        self.e2 = tk.Entry(self)
        self.e2.place(x = 85 ,y = 160)
        l5 = tk.Label(self ,text = 'last name :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 190)
        self.e3 = tk.Entry(self)
        self.e3.place(x = 85 ,y = 190)
        l5 = tk.Label(self ,text = 'age :' ,font = ('Helvetica' ,10))
        l5.config(bg = 'purple')
        l5.place(x = 10 ,y = 220)
        self.e4 = tk.Entry(self)
        self.e4.place(x = 85 ,y = 220)
        l6 = tk.Label(self ,text = 'sex :' ,font = ('Helvetica' ,10))
        l6.config(bg = 'purple')
        l6.place(x = 10 ,y = 250)
        self.e5 = tk.Entry(self)
        self.e5.place(x = 85 ,y = 250)
        l7 = tk.Label(self ,text = 'email :' ,font = ('Helvetica' ,10))
        l7.config(bg = 'purple')
        l7.place(x = 10 ,y = 280)
        self.e6 = tk.Entry(self)
        self.e6.place(x = 85 ,y = 280)
        l8 = tk.Label(self ,text = 'phone :' ,font = ('Helvetica' ,10))
        l8.config(bg = 'purple')
        l8.place(x = 220 ,y = 130)
        self.e7 = tk.Entry(self)
        self.e7.place(x = 295,y = 130)
        l9 = tk.Label(self ,text = 'address :' ,font = ('Helvetica' ,10))
        l9.config(bg = 'purple')
        l9.place(x = 220 ,y = 160)
        self.e8 = tk.Entry(self)
        self.e8.place(x = 295 ,y = 160)
        l10 = tk.Label(self ,text = 'city :' ,font = ('Helvetica' ,10))
        l10.config(bg = 'purple')
        l10.place(x = 220 ,y = 190)
        self.e9 = tk.Entry(self)
        self.e9.place(x = 295 ,y = 190)
        l11 = tk.Label(self ,text = 'password :' ,font = ('Helvetica' ,10))
        l11.config(bg = 'purple')
        l11.place(x = 220 ,y = 220)
        self.e10 = tk.Entry(self)
        self.e10.place(x = 295 ,y = 220)
        l12 = tk.Label(self ,text = 'illness :' ,font = ('Helvetica' ,10))
        l12.config(bg = 'purple')
        l12.place(x = 220 ,y = 250)
        self.e11 = tk.Entry(self)
        self.e11.place(x = 295 ,y = 250)
        b1 = tk.Button(self ,text = 'save' ,width = 16 ,command = self.savep)
        b1.place(x = 180 ,y = 310)
        self.list1 = tk.Listbox(self ,width = 30 ,height = 10)
        self.list1.place(x = 150,y = 350)
        
    def savep(self):
        nationalId = self.e1.get()
        firstName = self.e2.get()
        lastName = self.e3.get()
        age = self.e4.get()
        sex = self.e5.get()
        email = self.e6.get()
        phone = self.e7.get()
        address = self.e8.get()
        city = self.e9.get()
        password = self.e10.get()
        illnes = self.e11.get()
        dname = random.choice(doctorlist2)
        nname = random.choice(nurselist2)
        pyment = random.randint(0 ,1000)
        p = Patient(nationalId ,firstName ,lastName ,age ,sex ,email ,phone ,address ,city , 
                        password, illnes, dname ,nname ,pyment)
        plist.add_p(p)
        plist2.append(p)
        self.list1.insert(0 ,nationalId ,str('patient registerd'))
        self.list1.insert(0 ,dname)
        self.list1.insert(0 ,nname)
        self.list1.insert(0 ,pyment)
######################################################################################
if __name__ == "__main__":
    app = HospitalApp()
    app.mainloop()