# your code goes here!
import time

def countdown(x):
    
    while x >= 1:
        print(f'{x} SECOND(S)!')
        x-=1
    print('HAPPY NEW YEAR!')


def countdown_with_sleep(x):
    while x >= 1:
        print(f'{x} SECOND(S)!')
        x-=1
        time.sleep(1)
    print('HAPPY NEW YEAR!')




