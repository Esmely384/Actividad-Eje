#inicio
#bienvenida
print("Bienvenido al sistema de Volaris")
#opciones
mty=6000
gdl=3000
cun=5000
total=0
opcion=0
while(opcion!=2):
    print("------------------------------------------")
    print("Seleccione la opcion que desee")
    print("presione 1 para agendar vuelos")
    print("presione 2 para salir")

    print("Elija una opcion: ")
    opcion=int(input())
    if opcion==1:
        #destino
        print("------------------------------------------")
        print("Seleccione el destino que desee")
        print("1: Monterrey, Nuevo Leon, precio por boleto, $6000")
        print("2: Guadalajara, Jalisco, precio por boleto, $3000")
        print("3: Cancún, Quintana Roo, precio por boleto, $5000")
        print("Selecciona el numero de tu destino: ")
        destino=int(input())
        lugar=""
        if destino==1:
            total=total+mty
            lugar="Monterrey, Nuevo Leon"
        elif destino==2:
            total=total+gdl
            lugar="Guadalajara, Jalisco"
        if destino==3:
            total=total+cun
            lugar="Cancún, Quintana Roo"
        if destino>3:
            print("destino no valido")

        print()
        print("para cuantas personas sería su viaje: ")
        personas=int(input())
        if personas==0:
            print("numero no valido, se asignó boleto para una (1) persona")
            personas=1
        else:
            total=total*personas
        
        print()
        print("Desea mejorar su plan de viaje a ejecutivo? Se agregará un monto de $1000 por persona. 1:SI, 2:NO ")
        mejora=int(input())
        plan=""
        if mejora==2:
            print("se mantuvo en clase turista")
            plan="Turista"
        if mejora==1:
            print("se mejoró su plan a ejecutivo")
            total=total+(1000*personas)
            plan="Ejecutivo"
        if mejora>2 or mejora<1:
            plan="Turista"
            print("opcion no valida, no se aplicó ninguna mejora")

        print()
        print("Desea añadir documentar equipaje? se agregará un monto de $200 por maleta extra. 1:SI, 2:NO ")
        equipaje=int(input())
        pequipaje=""
        if equipaje==1:
            pequipaje="Documentado"
            print("inserte el numero de maletas")
            maletas=int(input())
            total=total+(maletas*200)
            
        if equipaje==2:
            pequipaje="Sencillo"
            print("perfecto, solo puede llevar equipaje de mano")
            
        if equipaje>2 or equipaje<1:
            print("opcion no valida, solo puede llevar equipaje de mano")
            pequipaje="Sencillo"

        print()
        print("Desea hacer su viaje redondo? se le cobrará el doble de su monto actual ",total," y se respetará el numero de personas, el plan de viaje y el plan de equipaje")
        print("1:SI, 2:NO ")
        redondo=int(input())
        redondea=""
        if redondo==1:
            total=total*2
            redondea="Si"
            print("Se hizo su viaje redondo")
        if redondo==2:
            redondea="No"
            print("No se hizo su viaje redondo")
        if redondo>2 or redondo<1:
            redondea="No"
            print("opcion no valida, no se hizo su viaje redondo")
        
        print("------------------------------------------")
        print("Terminando su orden")
        print("Su destino es: ", lugar)
        print("se selecciono ",personas, " personas")
        print("se seleccionó el plan de vuelo: ", plan)
        print("se seleccionó el plan de equipaje: ", pequipaje)
        print("Se seleccionó hacer redondo el vuelo: ", redondea)
        print("Su pedido es de : $",total)
        print("¿Está de acuerdo?  1:SI, 2:NO")
        acepto=int(input())
        if acepto==1:
            print("------------------------------------------")
            print("por favor pague ", total)
            while total>0:
                print("ingrese la cantidad a pagar")
                pago=int(input())
                total=total-pago
                if total>0:
                    print("Gracias, pero aun falta por pagar", total)
                elif total==0:
                    print("Gracias por su compra")
                    break
                elif total<0:
                    cambio=total*(-1)
                    print("Gracias por su compra, le sobró", cambio)
        if acepto==2:
            print("Su orden ha sido cancelada")

    if opcion==2:
        print("Hasta Pronto!")
    if opcion>2 or opcion<1:
        print("opcion no valida")