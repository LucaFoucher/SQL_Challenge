import random

def multiply_until_4():
    while True:
     
        A = random.randint(1, 9)
        B = random.randint(1, 9)

        C = A * B 
        print(f'A: {A}, C: {C}')

        if C == 4:
            print('Success!')
            
            print(f'Results for A: {A} and B: {B}')
            break


multiply_until_4()
