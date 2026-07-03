# Crea una funcion donde aparesca las opciones retirar, depositar, transferir y salir,
# el cliente tiene un saldo de 15000 soles, si el cliente realiza un deposito este se agregara
# a su saldo y se muestra, si el cliente retira un monto, este se descontara de su saldo y se mostrara
# un nuevo saldo, si elige transferir, pedira usar numero de cuenta y luego el monto a transferir y
# se mostrara su nuevo saldo.


def cajero():
    saldo = 15000
    
    while True:
        print("\n[1] Depositar")
        print("[2] Retirar")
        print("[3] Transferir")
        print("[4] Salir")
        
        caso = input("Opcion: ")
        
        if caso == "1":
            monto = int(input("Monto a depositar: "))
            saldo = saldo + monto
            print("Nuevo saldo: S/.", saldo)
        
        elif caso == "2":
            monto = int(input("Monto a retirar: "))
            if monto <= saldo:
                saldo = saldo - monto
                print("Nuevo saldo: S/.", saldo)
            else:
                print("Saldo insuficiente")
        
        elif caso == "3":
            cuenta = input("Numero de cuenta: ")
            monto = int(input("Monto a transferir: "))
            if monto <= saldo:
                saldo = saldo - monto
                print("Transferencia a cuenta", cuenta)
                print("Nuevo saldo: S/.", saldo)
            else:
                print("Saldo no suficiente intente denuevo")
        
        elif caso == "4":
            print("Chao que tenga un buen dia")
            break
        
        else:
            print("Opcion no valida")

cajero()


