import random
def random_phone_num_generator():
    first = str(random.randint(87, 89))
    second = str(random.randint(1, 888)).zfill(3)

    last = (str(random.randint(1, 9998)).zfill(4))
    while last in ['1111', '2222', '3333', '4444', '5555', '6666', '7777', '8888']:
        last = (str(random.randint(1, 9998)).zfill(4))

    return '0{}{}{}'.format(first, second, last)

a = random_phone_num_generator()
print(a)