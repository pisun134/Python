n = int(input())
h = n // 100
t = (n // 10) % 10
o = n % 10
text = ''
match h:
    case 1:
        text += 'Сто '
    case 2:
        text += 'Двести '
    case 3:
        text += 'Триста '
    case 4:
        text += 'Четыреста '
    case 5:
        text += 'Пятьсот '
    case 6:
        text += 'Шестьсот '
    case 7:
        text += 'Семьсот '
    case 8:
        text += 'Восемьсот '
    case 9:
        text += 'Девятьсот '

match t:
    case 1:
        match o:
            case 0:
                text += 'Десять'
            case 1:
                text += 'Одиннадцать'
            case 2:
                text += 'Двенадцать'
            case 3:
                text += 'Тринадцать'
            case 4:
                text += 'Четырнадцать'
            case 5:
                text += 'Пятнадцать'
            case 6:
                text += 'Шестнадцать'
            case 7:
                text += 'Семнадцать'
            case 8:
                text += 'Восемнадцать'
            case 9:
                text += 'Девятнадцать'
    case 2:
        text += 'Двадцать '
    case 3:
        text += 'Тридцать '
    case 4:
        text += 'Сорок '
    case 5:
        text += 'Пятьдесят '
    case 6:
        text += 'Шестьдесят '
    case 7:
        text += 'Семьдесят '
    case 8:
        text += 'Восемьдесят '
    case 9:
        text += 'Девяносто '

if t > 1:
    match o:
        case 1:
            text += 'один'
        case 2:
            text += 'Два'
        case 3:
            text += 'Три'
        case 4:
            text += 'Четыре'
        case 5:
            text += 'Пять'
        case 6:
            text += 'Шесть'
        case 7:
            text += 'Семь'
        case 8:
            text += 'Восемь'
        case 9:
            text += 'Девять'
print(text)
