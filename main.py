#Главный файл

#Плавучий ли объект?
import Arhimed as m1
#Находим объём усечённой пирамиды
import pyramid as m2

def main():
    print ('Введите A, если хотите узнать плавучий ли объект\n'
           'Введите P, если хотите узнать объём усечённой пирамиды:')
    user = input()
    if user.upper()== 'A':
        print('Введите массу тела, объём погруженной части объекта и его плотность')
        m = int(input())
        v = int(input())
        p = int(input())
        print ('Объект плавучий')
        print (m1.arh(m,v))
    elif user.upper()== 'P':
        print('Введите площадь верхнего и нижнего основания и высоту')
        S1 = int(input())
        S2 = int(input())
        H = int(input())
        print('Ответ:', m2.V(S1,S2,H))

if __name__=='__main__':
    main()