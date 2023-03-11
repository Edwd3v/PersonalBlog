def run():
    name = 'Edward'
    last_name = 'Steven'

    print(name)
    print(last_name)

    full_name = name + " " + last_name
    age = 23
    print(full_name)

    name_complete_whit_age = 'Hola, mi nombre es {} y mi edad es de {} años'.format(full_name, age)
    print(name_complete_whit_age)

if __name__ == '__main__':
    run