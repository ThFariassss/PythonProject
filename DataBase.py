import datetime
from kivy.app import App
from kivy.uix.boxlayout import BoxLayout
from kivy.uix.textinput import TextInput
from kivy.uix.button import Button


class DataBase:
    def __init__(self, filename):
        self.filename = filename
        self.users = None
        self.file = None
        self.load()

    def load(self):
        try:
            self.file = open(self.filename, "r")
            self.users = {}
            for line in self.file:
                email, password, name, created = line.strip().split(";")
                self.users[email] = (password, name, created)
            self.file.close()
        except FileNotFoundError:
            self.users = {}

    def get_user(self, email):
        if email in self.users:
            return self.users[email]
        else:
            return -1

    def add_user(self, email, password, name):
        if email.strip() not in self.users:
            self.users[email.strip()] = (password.strip(), name.strip(), DataBase.get_date())
            self.save()
            return 1
        else:
            print("Email already exists")
            return -1

    def validate(self, email, password):
        if self.get_user(email) != -1:
            return self.users[email][0] == password
        else:
            return False

    def save(self):
        with open(self.filename, "w") as f:
            for user in self.users:
                f.write(
                    user + ";" + self.users[user][0] + ";" + self.users[user][1] + ";" + self.users[user][2] + "\n"
                )

    @staticmethod
    def get_date():
        return str(datetime.datetime.now()).split(" ")[0]


class MyApp(App):
    def build(self):
        self.db = DataBase("users.txt")

        layout = BoxLayout(orientation="vertical", spacing=10, padding=10)

        self.email_input = TextInput(text="Email", multiline=False)
        self.password_input = TextInput(text="Password", multiline=False, password=True)
        self.name_input = TextInput(text="Name", multiline=False)
        register_button = Button(text="Register", on_press=self.register_user)
        login_button = Button(text="Login", on_press=self.login_user)

        layout.add_widget(self.email_input)
        layout.add_widget(self.password_input)
        layout.add_widget(self.name_input)
        layout.add_widget(register_button)
        layout.add_widget(login_button)

        return layout

    def register_user(self, instance):
        email = self.email_input.text
        password = self.password_input.text
        name = self.name_input.text

        result = self.db.add_user(email, password, name)
        if result == 1:
            print("User registered successfully.")
        else:
            print("Failed to register user.")

    def login_user(self, instance):
        email = self.email_input.text
        password = self.password_input.text

        if self.db.validate(email, password):
            print("Login successful.")
        else:
            print("Invalid email or password.")


if __name__ == "__main__":
    MyApp().run()
