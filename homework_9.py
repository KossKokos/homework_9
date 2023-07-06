from re import findall

def input_error(func):
    def decorator(command):
        try:
            result = func(command)
            return result
        except KeyError:
            print('Wrong user_name, try again')
        except IndexError:
            print('enter one of those commands: (add, show_all, hello, change, phone)')
        
    return decorator


dict_of_contacts = {}
@input_error
def add_contact(comand):
    find_name_number = r'[A-z\d]{1,}'
    only_name_and_num = comand[3:]
    name_and_number = findall(find_name_number, only_name_and_num)
    dict_of_contacts.update({name_and_number[0]:name_and_number[1]})
    return dict_of_contacts
@input_error       
def change_number(command):
    find_name_number =r'[A-z\d]{1,}'
    only_name_num = command[6:]
    name_and_num = findall(find_name_number, only_name_num)
    for key in dict_of_contacts.keys():
        if key == name_and_num[0]:
            dict_of_contacts[key] = name_and_num[1] 
        else:
            KeyError
    return dict_of_contacts
@input_error
def return_phone(command):
    find_name = r'[A-z]{1,}'
    only_name = command[5:]
    name = findall(find_name, only_name)
    result = dict_of_contacts.get(name[0])
    if result != None:
        return result
    else:
        return f'Key {name[0]} not in dictionary'
@input_error
def show_all(command):
    dict_of_contacts
    return dict_of_contacts

@input_error
def find_commands(command):
    command_re = r'^[A-z_]{1,}'
    find_command = findall(command_re, command.lower())
    return find_command[0]

@input_error
def say_hello(command):
    return 'How can i help you?'


def main():
    while True:
        user_input = input('>>>')
       # command = r'^[A-z]{1,}'
      #  find_command = findall(command, user_input.lower())
        if user_input.lower() == 'good bye' or user_input.lower() == 'close' or user_input.lower() == 'exit':
           break
        users_inputs = {
                        'hello': say_hello(user_input.lower()), 
                        'add': add_contact(user_input.lower()),
                        'change': change_number(user_input.lower()), 
                        'phone': return_phone(user_input.lower()), 
                        'show_all': show_all(user_input.lower())
                        }
        result = ''
        if find_commands(user_input) in users_inputs.keys():
            result = users_inputs.get(find_commands(user_input))
        print(result)

     #   if find_commands(user_input) == 'hello':
    #        print(say_hello('hello'))
    #    if find_commands(user_input) == 'add':
    #        add_contact(user_input.lower())
    #    elif find_commands(user_input) == 'show_all':
   #         print(show_all('show_all'))
    #    elif find_commands(user_input) == 'change':
    #        change_number(user_input.lower())
   #     elif find_commands(user_input) == 'phone':
    #        print(return_phone(user_input.lower()))
        #else:
         #   print('wrong command')
                
            


    
    


if __name__ == '__main__':
    main()