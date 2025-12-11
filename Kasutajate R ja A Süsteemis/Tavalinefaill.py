from MyModule import *
kasutajad, paroolid = lae_andmed()

while True:
    print("\n--- MENÜÜ","-" * 30)
    print("1 – Registreerimine")
    print("2 – Autoriseerimine")
    print("3 – Nime või parooli muutmine")
    print("4 – Parooli taastamine")
    print("5 – Lõpetamine")
    print("-" * 40)

    valik = input("Vali tegevus: ")

    if valik == "1":
        registreeri(kasutajad, paroolid)
    elif valik == "2":
        logi_sisse(kasutajad, paroolid)
    elif valik == "3":
        muuda_andmeid(kasutajad, paroolid)
    elif valik == "4":
        taasta_parool(kasutajad, paroolid)
    elif valik == "5":
        print("Programmi töö lõppes.")
        break
    else:
        print("Vale valik!")
