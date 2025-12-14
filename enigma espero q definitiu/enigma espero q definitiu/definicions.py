import os
import random

abecedari = "ABCDEFGHIJKLMNOPQRSTUVWXYZ"
MAX = 26

def pantalla_inici():
    print(
        "ENIGMA:\n"
        "---------------\n"
        "1. Xifrar missatge\n"
        "2. Desxifrar missatge\n"
        "3. Editar rotors\n"
        "4. Sortir"
    )


def cablejat_rotors():
    llista2 = []
    llista = []
    for y in abecedari:
        llista.append(y)
    while len(llista2) < 26:
        num=random.randint(0,25)
        if llista[num] not in llista2:
            llista2.append(llista[num])
    llista2 = "".join(llista2)
    return llista2


def abans_xifrar(text_original):
    text_original = text_original.upper()
    llista=[]
    for y in text_original:
        llista.append(y)
    for x in llista:
        if x not in abecedari:
            llista.remove(x)
    frase="".join(llista)
    return frase
   

def posicio_inicial_rotors():
    rotors_llista=[]
    while True:
        posicio_inicial1 = input("digues la posicio inicial del rotor 1 (una lletra A-Z): ").strip().upper()
        if len(posicio_inicial1) == 1 and posicio_inicial1 in abecedari:
            break
        print("ERROR: introdueix UNA lletra valida (A-Z)")
    rotors_llista.append(posicio_inicial1)
    while True:
        posicio_inicial2= input("digues la posicio inicial del rotor 2 (una lletra A-Z): ").strip().upper()
        if len(posicio_inicial2) == 1 and posicio_inicial2 in abecedari:
            break
        print("ERROR: introdueix UNA lletra valida (A-Z)")
    rotors_llista.append(posicio_inicial2)

    while True:
        posicio_inicial3 = input("digues la posicio inicial del rotor 3 (una lletra A-Z): ").strip().upper()
        if len(posicio_inicial3) == 1 and posicio_inicial3 in abecedari:
            break
        print("ERROR: Introdueix una lletra valida (A-Z)")
    rotors_llista.append(posicio_inicial3)
    return rotors_llista

def carregar_rotor(nom_fitxer):
    f = open(nom_fitxer, "r", encoding="utf-8")
    linies =f.read().splitlines()
    f.close()

    rotor = linies[0]
    notch = linies[1]
    return rotor, notch

def mostrar_configuracio_rotors():
    rotor1, notch1 = carregar_rotor("rotor1.txt")
    rotor2, notch2 = carregar_rotor("rotor2.txt")
    rotor3, notch3 = carregar_rotor("rotor3.txt")

    print(
        "CONFIGURACIO ROTORS:\n"
        "-------------------\n"
        "Rotor 1:"
    )
    print("  Cablejat:", rotor1)
    print("  Notch:", notch1)
    print()

    print("Rotor 2:")
    print("  Cablejat:", rotor2)
    print("  Notch:", notch2)
    print()

    print("Rotor 3:")
    print("  Cablejat:", rotor3)
    print("  Notch:", notch3)
    return rotor1, notch1, rotor2, notch2, rotor3, notch3

 

def separar5(text_netejat):
    return " ".join(text_netejat[i:i+5] for i in range(0, len(text_netejat), 5))

def xifrar_missatge(rotor1, posicio_inicial1, notch1, rotor2, posicio_inicial2, notch2, rotor3, posicio_inicial3, notch3, text):
    p_r1 = abecedari.index(posicio_inicial1)
    p_r2 = abecedari.index(posicio_inicial2)
    p_r3 = abecedari.index(posicio_inicial3)

    resultat = []

    for lletra in text.replace(" ",""):
        p_r1 = (p_r1 + 1) % MAX # Rotacío del primer rotor, sempre avança 1
        if abecedari[p_r1] == notch1: # Quan arriba al notch, comença a girar el segon rotor 1 posicio
            p_r2 = (p_r2 + 1) % MAX
            if abecedari[p_r2] == notch2: # Quan arriba al notch, comença a girar el tercer rotor 1 posicio
                p_r3 = (p_r3 + 1) % MAX
   
        index_actual = abecedari.index(lletra)

        # passar per rotor 1
        index_sortida_r1 = (p_r1 + index_actual) % MAX
        lletra_sortida_r1 = rotor1[index_sortida_r1]
        index_actual = (abecedari.index(lletra_sortida_r1) - p_r1) % MAX

        # passar per rotor 2
        index_sortida_r2 = (p_r2 + index_actual) % MAX
        lletra_sortida_r2 = rotor2[index_sortida_r2]
        index_actual = (abecedari.index(lletra_sortida_r2) - p_r2) % MAX

        # passar per rotor 3
        index_sortida_r3 = (p_r3 + index_actual) % MAX
        lletra_sortida_r3 = rotor3[index_sortida_r3]
        index_final = (abecedari.index(lletra_sortida_r3) - p_r3) % MAX

        lletra_xifrada = abecedari[index_final]
        resultat.append(lletra_xifrada)

    return separar5("".join(resultat))

def desxifrar_missatge(rotor1, posicio_inicial1, notch1, rotor2, posicio_inicial2, notch2, rotor3, posicio_inicial3, notch3, text_xifrat):
    p_r1 = abecedari.index(posicio_inicial1)
    p_r2 = abecedari.index(posicio_inicial2)
    p_r3 = abecedari.index(posicio_inicial3)

    resultat = []

    for lletra in text_xifrat.replace(" ", ""):
        p_r1 = (p_r1 + 1) % MAX # Rotacío del primer rotor, sempre avança 1
        if abecedari[p_r1] == notch1: # Quan arriba al notch, comença a girar el segon rotor 1 posicio
            p_r2 = (p_r2 + 1) % MAX
            if abecedari[p_r2] == notch2: # Quan arriba al notch, comença a girar el tercer rotor 1 posicio
                p_r3 = (p_r3 + 1) % MAX

        index_actual = abecedari.index(lletra)

        # passar per rotor 3
        index_sortida_r3 = (p_r3 + index_actual) % MAX
        lletra_sortida_r3 = abecedari[rotor3.index(abecedari[index_sortida_r3])]
        index_actual = (abecedari.index(lletra_sortida_r3) - p_r3) % MAX

        # passar per rotor 2
        index_sortida_r2 = (p_r2 + index_actual) % MAX
        lletra_sortida_r2 = abecedari[rotor2.index(abecedari[index_sortida_r2])]
        index_actual = (abecedari.index(lletra_sortida_r2) - p_r2) % MAX

        # passar per rotor 1
        index_sortida_r1 = (p_r1 + index_actual) % MAX
        lletra_sortida_r1 = abecedari[rotor1.index(abecedari[index_sortida_r1])]
        index_final = (abecedari.index(lletra_sortida_r1) - p_r1) % MAX

        resultat.append(abecedari[index_final])

    return "".join(resultat)

def generar_rotors():
    for i in range(1,4):
        nom_fitxer = f"rotor{i}.txt"

        if not os.path.exists(nom_fitxer):
            rotor = cablejat_rotors()
            pos_notch = random.randint(0,25)
            notch = rotor[pos_notch]

            with open(nom_fitxer, "w", encoding= "utf-8") as f:
                f.write(rotor + "\n")
                f.write(notch + "\n")
 
def guardar_rotor(num_rotor, rotor, notch):
   
    with open(f"rotor{num_rotor}.txt", "w", encoding = "utf-8") as f:
        f.write(rotor + "\n")
        f.write(notch + "\n")