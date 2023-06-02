from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup
from kivy.utils import platform

import pyrebase
import os

if platform == 'android':
    from android.permissions import request_permissions, Permission
    request_permissions([
        Permission.WRITE_EXTERNAL_STORAGE,
        Permission.READ_EXTERNAL_STORAGE,
        Permission.INTERNET,
    ])
outvar =''
class LoadDialog(FloatLayout):
    load = ObjectProperty(None)
    cancel = ObjectProperty(None)

class SaveDialog(FloatLayout):
    save = ObjectProperty(None)
    text_input = ObjectProperty(None)
    cancel = ObjectProperty(None)

class Root(FloatLayout):
    loadfile = ObjectProperty(None)
    savefile = ObjectProperty(None)
    text_input = ObjectProperty(None)

    def dismiss_popup(self):
        self._popup.dismiss()

    def show_load(self):
        content = LoadDialog(load=self.load, cancel=self.dismiss_popup)
        self._popup = Popup(title="Load file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def show_save(self):
        content = SaveDialog(save=self.save, cancel=self.dismiss_popup)
        self._popup = Popup(title="Save file", content=content,
                            size_hint=(0.9, 0.9))
        self._popup.open()

    def load(self, path, filename):
        print('filename:::',filename)
        print('file path:::',path)
        global outvar



        print('filename[]:::',filename[0])
        mytext= str(filename[0])
        plec= mytext.replace('\\','/')
        outvar =plec
        print('outvar dentro load::',outvar)
        print('plec::',plec)
        if  plec.find('.jpg')>0:
            print('jpg ind;;::',plec.find('.jpg'))
            self.ids.image.source = filename[0]
            #self.text_input.text = 'uploading png'
        elif  plec.find('.png'):
            print('png ind;;::',plec.find('.png'))
            self.ids.image.source = filename[0]
            #self.text_input.text = 'uploading png'

        # with open(os.path.join(path, filename[0])) as stream:
        #     self.text_input.text = stream.read()

        self.dismiss_popup()
    
    def uploader(self,plec):

       
        config= { "apiKey": "AIzaSyBxw0QngVLFlufOghrZv6MV2JIXVN4vSbk",
        "authDomain": "test-fire-base-f2a39.firebaseapp.com",
        "databaseURL":"https://test-fire-base-f2a39-default-rtdb.europe-west1.firebasedatabase.app",
        "projectId": "test-fire-base-f2a39",
        "storageBucket": "test-fire-base-f2a39.appspot.com",
        "messagingSenderId": "958225020020",
        "appId": "1:958225020020:web:d417437c2b7802f6aa4d21",
        "measurementId": "G-PE3FHE56LB"}
        firebase = pyrebase.initialize_app(config)
        storage = firebase.storage()
        path_local=plec
        print('path_local:::',path_local)
        print('path_local len:::',len(path_local))
        # path_local="logo.png"
        img=plec[len(path_local)-13:len(path_local)]
        print('image name::',img)
        path_on_cloud="img4/"+str(img)
        print('path_on_cloud::::',path_on_cloud)

        # path_local=r'C:\Users\MINE\Pictures\leeon data\screenshoot\2021-05-11 12_18_43-Greenshot.png'
        storage.child(path_on_cloud).put(path_local)
        print('storage::',storage)   



    def upload(self):
        #print('filename:::',filename)
        ##print('filename[]:::',filename[0])
        #mytext= str(filename[0])
        #plec= mytext.replace('\\','/')
        print('outvar dentro upload::',outvar)
        #plec='C:/Dowmarker.jpg'
        plec=outvar
        print('plec::',plec)
        if  plec.find('.jpg')>0:
            print('jpg ind;;::',plec.find('.jpg'))
            #self.ids.image.source = filename[0]
            self.text_input.text = 'uploading jpg'
            self.uploader(plec)
        elif  plec.find('.png'):
            print('png ind;;::',plec.find('.png'))
            #self.ids.image.source = filename[0]
            self.text_input.text = 'uploading png'
            self.uploader(plec)

        # with open(os.path.join(path, filename[0])) as stream:
        #     self.text_input.text = stream.read()
    






    def save(self, path, filename):
        with open(os.path.join(path, filename), 'w') as stream:
            stream.write(self.text_input.text)

        self.dismiss_popup()


class Editor(App):
    pass


Factory.register('Root', cls=Root)
Factory.register('LoadDialog', cls=LoadDialog)
Factory.register('SaveDialog', cls=SaveDialog)


if __name__ == '__main__':
    Editor().run()