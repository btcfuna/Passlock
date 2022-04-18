from kivymd.app import MDApp
from kivymd.toast import toast
from kivymd.uix.screen import MDScreen
import os.path
from time import time
from kivy.factory import Factory
app = MDApp.get_running_app()


class LoginScreen(MDScreen):
    loading_view =  None

    def login_button_pressed(self, password):

        def dismiss_spinner(*args):
            if self.load:
                app.root.load_screen('HomeScreen')
            self.loading_view.dismiss()

        def initialise_encryption():
            i = time()
            from libs.Backend import Encryption
            try:
                self.load = True
                if app.fps: 
                    app.fps_monitor_start()
                app.encryption_class = Encryption(password)
                if os.path.exists("data/password"):
                    app.passwords = app.encryption_class.load_decrypted()
                else:
                    if os.path.exists("data/encrypted_file.txt"):
                        with open("data/encrypted_file.txt","r")as f:
                            app.encryption_class.decrypt(f.read())
                    else:
                        print("'encrypted_file' not found, can't check password.")
                    
                dismiss_spinner()
                encrypted_pass = app.encryption_class.load_passwords()
                for keys in encrypted_pass:
                    app.encrypted_keys[app.encryption_class.decrypt(keys)] = keys
                # app.root.HomeScreen.ids.create.ids.tab.switch_tab("[b]MANUAL")
            except UnicodeDecodeError:
                self.load = False
                dismiss_spinner()
                toast('Invalid password')
            print(f"Time taken to load passwords = {time()-i}")
            
        if self.loading_view is None:
            self.loading_view = Factory.LoadingScreen()
        self.loading_view.open()
        self.loading_view.on_open = lambda *args: initialise_encryption()
        
        
