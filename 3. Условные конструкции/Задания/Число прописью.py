n = int(input())
h = n // 100
t = (n // 10) % 10
o = n % 10
match h:
    case 1:
        print(f'Сто')
    case 2:
        print(f'Двести')
    case 3:
        print(f'Триста')
    case 4:
        print(f'Четыреста')
    case 5:
        print(f'Пятьсот')
    case 6:
        print(f'Шестьсот')
    case 7:
        print(f'Семьсот')
    case 8:
        print(f'Восемьсот')
    case 9:
        print(f'Девятьсот')
match t:
    case 1:
        match o:
            case 0:
                print(f'Десять')
            case 1:
                print(f'Одиннадцать')
            case 2:
                print(f'Двенадцать')
            case 3:
                print(f'Тринадцать')
            case 4:
                print(f'Четырнадцать')
            case 5:
                print(f'Пятнадцать')
            case 6:
                print(f'Шестнадцать')
            case 7:
                print(f'Семнадцать')
            case 8:
                print(f'Восемнадцать')
            case 9:
                print(f'Девятнадцать')
    case 2:
        print(f'Двадцать')
    case 3:
        print(f'Тридцать')
    case 4:
        print(f'Сорок')
    case 5:
        print(f'Пятьдесят')
    case 6:
        print(f'Шестьдесят')
    case 7:
        print(f'Семьдесят')
    case 8:
        print(f'Восемьдесят')
    case 9:
        print(f'Девяносто')
if t > 1:
    match o:
        case 1:
            print(f'один')
        case 2:
            print(f'Два')
        case 3:
            print(f'Три')
        case 4:
            print(f'Четыре')
        case 5:
            print(f'Пять')
        case 6:
            print(f'Шесть')
        case 7:
            print(f'Семь')
        case 8:
            print(f'Восемь')
        case 9:
            print(f'Девять')
