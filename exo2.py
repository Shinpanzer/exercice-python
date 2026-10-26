
taille = float(input("Ta taille en mètres : "))
poids = float(input("Ton poids en kg : "))


if taille > 0 :
    imc = poids / (taille ** 2)
    print(f"Ton IMC est de {imc:.2f}")

else:
     print("ERREUR: la taille doit être strictement positive")