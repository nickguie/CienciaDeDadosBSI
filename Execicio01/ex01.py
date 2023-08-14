def yardForMeter(yards):
    meters = yards * 0.9144
    return meters

def yardForFoot(yard):
    foot = yard * 3
    return foot

def footForMeter(foot):
    meter = foot * 0.3048
    return meter

def footForYard(foot):
    yards = foot / 3
    return yards

def meterForYard(meters):
    yards = meters / 0.9144
    return yards

def meterForFoot(meters):
    foot = meters / 0.3048
    return foot

def invalidOption():
    print("Opção INVÁLIDA")

conversorOptions = {
    "metro": ("Metro", {"jarda": meterForYard, "pes": meterForFoot}),
    "pes": ("Pés", {"jarda": footForYard, "metro": footForMeter}),
    "jarda": ("Jarda", {"metro": yardForMeter, "pes": yardForFoot})
}

print("Escolha a unidade de entrada:")
for key, (description, _) in conversorOptions.items():
    print(f"- {key}")

input_unit = input("Digite a unidade de entrada: ")

if input_unit not in conversorOptions:
    invalidOption()
else:
    value = float(input("Digite o valor: "))
    
    print("Escolha a unidade de saída:")
    for key in conversorOptions[input_unit][1]:
        print(f"- {key}")
    
    output_unit = input("Digite a unidade de saída: ")

    if output_unit not in conversorOptions[input_unit][1]:
        invalidOption()
    else:
        conversion_function = conversorOptions[input_unit][1][output_unit]
        result = conversion_function(value)

        print(f"{value} {conversorOptions[input_unit][0]} equivalem a {result:.3f} {output_unit}.")