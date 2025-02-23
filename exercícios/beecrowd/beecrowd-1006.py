# beecrowd | média aritmética ponderada 2
nota_A = float(input(""))
nota_B = float(input(""))
nota_C = float(input(""))
# Média ponderada
calculo_nota = ((nota_A * 2) + (nota_B * 3) + (nota_C * 5)) / 10 

if 0 <=nota_A <= 10 and 0 <=nota_B <= 10 and 0 <= nota_C <= 10:
    print(f"MEDIA = {calculo_nota:.1f}")
else:
    print("Erro, insira as notas corretas!")