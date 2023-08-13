def yardForMeter(yards):
    meters = yards * 0.9144
    return meters

def yardForFeet(yard):
    feet = yard * 3
    return feet

def feetForMeter(feet):
    meter = feet * 0.3048
    return meter

opcoes = {
    1: ("Jarda para Metros", yardForMeter),
    2: ("Jarda para Pés", yardForFeet),
    3: ("Pés para Metros", feetForMeter)
}

# Solicita ao usuário a escolha da conversão
print("Escolha a conversão:")
print("1 - Jarda para Metros")
print("2 - Jarda para Pés")
print("3 - Pés para Metros")
inputOption = int(input("Digite o número da opção: "))

if inputOption == 1:
    yards = float(input("Digite o valor em jardas: "))
    meters = yardForMeter(yards)
    print(f"{yards} jardas equivalem a {meters} metros.")
elif inputOption == 2:
    yard = float(input("Digite o valor em jardas: "))
    feet = yardForFeet(yard)
    print(f"{yard} jardas equivalem a {feet} pés.")
elif inputOption == 3:
    feet = float(input("Digite o valor em pés: "))
    meters = feetForMeter(feet)
    print(f"{feet} pés equivalem a {meters} metros.")
else:
    print("Opção inválida.")