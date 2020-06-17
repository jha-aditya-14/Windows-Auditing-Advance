from tkinter import *
from tkinter import messagebox as tkmessagebox
import pickle, os
import subprocess
import re
import win32com.shell.shell as shell
import time
import tkinter as tk
from PIL import ImageTk,Image


class win1(Tk):
    
    new = None

    def __init__(self, *arg):
        Tk.__init__(self, *arg)
        lab1 = Label(self, text='Welcome to', font=('Comic Sans MS', 35), fg='red', width=70,bg='#000000' )
        lab1.pack()
        lab2 = Label(self, text='OASIS', font=('Comic Sans MS', 50, 'bold'), fg='#994483', width=70, bg='#000000' )
        lab2.pack()
        lab1 = Label(self, text='Creators---                    ', font=('Times', 35, 'bold'), fg='green', width=70,bg='#000000' ,
                     justify='right')
        lab1.pack()
        lab1 = Label(self, text='  Aditya Jha and Gaurav Kumar Gupta ', font=('Verdana', 20), fg='lightgreen', width=81, bg='#000000' )
        lab1.pack()

        bottom = Frame()
        bottom.pack()
        but = Button(bottom, text='NEW USER', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=24,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open1)
        but.pack(side='left')
        but = Button(bottom, text='EXISTING USER', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=24
                     , cursor='hand2',
                     activebackground='#86cc64', command=self.open2)
        but.pack(side='right')

    def open1(self, *arg):
        self.destroy()
        win2().mainloop()

    def open2(self, *arg):
        self.destroy()
        root = Tk()
        clas = login(root)
        win1.new = clas.user
        existing(win1.new).mainloop()


class win2(Tk):

    def __init__(self, *arg):
        Tk.__init__(self, *arg)

        self.lab1 = Label(text='ENTER YOUR DETAILS FOR NEW ID', font=('Times', 17, 'bold'), fg='#15633b')
        self.lab1.grid(row=1, column=1, columnspan=2)

        self.lab2 = Label(text='Username', font=('Times', 17), fg='#14b863')
        self.lab2.grid(row=2, column=1)
        self.txt1 = Entry(bd=4, width=20, font=('Verdana', 12))
        self.txt1.grid(row=2, column=2)

        self.lab3 = Label(text='Password', font=('Times', 17), fg='#14b863')
        self.lab3.grid(row=3, column=1)
        self.txt2 = Entry(bd=5, width=20, font=('Verdana', 12), show='*')
        self.txt2.grid(row=3, column=2)

        self.lab4 = Label(text='Contact No.', font=('Times', 17), fg='#14b863')
        self.lab4.grid(row=4, column=1)
        self.txt3 = Entry(bd=5, width=20, font=('Verdana', 12))
        self.txt3.grid(row=4, column=2)

        self.lab5 = Label(text='City', font=('Times', 17), fg='#14b863')
        self.lab5.grid(row=5, column=1)
        self.txt4 = Entry(bd=5, width=20, font=('Verdana', 12))
        self.txt4.grid(row=5, column=2)

        self.lab6 = Label(text='Email', font=('Times', 17), fg='#14b863')
        self.lab6.grid(row=6, column=1)
        self.txt5 = Entry(bd=5, width=20, font=('Verdana', 12))
        self.txt5.grid(row=6, column=2)

        self.txt1.bind('<Return>', self.call2)
        self.txt2.bind('<Return>', self.call3)
        self.txt3.bind('<Return>', self.call4)
        self.txt4.bind('<Return>', self.call5)
        self.txt5.bind('<Return>', self.call6)

        self.but = Button(self, text='BACK', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.back)
        self.but.grid(row=7, column=1)
        self.but = Button(self, text='DONE', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.done)
        self.but.grid(row=7, column=2)
        self.txt1.focus_set()

    def call2(self, *arg):
        return self.txt2.focus_set()

    def call3(self, *arg):
        return self.txt3.focus_set()

    def call4(self, *arg):
        return self.txt4.focus_set()

    def call5(self, *arg):
        return self.txt5.focus_set()

    def call6(self, *arg):
        return self.but.invoke()

    def done(self, *arg):
        self.user = self.txt1.get()
        if self.user == '':
            return tkmessagebox.showinfo('Error', 'Enter a username')
        self.password = self.txt2.get()
        if self.password == '':
            return tkmessagebox.showinfo('Error', 'Enter a password')
        self.contact = self.txt3.get()
        if self.contact == '':
            return tkmessagebox.showinfo('Error', 'Enter a contact')
        try:
            tmp = self.contact
            int(tmp)
        except ValueError:
            return tkmessagebox.showinfo('Error', 'Contact No. Should Be Integer')
        self.city = self.txt4.get()
        if self.user == '':
            return tkmessagebox.showinfo('Error', 'Enter a city')
        self.email = self.txt5.get()
        if self.user == '':
            return tkmessagebox.showinfo('Error', 'Enter an email')
        f = open('users.log', 'rb')
        while True:
            try:
                user = pickle.load(f)
                if user.name == self.user:
                    return tkmessagebox.showinfo('Error', 'Username Already Exists')

            except EOFError:
                f.close()
                break

        f = open('users.log', 'ab')
        new = new_file(name=self.user, password=self.password, contact=self.contact, city=self.city, email=self.email)
        pickle.dump(new, f)
        f.close()
        self.back()

    def back(self):
        self.destroy()
        win1()


class Password_Policy(Tk):

    def __init__(self):

        Tk.__init__(self)


        self.di = {
            'MinimumPasswordAge': 'between 1 and 998',
            'MaximumPasswordAge': 'between 1 and 999, or 0 to specify that passwords never expire',
            'MinimumPasswordLength': 'between 1 and 20 characters, or 0 to specify no password.',
            'PasswordComplexity': 'Enable (for better security)',  # disabled
            'PasswordHistorySize': 'between 0 and 24 passwords',
            'LockoutBadCount': 'between 0 and 999 or 0 to specify that account will never be locked out',
            'RequireLogonToChangePassword': 'Option No Longer Exists in new version',
            'ForceLogoffWhenHourExpire': 'non zero (enable for better security)',
            'NewAdministratorName': '"Administrator"',
            'NewGuestName': '"Guest"',
            'ClearTextPassword': 'Non Zero (Provides Encryption)',
            'LSAAnonymousNameLookup': '0 (Restricts Anonymous LSA)',
            'EnableAdminAccount': '0 (preferred disable)',
            'EnableGuestAccount': '0 (preferred disable)'}

        self.labp1 = Label(text='Please Enter File Name', font=('Times', 17, 'bold'), fg='#006400', bg='#000000')
        self.labp1.grid(row=1, column=1, columnspan=2)
        self.txtp1 = Entry(bd=4, width=18, font=('Verdana', 12))
        self.txtp1.grid(row=2, column=2)

        self.but = Button(self, text='BACK', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.back)
        self.but.grid(row=7, column=1)
        self.but = Button(self, text='DONE', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.donep)
        self.but.grid(row=7, column=2)

        self.txtp1.bind('<Return>', self.callp1)

    def callp1(self, *arg):
        return self.txtp1.focus_set()

    def callp2(self, *arg):
        return self.txtp2.focus_set()

    def callp3(self, *arg):
        return self.txtp3.focus_set()

    def donep(self, *arg):
        self.name1 = str(self.txtp1)
        self.ls = []
        # st=str()
        self.counter = int(0)
        self.startpos = 84  # Bytes to seek before reading password policy
        self.lno = 13  # lines to be read under password policy
        self.path = 'C:\\All1\\' + self.name1 + '.txt'

        self.commands = str(r'SecEdit.exe /export /cfg ' + self.path)
        #tkinter.print(self.commands)
        #return tkmessagebox.showinfo('commands', self.commands)

        try:
            self.command1 = 'mkdir C:\\All1'
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + self.command1)
        except:
            pass
        try:
            shell.ShellExecuteEx(lpVerb='runas', lpFile='cmd.exe', lpParameters='/c ' + self.commands)
        except:
            T='Not able to get administrative privalages\nProgram is closing in next five seconds '
            return tkmessagebox.showinfo('ERROR!', T)
            exit()
            for a in range(5):
                time.sleep(1)
                #Tkprint('.', end=' ')

        for a in range(5):
            time.sleep(1)

        with open(self.path, 'a+', encoding='utf-16-le') as file:
            file.seek(self.startpos, 0)
            while self.counter <= self.lno:
                line = file.readline().strip()
                if line != '':
                    self.ls.append(line.split(' = '))
                    self.counter += 1
        self.ls = dict(self.ls)

#############################################################################################################

        #print(tkmessagebox.showinfo('Data File', self.ls))


        #print('|{:_^30}|{:_^16}|{:_^72}|'.format('Keys', 'UserValues', 'RecommendedValues'))


        self.ab = []
        self.ab.append('|{:_^28}|{:_^16}|{:_^74}|'.format('Keys', 'UserValues', 'RecommendedValues'))
        for a in self.di.keys():
            self.ab.append('|{:^30}|{:^16}|{:<72}|,'.format(a, self.ls[a], self.di[a]))
        T = tk.Text(self, height=200, width=126,bg='#000000', fg='#006400')
        T.grid(row=1, column=1)
        T.insert(tk.END, self.ab)

######################################################################################
        tkmessagebox.showinfo('Options for its "Explanation given below"',
                              '1 : MinimumPasswordAge\n2: MaximumPasswordAge\n3: MinimumPasswordLength\n4: PasswordComplexity\n5: PasswordHistorySize\n6: LockoutBadCount\n'
                              '7: RequireLogonToChangePassword\n8: ForceLogoffWhenHourExpire\n9: NewAdministratorName\n10: NewGuestName\n11: ClearTextPassword\n12: LSAAnonymousNameLookup\n13: EnableAdminAccount\n14: EnableGuestAccount')
        #T1 = tk.Text(self, height=200, width=126,sticky="nsew", padx=2, pady=2)
        #T1.grid(row=1, column=1)
        #T1.insert(tk.END, )
        tkmessagebox.showinfo('Explaination of First 3 Password Policies, Enter ok for further policies', '1.Minimum password age\n'
                                      'This security setting determines the period of time (in days) that a password must be used before the user can change it.'
                                      'You can set a value between 1 and 998 days, or you can allow changes immediately by setting the number of days to 0.'
                                      'The minimum password age must be less than the Maximum password age, unless the maximum password age is set to 0, indicating that passwords will never expire.'
                                      'If the maximum password age is set to 0   the minimum password age can be set to any value between 0 and 998.'
                                      'Configure the minimum password age to be more than 0 if you want Enforce password history to be effective.'
                                      'Without a minimum password age, users can cycle through passwords repeatedly until they get to an old favorite.'
                                      'The default setting does not follow this recommendation, so that an administrator can specify a password for a user and then require the user to change the administrator-defined password when the user  logs on.'
                                      'If the password history is set to 0, the user does not have to choose a new password.'
                                      '\nFor this reason,Enforce password history is set to 1 by default.\n'
                                      'Default:\n'
                                      '1 on domain controllers   0 on stand-alone servers'
                                      '\nNote:\n'
                                      'By default, member computers follow the configuration of their domain controllers.\n\n\n\n\n'
                                      '2.Maximum password age\n'
                                      'This security setting determines the period of time (in days) that a password can be used before the system requires the user to change it.'
                                      'You can set passwords to expire after a number of days between 1 and 999, or you can specify that passwords never expire by setting the number of days to 0.'
                                      'If the maximum password age is between 1 and 999 days, the Minimum password age must be less than the maximum password age.'
                                      'If the maximum password age is set to 0, the minimum password age can be any value between 0 and 998 days.'
                                      'Note:\n'
                                      'It is a security best practice to have passwords expire every 30 to 90 days, depending on your environment. This way, an attacker has a limited amount of time in which to crack a users password and have access to your network resources.'
                                      '\nDefault: 42.\n\n\n\n'
                                      '3.Minimum password length\nThis security setting determines the least number of characters that a password for a user account may contain.You can set a value of between 1 and 20 characters, or you can establish that no password is required by setting the number of characters to 0.'
                                      '\nDefault:\n'
                                      '7 on domain controllers. 0 on stand-alone servers.\n'
                                      'Note:\n'
                                      'By default, member computers follow the configuration of their domain controllers.\n\n\n\n')
        tkmessagebox.showinfo('Explaination of 4-8 Password Policy, Enter ok for further policies','4.Password Complexity \n'
                         'This security setting determines whether passwords must meet complexity requirements.'
                         'If this policy is enabled, passwords must meet the following minimum requirements: contain the users account name or parts of the users full name that exceed two consecutive characters.'
                         'Be at least six characters in length.'
                         'Contain characters from three of the following four categories:\n'
                         '1 English uppercase characters (A through Z)\n'
                         '2 English lowercase characters (a through z)\n'
                         '3 Base 10 digits (0 through 9)\n'
                         'Non-alphabetic characters (for example, !, $, #, %) Complexity requirements are enforced when passwords are changed or created.\n'
                         'Default:\nEnabled on domain controllers.  Disabled on stand-alone servers.\n'
                         'Note:\n By default, member computers follow the configuration of their domain controllers.\n'
                         'Enforce password history\n'
                         'This security setting determines the number of unique new passwords that have to be associated with a user account before an old password can be reused.  '
                         'The value must be between 0 and 24 passwords. '
                         'This policy enables administrators to enhance security by ensuring that old passwords are not reused continually.  Default:24 on domain controllers 0 on stand-alone servers.'
                         'Note: '
                         'By default, member computers follow the configuration of their domain controllers.'
                         'To maintain the effectiveness of the password history, do not allow passwords to be changed immediately after they were just changed by also enabling the Minimum password age security policy setting.'
                         'For information about the minimum password age security policy setting, see Minimum password age.'
                         '\n\n\n\n5.Password History Size\nThis security setting determines the number of unique new passwords that have to be associated with a user '
                         'account before an old password can be reused. The value must be between 0 and 24 passwords. '
                                                      'This policy enables administrators to enhance security by ensuring that old passwords are not reused continually.  '
                                                      'Default:24 on domain controllers 0 on stand-alone servers.\nNote:\nBy default, member computers follow the configuration'
                                                      ' of their domain controllers. To maintain the effectiveness of the password history, do not allow passwords to '
                                                      'be changed immediately after they were just changed by also enabling the Minimum password age security policy setting.'
                                                      'For information about the minimum password age security policy setting, see Minimum password age\n\n\n\n'
                         '6.Lock out BadCount\n'
                              'This security setting determines the number of failed logon attempts that causes a user account to be locked out.'
                              'A locked-out account cannot be used until it is reset by an administrator or until the lockout duration for the account has expired.'
                              'You can set a value between 0 and 999 failed logon attempts.If you set the value to 0, the account will never be locked out.'
                              'Failed password attempts against workstations or member servers that have been locked using either CTRL+ALT+DELETE or password-protected screen savers count as failed logon attempts.'
                              '\nDefault: 0.\n\n\n\n'
                         '7.Require Logon To Change Password\n'
                         'Windows ignores the RequireLogonToChangepassword setting.User Must Log On in Order to Change Password” Option No Longer Exists\n\n\n'
                         '8.Force Log off When Hour Expire\n'
                              'This setting specifies the name of the Administrator account on the local computer\n\n\n\n')


        tkmessagebox.showinfo('Explaination of 9-14 Policies',
                         '9.New Administrator Name\n'
                              'This setting specifies the name of the Administrator account on the local computer\n\n\n\n'
                         '10.NewGuestName\n'
                              'This setting specifies the name of the Guest account on the local computer\n\n\n\n'
                         '11.ClearTextPassword\n'
                              'Flag that indicates whether passwords MUST be stored by using reversible encryption. '
                              'This value MUST be between 0 and 2^16.A value of 0 indicates that the password is not stored using reversible encryption.'
                              'Any other valid value indicates that the password is stored with reversible encryption.'
                              'Use of this flag is not recommended.'
                              'This policy provides support for applications that use protocols that require knowledge of the users password for authentication purposes.'
                              'Storing passwords by using reversible encryption is essentially the same as storing plain-text versions of the passwords.\n\n\n\n'
                         '12.LSA Anonymous Name Lookup\n When enabled, this setting allows an anonymous user to query the local LSA policy.If the value element contains a nonzero value, the setting is enabled; otherwise, the setting is disabled.'
                         '\n\n\n\n13.EnableAdminAccount'
                              'This setting specifies whether the Administrator account on the local computer is enabled.'
                              'If the value element contains a nonzero value, the setting is enabled; otherwise, the setting is disabled.')

        tk.mainloop()
        self.back()


    def back(self):
        #self.destroy()
        win1()


class MsConfig(Tk):
    opt = 1

    def opt(self, esd):
        self.opt = opt
        self.opt = int(esd)

    def __init__(self, *arg):

        Tk.__init__(self, *arg)
        lab1 = Label(self, text='Msconfig', font=('Comic Sans MS', 50), fg='red', width=13, bg='#000000')
        lab1.pack()
        bottom = Frame()
        bottom.pack()
        but1 = Button(bottom, text='Service Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.service_info)
        but1.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but2 = Button(bottom, text='Startup Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.startup_info)
        but2.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but3 = Button(bottom, text='BIOS Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.bios_info)
        but3.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but4 = Button(bottom, text='User Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.useraccount_info)
        but4.grid(row=1, column=1)


        bottom = Frame()
        bottom.pack()
        but5 = Button(bottom, text='CPU Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.cpu_info)
        but5.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but6 = Button(bottom, text='Group Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.group_info)
        but6.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but7 = Button(bottom, text='OS Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.os_info)
        but7.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but8 = Button(bottom, text='SysAccount Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.sysaccount_info)
        but8.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but9 = Button(bottom, text='Process Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.process_info)
        but9.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but10 = Button(bottom, text=' Computer System Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.computersystem_info)
        but10.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but11 = Button(bottom, text='Net Info', font=('Courier', 10, 'bold'), fg='#436632', bg='#abcdef', width=80,
                      cursor='hand2',
                      activebackground='#86cc64', command=self.net_info)
        but11.grid(row=1, column=1)

        bottom = Frame()
        bottom.pack()
        but12 = Button(bottom, text='Back', font=('Courier', 10, 'bold'), fg='#006400', bg='#000000', width=30,
                       cursor='hand2',
                       activebackground='#86cc64', command=self.back)
        but12.grid(row=1, column=1)



    def back(self):
        # self.destroy()
        win1()

    def simplify_G(self, a, list_no=0, value_no=0, no=0, rm_ls_no=0, rm_ls_keys=[], rm_ls2_no=0, rm_ls2_keys=[]):
        ls1 = a.split(' \n\n')
        ls1.remove('\n')
        # except:
        #   pass
        ls2 = list()
        ls2.append(re.findall('\S+', ls1[0]))
        ls2.append(re.findall('\S+', ls1[1]))
        print(tkmessagebox.showinfo('Info',ls2))
        if list_no != 0:
            if list_no == 2:
                counter = 0
                while counter < no:
                    ls2[0].insert(value_no, ' ' * (counter + 1))
                    counter += 1
            if list_no == 1:
                counter = 0
                while counter < no:
                    ls2[1].insert(value_no, ' ' * (counter + 1))
                    counter += 1
        if rm_ls_no != 0:
            for k in rm_ls_keys:
                ls2[0].remove(k)
        if rm_ls2_no != 0:
            for k in rm_ls2_keys:
                ls2[1].remove(k)
        ls1 = list(zip(ls2[0], ls2[1]))
        print(tkmessagebox.showinfo('Info',ls1))
        ls1 = dict(ls1)
        ab = []
        print('\n')
        for a in ls1.keys():
            ab.append('{0:30} {1}'.format(a, ls1[a]))

        T = tk.Text(self, height=200, width=126, bg='#000000', fg='#006400')
        T.pack()
        T.insert(tk.END, ab)

    def service_info(self):
        di = {1: 'Brief', 2: 'Config', 3: 'Status', 4: 'Control', 5: 'Default'}

        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic service list ' + di[opt]
        if opt == 2:
            command = 'wmic service get DesktopInteract,ErrorControl,Name,ServiceType,StartMode'
        if opt == 5:
            command = ' wmic service get name, processid, startmode, state, status, exitcode,servicetype /format: table'
        try:
            a = eval("subprocess.getoutput(command)")
            print(tkmessagebox.showinfo('Output',a))
        except:
            print(tkmessagebox.showinfo('ERROR',"Error \n Cannot proceed"))
        # a=(eval("subprocess.getoutput(' wmic service get name, processid, startmode, state, status, exitcode,servicetype /format: table')"))

    def startup_info(self):
        di = {1: 'Brief', 2: 'Default'}
        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic startup list ' + di[opt]
        if opt == 1:
            command = ' wmic startup get caption,user/format: table'
        if opt == 2:
            command = ' wmic startup get description,user,caption/format: table'
        try:
            a = eval("subprocess.getoutput(command)")
            print(tkmessagebox.showinfo('Info',a))
        except:
            print(tkmessagebox.showinfo('ERROR','"Error \n Cannot proceed"'))
        # print(eval("subprocess.getoutput('wmic startup get description,user,command/format: table')"))

    def bios_info(self):
        a = eval(
            "subprocess.getoutput('wmic BIOS get SMBIOSBIOSVersion, Manufacturer, Name, SerialNumber, Version, Status, SMBIOSPresent /format: table')")
        self.simplify_G(a)

    def useraccount_info(self):
        di = {1: 'Brief', 2: 'Writeable', 3: 'Status'}
        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic useraccount list ' + di[opt]
        if opt == 1:
            command = 'wmic useraccount get AccountType,Caption,Domain,Name,SID'
        if opt == 2:
            command = 'wmic useraccount get Disabled,Caption,Lockout,PasswordChangeable,PasswordExpires,PasswordRequired'
        try:
            a = eval("subprocess.getoutput(command)")
            print(tkmessagebox.showinfo('Output',a))
        except:
            print(tkmessagebox.showinfo('ERROR','"Error \n Cannot proceed"'))

    def cpu_info(self):
        di = {1: 'Brief', 2: 'Config', 3: 'Status', 4: 'Instance'}
        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic cpu list ' + di[opt]
        if opt == 1:
            command = 'wmic cpu get Caption,DeviceID,Manufacturer,MaxClockSpeed,Name'
        try:
            a = eval("subprocess.getoutput(command)")
            if opt == 2:
                self.simplify_G(a, rm_ls_no=1, rm_ls_keys=['L2CacheSpeed', 'Version', 'VoltageCaps'], rm_ls2_no=2,
                                rm_ls2_keys=['CPU', 'Socket', '-'])
            elif opt == 3:
                self.simplify_G(a, rm_ls_no=1,
                                rm_ls_keys=['ErrorCleared', 'ErrorDescription', 'LastErrorCode', 'LoadPercentage'])
            else:
                print(tkmessagebox.showinfo('Output', a))
        except:
            print(tkmessagebox.showinfo('ERROR',"Error \n Cannot proceed"))

    def group_info(self):
        di = {1: 'Brief', 2: 'Full', 3: 'Status', 4: 'Instance'}
        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic group list ' + di[opt]
        if opt == 2:
            command = 'wmic group get description,name /format:list'
        if opt == 4:
            command = 'wmic group get name,domain'
        try:
            a = eval("subprocess.getoutput(command)")
            if opt == 2:
                # print(a)
                a = a.split('\n\n\n\n')
                a = [s.replace('\n', '') for s in a]
                a = [s.split('Name=') for s in a]
                del a[0], a[-1]
                a = {s[1]: s[0].replace('Description=', '') for s in a}
                for s in a.keys():
                    print('\n{:30}\n{}'.format(s, a[s]), '\n')
            print(tkmessagebox.showinfo('Output', a))
        except:
            print(tkmessagebox.showinfo('ERROR',"Error \n Cannot proceed"))

    def os_info(self):
        di = {1: 'Brief', 2: 'Free', 3: 'Status'}
        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic os list ' + di[opt]
        try:
            a = eval("subprocess.getoutput(command)")
            if opt == 1:
                self.simplify_G(a, rm_ls_no=1, rm_ls_keys=['Organization'])
            if opt == 2:
                self.simplify_G(a, list_no=2, value_no=4, no=3)
            else:
                print(tkmessagebox.showinfo('\n', a))
        except:
            print(tkmessagebox.showinfo('ERROR',"Error \n Cannot proceed"))

    def sysaccount_info(self):
        di = {1: 'Brief', 2: 'Full', 3: 'Status', 4: 'instance'}
        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic sysaccount list ' + di[opt]
        if opt == 2:
            command = 'wmic sysaccount get Description,Domain,LocalAccount,Name,SID,SIDType,Status '
        try:
            a = eval("subprocess.getoutput(command)")
            print(tkmessagebox.showinfo('OUTPUT',a))
        except:
            print(tkmessagebox.showinfo("Error \n Cannot proceed"))

    def process_info(self):
        di = {1: 'Brief', 2: 'Io', 3: 'Memory', 4: 'Status'}
        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic process list ' + di[opt]
        try:
            a = eval("subprocess.getoutput(command)")
            print(tkmessagebox.showinfo('OUTPUT',a))
        except:
            print(tkmessagebox.showinfo('ERROR','"Error \n Cannot proceed"'))

    def computersystem_info(self):
        di = {1: 'Brief', 2: 'Power', 3: 'Status', 4: 'writeable'}
        print(tkmessagebox.showinfo('Following Options are available: ', di))
        opt = int(input("Please select an option: "))
        command = 'wmic computersystem list ' + di[opt]
        if di[opt] == 'writeable':
            command = 'wmic computersystem get AutomaticResetBootOption,CurrentTimeZone,EnableDaylightSavingsTime,Roles,Workgroup'
        try:
            a = eval("subprocess.getoutput(command)")
            if opt == 3:
                self.simplify_G(a, list_no=2, value_no=2, no=1)
            elif opt == 4:
                self.simplify_G(a, list_no=2, value_no=4, no=2)
            else:
                self.simplify_G(a)
        except:
            print(tkmessagebox.showinfo('ERROR','"Error \n Cannot proceed"'))
        if opt != 1:
            print(tkmessagebox.showinfo('OUTPUT',
                "\nNote:\n*Status = 2 represents 'not Implemented'\n*Status = 1 represents 'Enabled'\n*Status = 0 represents 'Disabled'"))

    def net_info(self):
        di = {1: 'ACCOUNTS', 2: 'COMPUTER', 3: 'CONFIG', 4: 'CONTINUE', 5: 'FILE', 6: 'GROUP', 7: 'HELP',
              8: 'LOCALGROUP', 9: 'PAUSE', 10: 'SESSION', 11: 'SHARE', 12: 'START', 13: 'STATISTICS', 14: 'STOP',
              15: 'TIME', 16: 'USE', 17: 'USER', 18: 'VIEW'}
        # di={1:'Brief',2:'Io',3:'Memory',4:'Status'}
        print(tkmessagebox.showinfo('Following Options are available: ') ) # ,di)
        ab = []
        for c in di.keys():
            ab.append('{:<3}: {:20}'.format(c, di[c]))

        T = tk.Text(self, height=200, width=126, bg='#000000', fg='#006400')
        T.pack()
        T.insert(tk.END, ab)

        opt = int(input("Please select an option: "))
        # command='net  '+di[opt]
        # if opt==2 or 5 or 4:
        command = 'net ' + di[opt] + ' /help'
        try:
            a = eval("subprocess.getoutput(command)")
            print(tkmessagebox.showinfo('OUTPUT', a))
        except:
            print(tkmessagebox.showinfo("Error \n Cannot proceed"))


class new_file(object):
    def __init__(self, name, password, city, email, contact):
        self.name = name
        self.password = password
        self.city = city
        self.email = email
        self.contact = contact





class login():
    def __init__(self, root):
        self.users = {}
        self.root = root
        f = open('users.log', 'rb')
        while True:
            try:
                user = pickle.load(f)
                self.users[user.name] = user.password

            except EOFError:
                f.close
                break

        self.cont = Frame(self.root)
        self.cont.pack()
        self.name = StringVar()
        self.pasw = StringVar()
        self.head = Label(self.cont, text='LOGIN', font=('Times', 45, 'bold'), fg='#546775')
        self.head.grid(row=1, column=1, columnspan=2)
        self.lab1 = Label(self.cont, text='USERNAME', font=('Courier', 15, 'bold'), fg='#792834')
        self.lab1.grid(row=2, column=1)
        self.ent1 = Entry(self.cont, bd=5, font=('Courier', 15, 'bold'), textvariable=self.name)
        self.ent1.grid(row=2, column=2)
        self.ent1.focus_set()
        self.lab2 = Label(self.cont, text='PASSWORD', font=('Courier', 15, 'bold'), fg='#792834')
        self.lab2.grid(row=3, column=1)
        self.ent2 = Entry(self.cont, bd=5, font=('Courier', 15, 'bold'), show='*', textvariable=self.pasw)
        self.ent2.grid(row=3, column=2)
        self.but = Button(self.cont, text='Login', font=('Courier', 25, 'bold'), fg='cyan', command=self.callback)
        self.but.grid(row=4, column=1, columnspan=2)

        self.ent1.bind('<Return>', self.move1)
        self.ent2.bind('<Return>', self.move2)
        self.root.mainloop()

    def move1(self, *arg):
        return self.ent2.focus_set()

    def move2(self, *arg):
        return self.but.invoke()

    def callback(self):
        complete = False
        for user in self.users:
            if self.name.get() == user and self.pasw.get() == self.users[user]:
                complete = True
                self.root.destroy()
                self.user = user
                return
        if not complete:
            com = tkMessageBox.askyesno(title='Wrong Password', message='WRONG PASSWORD!!!!  Do you want to retry?')
            if com:
                self.ent2.delete(0, END)
            else:
                self.root.destroy()
                win1.win1()


class existing(Tk):
    def __init__(self, name, *arg):
        Tk.__init__(self, *arg)
        self.name = name
        lab1 = Label(self, text='Welcome', font=('Comic Sans MS', 50), fg='red', width=13)
        lab1.pack()
        lab2 = Label(self, text='Mr.' + name, font=('Comic Sans MS', 50, 'bold'), fg='#994483', width=13)
        lab2.pack()
        bottom = Frame()
        bottom.pack()
        but = Button(bottom, text='Password Policy', font=('Courier', 20, 'bold'), fg='#436632', bg='#abcdef', width=20,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open1)
        but.grid(row=1, column=1)

        but = Button(bottom, text='MsConfig', font=('Courier', 20, 'bold'), fg='#436632', bg='#abcdef', width=20,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open2)
        but.grid(row=2, column=2)

        but = Button(bottom, text='Modify Details', font=('Courier', 20, 'bold'), fg='#436632', bg='#abcdef', width=20,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open3)
        but.grid(row=1, column=2)

        but = Button(bottom, text='Delete User', font=('Courier', 20, 'bold'), fg='#436632', bg='#abcdef', width=20,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.open4)
        but.grid(row=2, column=1)

        but = Button(bottom, text='Back', font=('Courier', 20, 'bold'), fg='#436632', bg='#bbcdef', width=12,
                     cursor='hand2',
                     activebackground='#86cc64', command=self.back)
        but.grid(row=3, column=1, columnspan=2)

    def open1(self):
        self.destroy()
        Password_Policy().mainloop()

    def open2(self, *arg):
        self.destroy()
        MsConfig().mainloop()

    def open3(self, *arg):
        self.destroy()
        change(self.name).mainloop()

    def open4(self, *arg):
        self.destroy()
        f = open('users.log', 'rb')
        fn = open('temp.log', 'wb')
        while True:
            try:
                user = pickle.load(f)
                if win1.new != user.name:
                    pickle.dump(user, fn)

            except EOFError:
                f.close()
                fn.close()
                break

    def open5(self, *arg):
        self.destroy()
        os.remove('users.log')
        os.rename('temp.log', 'users.log')
        win1().mainloop()

    def back(self):
        self.destroy()
        win1().mainloop()


class change(Tk):
    def __init__(self, new, *arg):
        if new == None:
            return
        Tk.__init__(self, *arg)
        f = open('users.log', 'rb')
        self.new = new
        self.name = StringVar()
        self.pasw = StringVar()
        self.contact = StringVar()
        self.city = StringVar()
        self.email = StringVar()
        while True:
            try:
                user = pickle.load(f)
                if new == user.name:
                    self.name.set(user.name)
                    self.pasw.set(user.password)
                    self.city.set(user.city)
                    self.email.set(user.email)


            except EOFError:
                f.close()
                break

        self.lab1 = Label(text='UPDATE YOUR DETAILS U WANT TO CHANGE', font=('Times', 17, 'bold'), fg='#15633b')
        self.lab1.grid(row=1, column=1, columnspan=2)

        self.lab2 = Label(text='Username', font=('Times', 17), fg='#14b863')
        self.lab2.grid(row=2, column=1)
        self.txt1 = Entry(bd=4, width=20, font=('Verdana', 12), textvariable=self.name)
        self.txt1.grid(row=2, column=2)

        self.lab3 = Label(text='Password', font=('Times', 17), fg='#14b863')
        self.lab3.grid(row=3, column=1)
        self.txt2 = Entry(bd=5, width=20, font=('Verdana', 12), textvariable=self.pasw)
        self.txt2.grid(row=3, column=2)

        self.lab4 = Label(text='Contact No.', font=('Times', 17), fg='#14b863')
        self.lab4.grid(row=4, column=1)
        self.txt3 = Entry(bd=5, width=20, font=('Verdana', 12), textvariable=self.contact)
        self.txt3.grid(row=4, column=2)

        self.lab5 = Label(text='City', font=('Times', 17), fg='#14b863')
        self.lab5.grid(row=5, column=1)
        self.txt4 = Entry(bd=5, width=20, font=('Verdana', 12), textvariable=self.city)
        self.txt4.grid(row=5, column=2)

        self.lab6 = Label(text='Email', font=('Times', 17), fg='#14b863')
        self.lab6.grid(row=6, column=1)
        self.txt5 = Entry(bd=5, width=20, font=('Verdana', 12), textvariable=self.email)
        self.txt5.grid(row=6, column=2)

        self.txt1.bind('<Return>', self.call2)
        self.txt2.bind('<Return>', self.call3)
        self.txt3.bind('<Return>', self.call4)
        self.txt4.bind('<Return>', self.call5)
        self.txt5.bind('<Return>', self.call6)
        self.but = Button(self, text='BACK', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.back)
        self.but.grid(row=7, column=1)

        self.but = Button(self, text='DONE', font=('Courier', 15, 'bold'), fg='#436632', bg='#abcdef', width=15,
                          cursor='hand2',
                          activebackground='#86cc64', command=self.callback)
        self.but.grid(row=7, column=2)

    def call2(self, *arg):
        return self.txt2.focus_set()

    def call3(self, *arg):
        return self.txt3.focus_set()

    def call4(self, *arg):
        return self.txt4.focus_set()

    def call5(self, *arg):
        return self.txt5.focus_set()

    def call6(self, *arg):
        return self.but.invoke()

    def callback(self, *arg):
        f = open('users.log', 'rb')
        fn = open('temp.log', 'wb')
        while True:
            try:
                user = pickle.load(f)
                if self.new == user.name:
                    name = self.name.get()
                    pas = self.pasw.get()
                    contact = self.contact.get()
                    email = self.email.get()
                    city = self.city.get()
                    user = new_file(name, pas, city, email, contact)
                pickle.dump(user, fn)

            except EOFError:
                f.close()
                fn.close()
                break
        os.remove('users.log')
        os.rename('temp.log', 'users.log')
        self.back()

    def back(self):
        self.destroy()
        existing(win1.new).mainloop()


app = win1()

app.mainloop()
