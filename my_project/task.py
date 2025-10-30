def sum_quad(a:int, b:int):
    return a**2 + b**2

gres = f'Сумма квадратов равна: {sum_quad( 5, 6 )}'

with open('result.txt', 'w', encoding='utf-8') as file:
    file.write(res)