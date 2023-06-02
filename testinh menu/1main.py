from kivy.app import App
from kivy.uix.floatlayout import FloatLayout
from kivy.factory import Factory
from kivy.properties import ObjectProperty
from kivy.uix.popup import Popup

import os
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
        outvar =filename[0]
        print('outvar dentro load::',outvar)


        print('filename[]:::',filename[0])
        mytext= str(filename[0])
        plec= mytext.replace('\\','/')
        print('plec::',plec)
        if  plec.find('.jpg')>0:
            print('jpg ind;;::',plec.find('.jpg'))
            self.ids.image.source = filename[0]
            #self.text_input.text = 'uploading png'
        elif  plec.find('.png'):
            print('png ind;;::',plec.find('.png'))
            self.ids.image.source = filename[0]
            self.text_input.text = 'uploading png'

        # with open(os.path.join(path, filename[0])) as stream:
        #     self.text_input.text = stream.read()

        self.dismiss_popup()
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
            self.text_input.text = 'uploading png'
        elif  plec.find('.png'):
            print('png ind;;::',plec.find('.png'))
            #self.ids.image.source = filename[0]
            self.text_input.text = 'uploading png'

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