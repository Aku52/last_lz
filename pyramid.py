#Находим объём усечённой пирамиды( зная площадь оснований и высоту)

V = lambda S1,S2,H: 1/3*H*(S1+S2+(S1*S2)**(1/2))


def main():
    print('Введите площадь верхнего и нижнего основания и высоту')
    S1 = int(input())
    S2 = int(input())
    H = int(input())
    print('Объём усечённой пирамиды',V(S1,S2,H))



if __name__=='__main__':
    main()