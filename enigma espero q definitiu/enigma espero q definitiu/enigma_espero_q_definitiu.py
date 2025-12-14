from definicions import generar_rotors,pantalla_inici, abans_xifrar,mostrar_configuracio_rotors,posicio_inicial_rotors,xifrar_missatge,desxifrar_missatge,carregar_rotor,cablejat_rotors,guardar_rotor
while True:
    generar_rotors()
    pantalla_inici()
    user_num = int(input("Introdueix una de les opcions: "))
    if user_num == 1:
        text_original = input("Introdueix el text que vols xifrar: ")
        text_netejat = abans_xifrar(text_original)
        with open("Missatge.txt", "w", encoding="utf-8") as fitxer:
            fitxer.write(text_original)
        config_rotors = mostrar_configuracio_rotors()
        rotor1, notch1, rotor2, notch2, rotor3, notch3 = config_rotors

        posicio_inicial1, posicio_inicial2, posicio_inicial3 = posicio_inicial_rotors()
        text_xifrat = xifrar_missatge(rotor1, posicio_inicial1, notch1, rotor2, posicio_inicial2, notch2, rotor3, posicio_inicial3, notch3, text_netejat)
        with open("Xifrat.txt", "w", encoding="utf-8") as fitxer:
            fitxer.write(text_xifrat)
        print(text_xifrat)

    elif user_num == 2:
        print("Desxifrar misstage")
        
        text_xifrat_amb_espais = input("Introdueix el text xifrat (en grups de 5): ")
        text_xifrat_net = text_xifrat_amb_espais.replace(" ", "").upper()
        text_desxifrat = desxifrar_missatge(rotor1, posicio_inicial1, notch1, rotor2, posicio_inicial2, notch2, rotor3, posicio_inicial3, notch3, text_xifrat_net)
        with open("Desxifrat.txt", "w", encoding="utf-8") as fitxer:
            fitxer.write(text_desxifrat)
        print("Missatge desxifrat guardat a Desxifrat.txt\n")
        print(text_desxifrat.replace(" ", ""))

    elif user_num == 3:
        print("\nEDITAR ROTORS\n ------------------")

        while True:
            num_rotor = input("Quin rotor vols editar? (1, 2 o 3): ")
            if num_rotor in ("1", "2", "3"):
                break
            else:
                print("ERROR: Introdueix 1, 2 o 3")

        rotor_actual, notch_actual = carregar_rotor(f"rotor{num_rotor}.txt")

        print("\nRotor actual:")
        print("Cablejat:", rotor_actual)
        print("Notch:", notch_actual)

        print("\nQue vols fer?")
        print("1. Generar nou cablejat")
        print("2. Canviar notch")
        print("3. Generar tot de nou")

        opcio = input("Escull una opcio (1-3): ")

        if opcio == "1":
            rotor_nou = cablejat_rotors()
            notch_nou = notch_actual

        elif opcio == "2":
            while True:
                notch_nou = input("Introdueix el nou notch (A-Z): ").upper()
                if len(notch_nou) == 1 and notch_nou in abecedari:
                    break
                print("ERROR: Notch invalid")
            rotor_nou = rotor_actual

        elif opcio == "3":
            rotor_nou = cablejat_rotors()
            notch_nou = rotor_nou[random.randint(0, 25)]

        else:
            print("Opcio invalida")
            continue

        (num_rotor, rotor_nou, notch_nou)

        print("\n Rotor actualitzat correctament!")
