from kivy.app import App
from kivy.uix.label import Label
from kivy.uix.gridlayout import GridLayout
from kivy.properties import StringProperty
from kivy.properties import NumericProperty
from random import choice
from random import shuffle
#from pyperclip import copy
from kivy.uix.popup import Popup
from kivy.uix.screenmanager import ScreenManager,Screen,FadeTransition
from kivy.core.clipboard import Clipboard
from simplecrypt import encrypt,decrypt
import sqlite3

'''
To set up forced dimensions of the applications 

from kivy.config import Config
Config.set('graphics', 'width', '500')
Config.set('graphics', 'height', '700')
'''

# setting up the database connections 

db = sqlite3.connect("pwddb")
cursor = db.cursor()
cursor.execute(''' CREATE TABLE IF NOT EXISTS pwd (username varchar(50),password text)''')
db.commit()


class MainScreen(Screen):
    pass
class GenerateScreen(Screen):
    length = NumericProperty()
    password = StringProperty('')
    keyword = StringProperty('')

    def generatepwd(self):
        self.password = ''
        keywd = self.ids.keywd.text

        alphas = 'ABCDEFGHIJKLMNOPQRSTUBWXYZabcdefghijklmnopqrstuvwxyz0123456789./_-'
        if (self.ids.pwdlen.text == ''):
            popup = Popup(title="Incorrect Input", size=(200, 200), size_hint=(None, None),
                          content=Label(text='Length cannot be empty ! '))
            popup.open()
        else:
            length = int(self.ids.pwdlen.text) - len(keywd)

            while (length):
                self.password = self.password + choice(alphas)
                length = length - 1
            result = list(self.password)
            result.append(keywd)
            shuffle(result)
            result = ''.join(result)
            self.password = result

           

    def savepwd(self):
        encryped_pass = encrypt("password",self.password)
        u_name = self.ids.usrname.text
        cursor.execute(''' INSERT INTO pwd values(?,?)''',(u_name,encryped_pass))
        db.commit()
        Clipboard.copy(self.password)
        popup = Popup(title='Saved !', content=Label(text='Copied to clipboard'), size_hint=(None, None),
                      size=(400, 200))
        popup.open()
        

    def clear(self):
        self.length = 0
        # self.password = ''

class RetrieveScreen(Screen):
    global IDS
    def Fetch(self):
        #fetch data from db 
        u_name = self.ids.ret_usrname.text
        cursor.execute('''select password from pwd where username = ?''',(u_name,))
        data = cursor.fetchone()
        print(data[0])
        decrypted_pass = decrypt("password",data[0]).decode("utf-8")
        Clipboard.copy(decrypted_pass)
        popup = Popup(title='Saved !', content=Label(text='Copied to clipboard'), size_hint=(None, None),size=(400, 200))
        popup.open()
       
class screenmanage(ScreenManager):
        pass

class PWManagerapp(App):
    pass

if __name__ == '__main__':
    PWManagerapp = PWManagerapp()
    PWManagerapp.run()