import names

def get_one_name():
    return names.get_full_name()

def get_array_names(count):
    return [names.get_full_name() for _ in range(count)]

if __name__ == '__main__':
    print(f'{get_one_name()=}')
    print(f'{get_array_names(7)=}')