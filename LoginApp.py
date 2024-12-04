from kivymd.app import MDApp
from kivy.lang import Builder
from kivy.uix.screenmanager import Screen, ScreenManager
import random
import smtplib
from email.message import EmailMessage
from kivy.core.window import Window
#Window.size = (350, 550)

class EntryScreen(Screen):
    pass
class SignInScreen(Screen):
    def Clear(self):
        self.ids.email.text = ""
        self.ids.password.text = ""
class SignUpScreen(Screen):
    def SendMail(self):
        global otp
        email = self.ids.gmail.text
        password = self.ids.password.text
        if email != "" and password != "" and "@" in email:
            otp = ""
            for i in range(6):
                otp += str(random.randint(0, 9))
            server = smtplib.SMTP("smtp.gmail.com", 587)
            server.starttls()
            from_mail = "*******" # Enter Your From Mail Here
            server.login(from_mail, "*******") #Enter Your Password Here

            msg = EmailMessage()
            msg["subject"] = "OTP Verification"
            msg["From"] = from_mail
            msg["To"] = email
            msg.set_content("Your OTP is: "+ otp)
            server.send_message(msg)
            self.ids.error.text = "OTP sent Successfully"
        else:
            pass
    def OTP_Verify(self):
        entered_otp = self.ids.otp.text
        if entered_otp != "":
            if entered_otp == otp:
                self.ids.gmail.text = ""
                self.ids.password.text = ""
                self.ids.otp.text = ""
                self.ids.error.text = ""
                self.manager.current = "signin"
                self.manager.transition.direction = "left"
            else:
                pass
        else:
            pass

class HomeScreen(Screen):
    pass
class FirstScreen(Screen):
    pass
class SecondScreen(Screen):
    pass
class ThirdScreen(Screen):
    pass
class WindowScreenManager(ScreenManager):
    pass
class SampleApp(MDApp):
    def build(self):
        return Builder.load_file("LoginApp.kv")
    def Back(self):
        self.root.current = "entry"
        self.root.transition.direction = "right"
if __name__ == "__main__":
    SampleApp().run()
