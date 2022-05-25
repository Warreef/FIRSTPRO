import sqlite3
import tkinter
import tkinter as tk
from tkinter import ttk, messagebox, END, filedialog as fd
import csv
import re

#IF NOT EXISTS

DB = sqlite3.connect("Tawaklna.db")
DB.execute(''' Create table IF NOT EXISTS PERSON
(ID_Number    CHAR(10)     PRIMARY KEY,
FirstName     CHAR (20)    NOT NULL,
LastName      CHAR (30)    NOT NULL,
Phone_Number  CHAR(15)     NOT NULL,
Gender        CHAR (6)     NOT NULL,
DateOfBirth   CHAR (10)    NOT NULL,
Num_doses     INT(5)       NOT NULL); ''')

DB.execute('''Create table IF NOT EXISTS DOSE 
(Shot_id      INTEGER PRIMARY KEY AUTOINCREMENT,
Shots         int(5)       NOT NULL,
Type0fVaccine CHAR (12)    NOT NULL,
DateOfDose    CHAR (10)    NOT NULL, 
TimeOfDose    CHAR (10)    NOT NULL,
ID_Number     CHAR (10)    NOT NULL,
FOREIGN KEY(ID_Number) REFERENCES PERSON(ID_Number));''')

DB.commit()
DB.close()
class GUI:
    def __init__(self):
        self.app = tk.Tk()
        self.app.title("Mini Tawakkalna")
        self.app.iconbitmap(r'C:\Users\bbash\Downloads\icontwlogo.ico')

        # TAP
        self.tap1 = ttk.Notebook(self.app)
        self.tap1.pack(pady=15, expand=True)

        # ID & NAME
        self.mainFrame = tk.Frame(self.app)
        self.lableID = tk.LabelFrame(self.mainFrame, text='PERSONAL INFORMATION')
        self.frameID = tk.Frame(self.lableID)
        self.labelTopID = tk.Label(self.frameID, text= 'ID')
        self.cbID = tk.Entry(self.frameID, width='15')
        self.lableTopFName = tk.Label(self.frameID, text='First name')
        self.cbFN = tk.Entry(self.frameID, width='10')
        self.lableTopLName = tk.Label(self.frameID, text='Last name')
        self.cbLN = tk.Entry(self.frameID, width='10')

        # Gender
        self.labelFS = tk.LabelFrame(self.mainFrame, text="Your Gender")
        self.frameS = tk.Frame(self.labelFS)
        self.labelTop0 = tk.Label(self.frameS, text='Gender')
        six = ('Female', 'Male')
        selected_six = tk.StringVar()
        self.cbs = ttk.Combobox(self.frameS, textvariable=selected_six, width=8)
        self.cbs['values'] = six

        # BIRTHDATE
        self.labelFD = tk.LabelFrame(self.mainFrame, text="Birth date information")
        self.frameD = tk.Frame(self.labelFD)
        self.labelTop1 = tk.Label(self.frameD, text="Day")
        days = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10',
                '11', '12', '13', '14', '15', '16', '17', '18', '19', '20',
                '21', '22', '23', '24', '25', '26', '27', '28', '29', '30', '31')
        selected_day = tk.StringVar()
        self.cb = ttk.Combobox(self.frameD, textvariable=selected_day, width=5)
        self.cb['values'] = days
        self.cb.current(15)
        self.labelTop2 = tk.Label(self.frameD, text="/ Month")
        months = ('01', '02', '03', '04', '05', '06', '07', '08', '09', '10', '11', '12')
        selected_month = tk.StringVar()
        self.cb2 = ttk.Combobox(self.frameD, textvariable=selected_month, width=5)
        self.cb2['values'] = months
        self.cb2.current(5)
        self.labelTop3 = tk.Label(self.frameD, text='/ Year')
        var = tk.StringVar(self.labelTop3)
        var.set("2001")
        self.cb3 = tk.Spinbox(self.labelTop3, from_=1900, to=2003, textvariable=var)

        # VACCINE
        self.labelFV = tk.LabelFrame(self.mainFrame, text="VACCINE")
        self.frameV = tk.Frame(self.labelFV)
        self.labelTop5 = tk.Label(self.frameV, text='Type')
        vac = ('Pfizer', 'AstraZeneca', 'Moderna', 'J&J')
        selected_vac = tk.StringVar()
        self.cbV = ttk.Combobox(self.frameV, textvariable=selected_vac, width=18)
        self.cbV['values'] = vac
        self.labelTop55 = tk.Label(self.frameV, text='Dose')
        vacNum = ('1', '2')
        vacN = tk.StringVar()
        self.cbVN = ttk.Combobox(self.frameV, textvariable=vacN, width=5)
        self.cbVN['values'] = vacNum
        self.cbVN.current(0)

        # DATE & TIME
        self.labelFDT = tk.LabelFrame(self.mainFrame, text="DATE OF VAC")
        self.frameDT = tk.Frame(self.labelFDT)
        self.labelTop6 = tk.Label(self.frameDT, text="Day")
        day_vac = tk.StringVar()
        self.cbT = ttk.Combobox(self.frameDT, textvariable=day_vac, width=5)
        self.cbT['values'] = days
        self.cbT.current(0)
        self.labelTop7 = tk.Label(self.frameDT, text="/ Month")
        month_vac = tk.StringVar()
        self.cb2T = ttk.Combobox(self.frameDT, textvariable=month_vac, width=5)
        self.cb2T['values'] = months
        self.cb2T.current(0)
        self.labelTop8 = tk.Label(self.frameDT, text='/ Year')
        self.cb3T = tk.Spinbox(self.labelTop8, from_=2019, to=2050)
        self.frameVT = tk.Frame(self.labelFDT)
        self.labelTopVT = tk.Label(self.frameVT, text='Time')
        hr = ('1', '2', '3', '5', '6', '7', '8', '9', '10', '11', '12')
        selected_hr = tk.StringVar()
        self.cbH = ttk.Combobox(self.frameVT, textvariable=selected_hr, width=5)
        self.cbH['values'] = hr
        self.cbH.current(10)
        self.labelTopVTT = tk.Label(self.frameVT, text=':')
        min = ('00', '15', '30', '45')
        selected_min = tk.StringVar()
        self.cbM = ttk.Combobox(self.frameVT, textvariable=selected_min, width=5)
        self.cbM['values'] = min
        self.cbM.current(0)
        dayP = ('AM', 'PM')
        selected_dp = tk.StringVar()
        self.cbdp = ttk.Combobox(self.frameVT, textvariable=selected_dp, width=5)
        self.cbdp['values'] = dayP
        self.cbdp.current(0)

        # PHONE NUMBER
        self.labelFP = tk.LabelFrame(self.mainFrame, text="Phone")
        self.frameP = tk.Frame(self.labelFP)
        self.labelTop4 = tk.Label(self.frameP, text='Number')
        self.cb4 = tk.Entry(self.frameP, width='15')

        # SUBMIT
        self.sub_button = tk.Button(self.mainFrame, text='Submit', command=self.action)

        # TAP2
        self.mainFrame2 = tk.LabelFrame(self.app, text='YOUR STATUS')
        self.frame2 = tk.Frame(self.mainFrame2)
        self.lableId2 = tk.Label(self.frame2, text='ID')
        self.cbID2 = tk.Entry(self.frame2, width='15')
        self.status = tk.StringVar()
        self.status_label = tk.Label(self.frame2, textvariable=self.status, font=('Arial', 20, 'bold'))
        self.status.set("")
        self.default = r'C:\Users\bbash\Downloads\iloveimg-resized\icontwlogo.png'
        self.yellow = r'C:\Users\bbash\Downloads\iloveimg-resized\ImmuneYellow-01.png'
        self.green = r'C:\Users\bbash\Downloads\iloveimg-resized\ImmuneGreen-01.png'
        self.red = r'C:\Users\bbash\Downloads\iloveimg-resized\ImmuneRed-01.png'

        self.canvas = tk.Canvas(self.frame2, width=300, heigh=300, bg="white")
        self.img = self.default
        self.vaccinated_img = tk.PhotoImage(file=self.img)
        self.canvas.create_image(50, 50, anchor=tkinter.NW, image=self.vaccinated_img)
        self.canvas.pack(fill='both', expand='yes', pady='30', padx='30')

        # Check
        self.check_button = tk.Button(self.frame2, text='Check', command=self.immune)
        self.reset_button = tk.Button(self.frame2, text='Reset', command=self.reset)

        # TAP3
        self.mainFrame3 = tk.LabelFrame(self.app, text='FILES')
        self.frameM3 = tk.Frame(self.mainFrame3)

        self.import_button = tk.Button(self.mainFrame3, text='Import', command=self.importFile)
        self.export_button = tk.Button(self.mainFrame3, text='Export', command=self.exportFile)

        # PACK
        self.labelTopID.pack(side='left', pady='10', padx='5')
        self.cbID.pack(side='left', padx='5')
        self.lableTopFName.pack(side='left', pady='10', padx='5')
        self.cbFN.pack(side='left', padx='5')
        self.lableTopLName.pack(side='left', pady='10', padx='5')
        self.cbLN.pack(side='left', padx='5')
        self.labelTop0.pack(side='left', pady='10', padx='5')
        self.cbs.pack(side='left', padx='5')
        self.labelTop1.pack(side='left', pady='10', padx='5')
        self.cb.pack(side='left', padx='5')
        self.labelTop2.pack(side='left', pady='10', padx='5')
        self.cb2.pack(side='left', padx='5')
        self.labelTop3.pack(side='left', pady='10', padx='5')
        self.cb3.pack(side='left', padx='5')
        self.labelTop5.pack(side='left', pady='10', padx='5')
        self.cbV.pack(side='left', padx='5')
        self.labelTop55.pack(side='left', pady='10', padx='5')
        self.cbVN.pack(side='left', padx='5')
        self.labelTop6.pack(side='left', pady='10', padx='5')
        self.cbT.pack(side='left', padx='5')
        self.labelTop7.pack(side='left', pady='10', padx='5')
        self.cb2T.pack(side='left', padx='5')
        self.labelTop8.pack(side='left', pady='10', padx='5')
        self.cb3T.pack(side='left', padx='5')
        self.labelTopVT.pack(side='left', pady='10', padx='5')
        self.cbH.pack(side='left', padx='5')
        self.labelTopVTT.pack(side='left')
        self.cbM.pack(side='left', padx='5')
        self.cbdp.pack(side='left', padx='5')
        self.labelTop4.pack(side='left', pady='10', padx='5')
        self.cb4.pack(side='left', padx='5')
        self.sub_button.pack(side='bottom')
        self.status_label.pack(side='top', pady='5', padx='5')
        self.lableId2.pack(side='left', pady='10', padx='5')
        self.cbID2.pack(side='left', padx='5')
        self.check_button.pack(side='left', padx='5')
        self.reset_button.pack(side='left', padx='5')
        self.import_button.pack(side='bottom')
        self.export_button.pack(side='bottom')
        self.frameID.pack()
        self.lableID.pack(fill='x')
        self.frameS.pack()
        self.labelFS.pack(fill='x')
        self.frameD.pack()
        self.labelFD.pack(fill='x')
        self.frameV.pack()
        self.labelFV.pack(fill='x')
        self.frameDT.pack()
        self.frameVT.pack()
        self.labelFDT.pack(fill='x')
        self.frameP.pack()
        self.labelFP.pack(fill='x')
        self.frameID.pack()
        self.frame2.pack()
        self.frameM3.pack()

        # TAP
        self.tap1.add(self.mainFrame, text='Check-In')
        self.tap1.add(self.mainFrame2, text='Immunity Check')
        self.tap1.add(self.mainFrame3, text='Import & Export')
        self.app.mainloop()


    def action(self):
        data_base = sqlite3.connect("Tawaklna.db")
        try:
            # VALIDATION
            # Tab no. 1
            # ID
            ID_Num = str(self.cbID.get())
            reg = "^[0-9]{10}$"
            pat = re.compile(reg)
            x = re.search(pat, ID_Num)
            if not x:
                ID_Num = ''
                messagebox.showinfo("ID Number error!", "Re-enter an ID number properly\rthat consists of 10 digits")
            # NAME
            firstname = str(self.cbFN.get())
            lastname = str(self.cbLN.get())
            # VACCINE
            typeOFvaccine = str(self.cbV.get())
            # SHOTS
            shot = int(self.cbVN.get())
            # DATE of dose
            day = str(self.cbT.get())
            month = str(self.cb2T.get())
            year = str(self.cb3T.get())
            DateOFdose = day + '/' + month + '/' + year
            # TIME of dose
            hour = str(self.cbH.get())
            minute = str(self.cbM.get())
            timeOfDay = str(self.cbdp.get())
            TimeOFdose = hour + ':' + minute + ' ' + timeOfDay
            # Phone number
            phoneNum = str(self.cb4.get())
            reg2 = "^(05)[0-9]{8}$"
            pat2 = re.compile(reg2)
            y = re.search(pat2, phoneNum)
            if not y:
                phoneNum = ''
                messagebox.showinfo("Phone Number error!", "Re-enter an phone number properly\rthat "
                                                           "consists of 10 digits and starts with \'05\'")
            # Gender
            gender = str(self.cbs.get())
            # BIRTH DATE
            bday = str(self.cb.get())
            bmonth = str(self.cb2.get())
            byear = str(self.cb3.get())
            if 1900 > int(byear) or int(byear) > 2003:
                byear = ''
                messagebox.showinfo("Year Of Birth Error", "Year Of Birth is out of range (1900-2003)"
                                                           "\rPlease enter a valid value")
            else:
                BirthDate = bday + "/" + bmonth + "/" + byear

        except:
            messagebox.showinfo("ADD MISSION FAILED", "Due to incorrect or incompelte inputs,"
                                                      "\rplease review your information and enter it correctly")

        try:
            # SHOTS
            # INSERTION
            shot = int(self.cbVN.get())
            found_id = data_base.execute(f"SELECT ID_Number FROM PERSON WHERE ID_Number = {ID_Num}")
            if len(found_id.fetchall()) == 0:
                data_base.execute(
                    "INSERT INTO PERSON (ID_Number, FirstName, LastName, Phone_Number, Gender,"
                    "DateOfBirth, Num_doses) VALUES (?, ?, ?, ?, ?, ?, ?)",
                    (str(ID_Num), str(firstname), str(lastname), int(phoneNum), str(gender), str(BirthDate), int(shot)))
                data_base.execute(
                    "INSERT INTO DOSE (ID_Number, Type0fVaccine, Shots, DateOfDose, TimeOfDose) VALUES (?, ?, ?, ?, ?)",
                    (str(ID_Num), str(typeOFvaccine), int(shot), str(DateOFdose), str(TimeOFdose)))

                self.clear_text(self.cbID)
                self.clear_text(self.cbFN)
                self.clear_text(self.cbLN)
                self.clear_text(self.cbs)
                self.cb.current(15)
                self.cb2.current(5)
                self.clear_text(self.cb3)
                self.clear_text(self.cbV)
                self.cbVN.current(0)
                self.cbT.current(0)
                self.cb2T.current(0)
                self.clear_text(self.cb3T)
                self.cbH.current(10)
                self.cbM.current(0)
                self.cbdp.current(0)
                self.clear_text(self.cb4)

                messagebox.showinfo("ADD MISSION", "SUCCESSFUL")

            else:
                numd = data_base.execute(f"SELECT Num_doses FROM PERSON WHERE ID_Number = {ID_Num}")
                numd = numd.fetchone()[0]
                if numd != shot and numd < shot:
                    data_base.execute(f"UPDATE PERSON SET Num_doses = {shot} WHERE ID_Number = {ID_Num}")
                    data_base.execute(
                        "INSERT INTO DOSE (ID_Number, Type0fVaccine, Shots, DateOfDose, TimeOfDose) VALUES (?, ?, ?, "
                        "?, ?)",
                        (str(ID_Num), str(typeOFvaccine), int(shot), str(DateOFdose), str(TimeOFdose)))

                    messagebox.showinfo("ADD MISSION", "SUCCESSFUL")

                    self.clear_text(self.cbID)
                    self.clear_text(self.cbFN)
                    self.clear_text(self.cbLN)
                    self.clear_text(self.cbs)
                    self.cb.current(15)
                    self.cb2.current(5)
                    self.clear_text(self.cb3)
                    self.clear_text(self.cbV)
                    self.cbVN.current(0)
                    self.cbT.current(0)
                    self.cb2T.current(0)
                    self.clear_text(self.cb3T)
                    self.cbH.current(10)
                    self.cbM.current(0)
                    self.cbdp.current(0)
                    self.clear_text(self.cb4)
                elif numd == shot:
                    messagebox.showinfo("Number of doses error!",
                                        "You already submitted the same number of doses earlier")
                else:
                    messagebox.showinfo("UPDATE MISSION FAILED",
                                        "Due to incorrect input,\rplease review your information and enter it correctly")

            data_base.commit()
            data_base.close()

        except:
            messagebox.showinfo("ADD MISSION FAILED", "Due to incorrect inputs,\rplease review your information and "
                                                      "enter it correctly")

    def clear_text(self, text):
        text.delete(0, END)

    def immune(self):
        try:
            database = sqlite3.connect("Tawaklna.db")
            immune_id = self.cbID2.get()
            if len(immune_id) != 10:
                messagebox.showinfo("ID Number error!",
                                    "Re-enter an ID number properly\rthat consists of 10 digits")
            else:
                found_id = database.execute(f"SELECT ID_Number FROM PERSON WHERE ID_Number = {immune_id}")
                if len(found_id.fetchall()) == 0:
                    self.img = self.red
                    self.status.set("Unvaccinated")
                    messagebox.showinfo("You are Unvaccinated",
                                        "The id you've entered isn't registered in our system")
                else:
                    no_doses = database.execute(f"SELECT Num_doses FROM PERSON WHERE ID_Number = {immune_id}")
                    no_doses = no_doses.fetchone()[0]
                    if no_doses == 1:
                        self.img = self.yellow
                        self.status.set("Vaccinated")
                    elif no_doses == 2:
                        self.img = self.green
                        self.status.set("Fully Vaccinated")

                self.vaccinated_img = tk.PhotoImage(file=self.img)
                self.canvas.create_image(50, 50, anchor=tkinter.NW, image=self.vaccinated_img)
            database.commit()
            database.close()
        except:
            messagebox.showinfo("No input is entered!",
                                "Please re-enter an ID number properly\rthat consists of 10 digits")

    def reset(self):
        self.clear_text(self.cbID2)
        self.img = self.default
        self.vaccinated_img = tk.PhotoImage(file=self.img)
        self.canvas.create_image(50, 50, anchor=tkinter.NW, image=self.vaccinated_img)
        self.status.set("")

    def importFile(self):
        try:
            database = sqlite3.connect("Tawaklna.db")
            name = fd.askopenfilename()
            file_read = open(name)
            csvreader = csv.reader(file_read)
            id_list = []
            for row in csvreader:
                if row[3] not in id_list:
                    database.execute(
                        "INSERT INTO PERSON (ID_Number, FirstName, LastName, Phone_Number, Gender, DateOfBirth,"
                        "Num_doses) VALUES (?, ?, ?, ?, ?, ?, ?)",
                        (str(row[3]), str(row[0]), str(row[1]), int(row[8]), str(row[2]), str(row[4]), int(1)))
                    id_list.append(str(row[3]))
                database.execute(
                    "INSERT INTO DOSE (Type0fVaccine, DateOfDose, TimeOfDose, Shots, ID_Number) VALUES (?, ?, ?, ?, ?)",
                    (str(row[5]), str(row[6]), str(row[7]), 1, str(row[3])))

            database.commit()
            database.close()
            file_read.close()

            messagebox.showinfo("UPDATE MISSION SUCCESSFUL", "The database of our system is updated correctly")
        except:
            messagebox.showinfo("UPDATE MISSION FAILED", "The database of our system isn't updated\rdue to existing "
                                                         "ID numbers that are already registered in the system")

    def exportFile(self):
        try:
            database = sqlite3.connect("Tawaklna.db")
            exported_file = open("MiniTawakkalna.csv", 'w')
            csvwriter = csv.writer(exported_file, lineterminator = "\n")
            peopleInfo = database.execute('''SELECT PERSON.FirstName, PERSON.LastName, PERSON.Gender, DOSE.Type0fVaccine,
                                                    PERSON.ID_Number,
                                                    PERSON.DateOfBirth, DOSE.DateOfDose, DOSE.TimeOfDose, PERSON.Phone_Number 
                                                    FROM DOSE INNER JOIN PERSON ON PERSON.ID_Number = DOSE.ID_Number;''')
            data = peopleInfo.fetchall()
            csvwriter.writerow(["First Name", "Last Name", "Gender", "Vaccine Type", "ID Number", "Birth Year",
                                "Dose Date", "Dose Time", "Phone Number"])
            for row in data:
                row = list(row)
                row[5] = row[5][-4:]
                csvwriter.writerow(row)

            database.commit()
            database.close()
            exported_file.close()
            messagebox.showinfo("SUCCESSFUL EXPORTATION", "The database of our system is exported in CSV file")

        except:
            messagebox.showinfo("UNSUCSESSSFUL EXPORTATION", "The database of our system couldn't be exported in CSV"
                                                             " file\rdue to unmanageable errors")


gui = GUI()