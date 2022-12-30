import msvcrt, sys

method='__orientation, year, car, emka, dancho_bratan, wh, aldik'
method2='Human2'
while True:
    method_count=0
    # methode1= input(method)
    for i in method:
        if i.isalpha():
         if i in method:
                method_count +=1
                if msvcrt.kbhit():
                   k = ord(msvcrt.getch())
                sys.exit()

        else:
         print('Количество методов', str(len(method)))






