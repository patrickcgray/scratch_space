#! /usr/bin/env python3

def count_em_up(print_nums=False):
    for x in range(1, 101):
        div_by_3 = False
        div_by_5 = False
        if x % 3 == 0:
            div_by_3 = True
        if x % 5 == 0: 
            div_by_5 = True
        if div_by_3 and div_by_5:
            print("CracklePop")
        elif div_by_3:
            print("Crackle")
        elif div_by_5:
            print("Pop")
        elif print_nums:
            print(x)

def main():
    count_em_up()
    
if __name__ == "__main__":
    main()
