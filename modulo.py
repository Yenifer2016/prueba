import sys
import os

def cambio(n,d,m,t):
    os.system('cls')
    print("Ud esta en el tipo de fondo: ",t)
    print("¿A que tipo de fondo quiere cambiar?")
    print("\t 1. Fondo 1")
    print("\t 2. Fondo 2")
    print("\t 3. Fondo 3")
    print()
    t=input()
    while(t!=1 and t!=2 and t!=3):
        if t=="1":
            mt=(m*0.02)+m
            print("Ud. se ha cambiado a fondo 1")
            print("su monto total sera: ",mt," soles")
            print()
            pregunta(n,d,m,t)
            menu()
            ope(n,d,m,t)
            
        elif t=="2":
            mt=(m*0.04)+m
            print("Ud. se ha cambiado a fondo 2")
            print("su monto total sera: ",mt," soles")
            print()
            pregunta(n,d,m,t)
            menu()
            ope(n,d,m,t)
            
        elif t=="3":
            mt=(m*0.07)+m
            print("Ud. se ha cambiado a fondo 3")
            print()
            print("su monto total sera: ",mt," soles")
            print()
            pregunta(n,d,m,t)
            menu()
            ope(n,d,m,t)
            
        cambio(n,d,m,t)
        t=input()
        
    print("INGRESE UN VALOR CORRECTO")

def ahorro(n,d,m,t):
    os.system('cls')
    while True:
        try:
            ma=float(input("Ingrese monto de ahorro: "))
            break
        except ValueError:
            print("INGRESE UN MONTO DE AHORRO VALIDO.")
    while True:
        try:
            mes=int(input("Ingrese numero de meses: "))
            break
        except ValueError:
            print("INGRESE UNA CANTIDAD DE MESES CORRECTO.")
    os.system('cls')
        
    if (t=="1"):
        at=ma+(ma*0.02*mes)
        am=at/mes
        print()
        print("Ud. se ha identificado como: ",n.capitalize())
        print("Su DNI es: ",d)
        print("Su monto de fondo es: ",m)
        print("Su Tipo de fondo: ",t)
        print("SU AHORRO TOTAL ES: ",at)
        print("SU AHORRO MENSUAL ES: ",am)
        print()
        pregunta(n,d,m,t)
        

    if (t=="2"):
        at=ma+(ma*0.04*mes)
        am=at/mes
        print()
        print("Ud. se ha identificado como: ",n.capitalize())
        print("Su DNI es: ",d)
        print("Su monto de fondo es: ",m)
        print("Su Tipo de fondo: ",t)
        print("SU AHORRO TOTAL ES: ",at)
        print("SU AHORRO MENSUAL ES: ",am)
        print()
        pregunta(n,d,m,t)
        

    if (t=="3"):
        at=ma+(ma*0.07*mes)
        am=at/mes
        print()
        print("Ud. se ha identificado como: ",n.capitalize())
        print("Su DNI es: ",d)
        print("Su monto de fondo es: ",m)
        print("Su Tipo de fondo: ",t)
        print("SU AHORRO TOTAL ES: ",at)
        print("SU AHORRO MENSUAL ES: ",am)
        print()
        pregunta(n,d,m,t)
        


def menu():
    os.system('cls')
    print()
    print("Operaciones")
    print("\t 1. Imprime reporte.")
    print("\t 2. Cambio de Tipo de Fondo.")
    print("\t 3. Ahorros en Fondo Mutuo.")
    print("\t 4. Salir.")

def ope(n,d,m,t):
    print()
    o=input("Ingrese el tipo de operacion que desea realizar: ")
    print()
    os.system('cls')
    while (o!=1 and o!=2 and o!=3 and o!=4):
        if o=="1":
            print("Ud. se ha identificado como: ",n.capitalize())
            print("Su DNI es: ",d)
            print("Su monto de fondo es: ",m)
            print("Su Tipo de fondo: ",t)
            print()
        elif o=="2":
            cambio(n,d,m,t)
        elif o=="3":
            ahorro(n,d,m,t)
        elif o=="4":
            pregunta2(n,d,m,t)
            
        pregunta(n,d,m,t)
        menu()
        print()
        o=input("Ingrese el tipo de operacion que desea realizar: ")
        print()

    print("EL VALOR DADO ES INCORRECTO.")
def verificar(a):
    for c in a:
        if((ord(c)<65 or ord(c)>90) and (ord(c)<97 or ord(c)>122 ) and (ord(c)!=32)):
            return False
    return True

def vale(m):
    if m==float:
        print("EL VALOR DADO ES CORRECTO UD. PUEDE CONTINUAR.")
        
def validacion(t):
    if t==int:
        print("EL VALOR DADO ES CORRECTO UD. PUEDE CONTINUAR.")
        
def pregunta(n,d,m,t):
    h=input("DESEA REALIZAR OTRA OPERACION(SI/NO): ")
    if h=="Si" or h=="SI" or h=="si":
        menu()
        ope(n,d,m,t)
    elif h=="No" or h=="NO" or h=="no":
        print("EL PROGRAMA SE CERRARA EN 5 SEGUNDOS.")
        import sys
        sys.exit(5)
def pregunta2(n,d,m,t):
    u=input("REALMENTE DESEAS SALIR:(SI/NO): ")
    if u=="Si" or u=="SI" or u=="si":
        print("EL PROGRAMA SE CERRARA EN 5 SEGUNDOS.")
        import sys
        sys.exit(5)
    elif u=="No" or u=="NO" or u=="no":
        menu()
        ope(n,d,m,t)
    
        

    
        
        
