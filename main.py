import names

def get_one_name():
    return names.get_full_name()

def get_array_names(count):
    return [names.get_full_name() for _ in range(count)]

def get_female_name(start_symb):
    female = ''
    while not female.startswith(start_symb):
        female = names.get_first_name(gender='female')
    return female


if __name__ == '__main__':
    print(f'{get_one_name()=}')
    print(f'{get_array_names(7)=}')
    print(f'{get_female_name("F")=}')