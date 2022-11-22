#%%
class User():
    def __init__(self, first_name, last_name, **user_info):
        self.first_name = first_name
        self.last_name = last_name
        self.age = user_info['age']
        self.city = user_info['city']
        self.state = user_info['state']
        for key, value in user_info.items():
            self.key = value

    def describe_user(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() + " tem " +
              str(self.age) + " anos, " + self.city.title() + " e " + self.state.title() + ".")

    def greet_user(self):
        print("Olá, " + self.first_name.title() +
              " " + self.last_name.title() + "!")


class Privileges(User):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)

    def show_privileges(self):
        print("O usuário " + self.first_name.title() + " " + self.last_name.title() +
              " possui os seguintes privilégios: " + str(self.privileges))


class Admin(Privileges):
    def __init__(self, first_name, last_name, **user_info):
        super().__init__(first_name, last_name, **user_info)
        self.privileges = ['can add post', 'can delete post', 'can ban user']


privileges = Admin('jose', 'silva', age=20, city='são paulo', state='sp')
privileges.show_privileges()