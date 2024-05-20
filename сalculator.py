import math
from termcolor import colored
import sys

def rainbow_text(text):
    colors = ['red', 'yellow', 'green', 'cyan', 'blue', 'magenta']
    result = []
    for i, char in enumerate(text):
        color = colors[i % len(colors)]
        result.append(colored(char, color))
    return ''.join(result)

def calculator():
    languages = {
        '1': 'русский',
        '2': 'español',
        '3': 'english'
    }

    print(rainbow_text("Выберите язык / Elija el idioma / Choose the language:"))
    for key, value in languages.items():
        print(rainbow_text(f"{key}. {value}"))
    
    lang_choice = input(rainbow_text("Введите номер языка / Ingrese el número del idioma / Enter the language number: "))

    if lang_choice == '1':
        lang = 'rus'
    elif lang_choice == '2':
        lang = 'esp'
    elif lang_choice == '3':
        lang = 'eng'
    else:
        print(rainbow_text("Неверный выбор / Selección incorrecta / Invalid choice"))
        return

    messages = {
        'rus': {
            'welcome': "Добро пожаловать в умный калькулятор!",
            'choose_op': "Выберите операцию:",
            'exit': "Выход",
            'result': "Результат",
            'first_num': "Введите первое число: ",
            'second_num': "Введите второе число: ",
            'enter_num': "Введите число: ",
            'angle_deg': "Введите угол в градусах: ",
            'angle_rad': "Введите угол в радианах: ",
            'log_base': "Введите основание логарифма: ",
            'error': "Ошибка",
            'invalid_input': "Неверный ввод",
            'div_zero': "Ошибка: Деление на ноль!",
            'sqrt_neg': "Ошибка: Невозможно извлечь квадратный корень из отрицательного числа!",
            'log_neg': "Ошибка: Логарифм определен только для положительных чисел!",
            'factorial_neg': "Ошибка: Факториал определен только для неотрицательных целых чисел!",
        },
        'esp': {
            'welcome': "¡Bienvenido al calculadora inteligente!",
            'choose_op': "Elija la operación:",
            'exit': "Salir",
            'result': "Resultado",
            'first_num': "Ingrese el primer número: ",
            'second_num': "Ingrese el segundo número: ",
            'enter_num': "Ingrese el número: ",
            'angle_deg': "Ingrese el ángulo en grados: ",
            'angle_rad': "Ingrese el ángulo en radianes: ",
            'log_base': "Ingrese la base del logaritmo: ",
            'error': "Error",
            'invalid_input': "Entrada no válida",
            'div_zero': "Error: ¡División por cero!",
            'sqrt_neg': "Error: ¡No se puede calcular la raíz cuadrada de un número negativo!",
            'log_neg': "Error: ¡El logaritmo está definido solo para números positivos!",
            'factorial_neg': "Error: ¡El factorial está definido solo para números enteros no negativos!",
        },
        'eng': {
            'welcome': "Welcome to the smart calculator!",
            'choose_op': "Choose the operation:",
            'exit': "Exit",
            'result': "Result",
            'first_num': "Enter the first number: ",
            'second_num': "Enter the second number: ",
            'enter_num': "Enter the number: ",
            'angle_deg': "Enter the angle in degrees: ",
            'angle_rad': "Enter the angle in radians: ",
            'log_base': "Enter the base of the logarithm: ",
            'error': "Error",
            'invalid_input': "Invalid input",
            'div_zero': "Error: Division by zero!",
            'sqrt_neg': "Error: Cannot compute square root of a negative number!",
            'log_neg': "Error: Logarithm is defined only for positive numbers!",
            'factorial_neg': "Error: Factorial is defined only for non-negative integers!",
        }
    }

    ops = {
        '1': ' + ',
        '2': ' - ',
        '3': ' * ',
        '4': ' / ',
        '9': ' ^ ',
        '24': ' log ',
        '28': ' ^ 2',
        '29': ' ^ 3',
        '30': ' ∛',
        '31': ' ln(1+',
        '32': ' expm1',
        '33': ' log1p',
        '34': ' rad',
        '35': ' deg',
        '36': ' hypot',
        '37': ' sign',
        '38': ' floor',
        '39': ' ceil',
        '40': ' atan2'
    }

    print(rainbow_text(messages[lang]['welcome']))
    print(rainbow_text(messages[lang]['choose_op']))

    operations = [
        "1. Сложение / Adición / Addition",
        "2. Вычитание / Sustracción / Subtraction",
        "3. Умножение / Multiplicación / Multiplication",
        "4. Деление / División / Division",
        "5. Квадратный корень / Raíz cuadrada / Square root",
        "6. Синус / Seno / Sine",
        "7. Косинус / Coseno / Cosine",
        "8. Тангенс / Tangente / Tangent",
        "9. Степень (возведение в степень) / Potencia / Power",
        "10. Логарифм (по основанию 10) / Logaritmo (base 10) / Logarithm (base 10)",
        "11. Натуральный логарифм / Logaritmo natural / Natural logarithm",
        "12. Экспонента (e^x) / Exponente (e^x) / Exponent (e^x)",
        "13. Модуль числа / Módulo / Absolute value",
        "14. Факториал / Factorial / Factorial",
        "15. Гиперболический синус / Seno hiperbólico / Hyperbolic sine",
        "16. Гиперболический косинус / Coseno hiperbólico / Hyperbolic cosine",
        "17. Гиперболический тангенс / Tangente hiperbólico / Hyperbolic tangent",
        "18. Арксинус / Arcoseno / Arcsine",
        "19. Арккосинус / Arcocoseno / Arccosine",
        "20. Арктангенс / Arcotangente / Arctangent",
        "21. Секанс / Secante / Secant",
        "22. Косеканс / Cosecante / Cosecant",
        "23. Котангенс / Cotangente / Cotangent",
        "24. Логарифм по произвольному основанию / Logaritmo de base arbitraria / Logarithm to arbitrary base",
        "25. Арксеканс / Arcosecante / Arcosecant",
        "26. Арккосеканс / Arcocosecante / Arcocosecant",
        "27. Арккотангенс / Arcotangente / Arccotangent",
        "28. Квадрат числа / Cuadrado del número / Square of the number",
        "29. Куб числа / Cubo del número / Cube of the number",
        "30. Кубический корень / Raíz cúbica / Cube root",
        "31. Натуральный логарифм плюс единица (ln(1+x)) / Logaritmo natural más uno (ln(1+x)) / Natural logarithm plus one (ln(1+x))",
        "32. Экспонента минус единица (expm1) / Exponente menos uno (expm1) / Exponent minus one (expm1)",
        "33. Логарифм суммы (log1p) / Logaritmo de la suma (log1p) / Logarithm of sum (log1p)",
        "34. Угол в радианы / Ángulo en radianes / Angle in radians",
        "35. Угол в градусы / Ángulo en grados / Angle in degrees",
        "36. Гипотенуза (hypot) / Hipotenusa / Hypotenuse",
        "37. Сигнум (sign) / Signo (sign) / Signum",
        "38. Пол (floor) / Suelo (floor) / Floor",
        "39. Потолок (ceil) / Techo (ceil) / Ceiling",
        "40. Тригонометрическая обратная функция (atan2) / Función inversa trigonométrica (atan2) / Trigonometric inverse function (atan2)",
    ]

    for op in operations:
        print(rainbow_text(op))
    print(rainbow_text("0. " + messages[lang]['exit']))

    while True:
        choice = input(rainbow_text(messages[lang]['choose_op']))
        if choice == '0':
            print(rainbow_text(messages[lang]['exit']))
            break

        try:
            if choice in ['1', '2', '3', '4', '9', '24', '28', '29']:
                num1 = float(input(rainbow_text(messages[lang]['first_num'])))
                num2 = float(input(rainbow_text(messages[lang]['second_num'])))
                if choice == '1':
                    print(rainbow_text(f"{messages[lang]['result']}: {num1} + {num2} = {num1 + num2}"))
                elif choice == '2':
                    print(rainbow_text(f"{messages[lang]['result']}: {num1} - {num2} = {num1 - num2}"))
                elif choice == '3':
                    print(rainbow_text(f"{messages[lang]['result']}: {num1} * {num2} = {num1 * num2}"))
                elif choice == '4':
                    if num2 != 0:
                        print(rainbow_text(f"{messages[lang]['result']}: {num1} / {num2} = {num1 / num2}"))
                    else:
                        print(rainbow_text(messages[lang]['div_zero']))
                elif choice == '9':
                    print(rainbow_text(f"{messages[lang]['result']}: {num1} ^ {num2} = {math.pow(num1, num2)}"))
                elif choice == '24':
                    print(rainbow_text(f"{messages[lang]['result']}: log({num1}, {num2}) = {math.log(num1, num2)}"))
                elif choice == '28':
                    print(rainbow_text(f"{messages[lang]['result']}: {num1} ^ 2 = {num1 ** 2}"))
                elif choice == '29':
                    print(rainbow_text(f"{messages[lang]['result']}: {num1} ^ 3 = {num1 ** 3}"))

            elif choice == '5':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                if num >= 0:
                    print(rainbow_text(f"{messages[lang]['result']}: √{num} = {math.sqrt(num)}"))
                else:
                    print(rainbow_text(messages[lang]['sqrt_neg']))

            elif choice in ['6', '7', '8', '15', '16', '17', '18', '19', '20', '21', '22', '23', '25', '26', '27']:
                angle = float(input(rainbow_text(messages[lang]['angle_deg'])))
                radians = math.radians(angle)
                if choice == '6':
                    print(rainbow_text(f"{messages[lang]['result']}: sin({angle}) = {math.sin(radians)}"))
                elif choice == '7':
                    print(rainbow_text(f"{messages[lang]['result']}: cos({angle}) = {math.cos(radians)}"))
                elif choice == '8':
                    print(rainbow_text(f"{messages[lang]['result']}: tan({angle}) = {math.tan(radians)}"))
                elif choice == '15':
                    print(rainbow_text(f"{messages[lang]['result']}: sinh({angle}) = {math.sinh(radians)}"))
                elif choice == '16':
                    print(rainbow_text(f"{messages[lang]['result']}: cosh({angle}) = {math.cosh(radians)}"))
                elif choice == '17':
                    print(rainbow_text(f"{messages[lang]['result']}: tanh({angle}) = {math.tanh(radians)}"))
                elif choice == '18':
                    print(rainbow_text(f"{messages[lang]['result']}: asin({angle}) = {math.degrees(math.asin(radians))}"))
                elif choice == '19':
                    print(rainbow_text(f"{messages[lang]['result']}: acos({angle}) = {math.degrees(math.acos(radians))}"))
                elif choice == '20':
                    print(rainbow_text(f"{messages[lang]['result']}: atan({angle}) = {math.degrees(math.atan(radians))}"))
                elif choice == '21':
                    print(rainbow_text(f"{messages[lang]['result']}: sec({angle}) = {1 / math.cos(radians)}"))
                elif choice == '22':
                    print(rainbow_text(f"{messages[lang]['result']}: csc({angle}) = {1 / math.sin(radians)}"))
                elif choice == '23':
                    print(rainbow_text(f"{messages[lang]['result']}: cot({angle}) = {1 / math.tan(radians)}"))
                elif choice == '25':
                    print(rainbow_text(f"{messages[lang]['result']}: asec({angle}) = {math.degrees(math.acos(1 / radians))}"))
                elif choice == '26':
                    print(rainbow_text(f"{messages[lang]['result']}: acsc({angle}) = {math.degrees(math.asin(1 / radians))}"))
                elif choice == '27':
                    print(rainbow_text(f"{messages[lang]['result']}: acot({angle}) = {math.degrees(math.atan(1 / radians))}"))

            elif choice == '10':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                if num > 0:
                    print(rainbow_text(f"{messages[lang]['result']}: log10({num}) = {math.log10(num)}"))
                else:
                    print(rainbow_text(messages[lang]['log_neg']))

            elif choice == '11':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                if num > 0:
                    print(rainbow_text(f"{messages[lang]['result']}: ln({num}) = {math.log(num)}"))
                else:
                    print(rainbow_text(messages[lang]['log_neg']))

            elif choice == '12':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: e^{num} = {math.exp(num)}"))

            elif choice == '13':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: |{num}| = {abs(num)}"))

            elif choice == '14':
                num = int(input(rainbow_text(messages[lang]['enter_num'])))
                if num >= 0:
                    print(rainbow_text(f"{messages[lang]['result']}: {num}! = {math.factorial(num)}"))
                else:
                    print(rainbow_text(messages[lang]['factorial_neg']))

            elif choice == '30':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: ∛{num} = {math.pow(num, 1/3)}"))

            elif choice == '31':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: ln(1+{num}) = {math.log1p(num)}"))

            elif choice == '32':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: expm1({num}) = {math.expm1(num)}"))

            elif choice == '33':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: log1p({num}) = {math.log1p(num)}"))

            elif choice == '34':
                angle = float(input(rainbow_text(messages[lang]['angle_deg'])))
                print(rainbow_text(f"{messages[lang]['result']}: {angle} grados = {math.radians(angle)} radianes"))

            elif choice == '35':
                radians = float(input(rainbow_text(messages[lang]['angle_rad'])))
                print(rainbow_text(f"{messages[lang]['result']}: {radians} radianes = {math.degrees(radians)} grados"))

            elif choice == '36':
                num1 = float(input(rainbow_text(messages[lang]['first_num'])))
                num2 = float(input(rainbow_text(messages[lang]['second_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: hipot({num1}, {num2}) = {math.hypot(num1, num2)}"))

            elif choice == '37':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: sign({num}) = {math.copysign(1, num)}"))

            elif choice == '38':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: floor({num}) = {math.floor(num)}"))

            elif choice == '39':
                num = float(input(rainbow_text(messages[lang]['enter_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: ceil({num}) = {math.ceil(num)}"))

            elif choice == '40':
                num1 = float(input(rainbow_text(messages[lang]['first_num'])))
                num2 = float(input(rainbow_text(messages[lang]['second_num'])))
                print(rainbow_text(f"{messages[lang]['result']}: atan2({num1}, {num2}) = {math.atan2(num1, num2)}"))

            else:
                print(rainbow_text(messages[lang]['invalid_input']))
        except ValueError:
            print(rainbow_text(messages[lang]['invalid_input']))

if __name__ == "__main__":
    calculator()
