# Плавучи ли объект?( ввести массу тела, объём погружённой 
# части объекта, плотность)


def arh(m,v): 
    return m*9.8 == 1*9.8*v


def main():
    print ('Введите массу тела, объём погруженной части объекта и его плотность')
    m = int(input())
    v = int(input())
    p = int(input())
    res = arh(m,v)
    print ('Объект плавучий')
    print (res)

if __name__=='__main__':
    main()