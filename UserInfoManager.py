'''
Author name: Jeremiah E. Ochepo
Code description: Sorting Data using json.dump() and json.load()
Last Updated Date: 9/29/19
'''
import json


# Function to print a horizontal line
def horizontal_line(numb_line):
    print('__' * numb_line)


numb_line = 24
horizontal_line(numb_line)


class UserInfoManager:
    def __init__(self):
        self.active_flag = True
        self.count = 0
        self.user_id = ''
        self.prompt1 = ''
        self.f_name = ''
        self.m_name = ''
        self.l_name = ''
        self.my_list = []
        self.info_dict = {}
        self.file_name = ''
        self.f_obj = None
        self.f_content = None

    def collect_info(self):
        while self.active_flag:
            horizontal_line(numb_line)
            self.prompt1 = input('\nAdd/Quit/Print? ').lower()

            if self.prompt1 == 'quit':
                print('Ending Program!')
                self.active_flag = False

            elif self.prompt1 == 'add':
                self.count += 1
                self.user_id = 'Guest' + str(self.count)
                self.f_name = input('Enter First Name: ')
                self.m_name = input('Enter Middle Name: ')
                self.l_name = input('Enter Last Name: ')

                self.info_dict = {
                    'User ID#': self.user_id,
                    'First Name': self.f_name,
                    'Middle Name': self.m_name,
                    'Last Name': self.l_name
                }

                self.my_list.append(self.info_dict)

                self.file_name = '../user_info.json'
                with open(self.file_name, 'w') as self.f_obj:
                    json.dump(self.my_list, self.f_obj)
                    print('Enter(Print) to view input.')
                    print('Enter(Add) to add new input.')
                    print('Enter(Quit) to end program.\n')

            elif self.prompt1 == 'print':
                with open(self.file_name) as self.f_obj:
                    self.f_content = json.load(self.f_obj)
                self.active_flag = False

            else:
                print('Entry error! Options(Add/Quit/Print)')
                self.active_flag = False

    def display_user_info(self):
        for user_info in self.f_content:
            for key, value in user_info.items():
                print(f'{key.title()}: {value.title()}')
            horizontal_line(numb_line)


# Program arguments
user_info_manager = UserInfoManager()
user_info_manager.collect_info()
user_info_manager.display_user_info()
