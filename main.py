import names

def get_one_name():
    return names.get_full_name()

if __name__ == '__main__':
    print(f'{get_one_name()=}')