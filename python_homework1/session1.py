# Напишите программу, которая принимает на вход цифру, обозначающую день недели,
# и проверяет, является ли этот день выходным.
# Пример:
# - 6 -> да
# - 7 -> да
# - 1 -> нет

a = int(input('введите цифру - '))
if a > 5: 
    print (f'- {a} -> да')
else:
    print (f'- {a} -> нет')



# Напишите программу для. проверки истинности утверждения ¬(X ⋁ Y ⋁ Z) = ¬X ⋀ ¬Y ⋀ ¬Z для всех значений предикат.

x=(input(f"Введите значение x: "))
y=(input(f"Введите значение y: "))
z=(input(f"Введите значение z: "))
left = not (x or y or z)
right = not x and not y and not z
print (left == right)



# Напишите программу, которая принимает на вход координаты точки (X и Y), 
# причём X ≠ 0 и Y ≠ 0 и выдаёт номер четверти плоскости, 
# в которой находится эта точка (или на какой оси она находится).
# Пример:
# - x=34; y=-30 -> 4
# - x=2; y=4-> 1
# - x=-34; y=-30 -> 3

x=0
while x==0:
    x=int(input(f'введите x '))
y=0
while y==0:
    y=int(input(f'введите y '))
if x>0 and y>0: 
    print(f'- x={x}; y={y} -> 1')
if x<0 and y>0: 
    print(f'- x={x}; y={y} -> 2')
if x<0 and y<0: 
    print(f'- x={x}; y={y} -> 3')
if x>0 and y<0: 
    print(f'- x={x}; y={y} -> 4')
  
  
    
# Напишите программу, которая по заданному номеру четверти, показывает диапазон возможных координат точек в этой четверти (x и y).

x=int(input(f'введите номер четверти - '))
match x:
    case 1:
        print ('x + , y + ')
    case 2:
        print ('x - , y + ')
    case 3:
        print ('x - , y - ')  
    case 4:
        print ('x + , y - ')          
        
        
        
# Напишите программу, которая принимает на вход координаты двух точек 
# и находит расстояние между ними в 2D пространстве.
# Пример:
# - A (3,6); B (2,1) -> 5,09
# - A (7,-5); B (1,-1) -> 7,21

x1=int(input(f'введите x первой точки '))
y1=int(input(f'введите y первой точки '))
x2=int(input(f'введите x второй точки '))
y2=int(input(f'введите y второй точки '))
d=( (x2-x1) ** 2 + (y2-y1) ** 2 ) ** 0.5
print (f'- A ({x1},{y1}); B ({x2},{y2}) -> {round(d,2)}')