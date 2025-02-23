# beecrowd | média aritmética ponderada
nota_A = float(input(""))
nota_B = float(input(""))
# Média ponderada
calculo_nota = ((nota_A * 3.5) + (nota_B * 7.5)) / 11 

if 0 <=nota_A <= 10 and 0 <=nota_B <= 10:
    print(f"MEDIA = {calculo_nota:.5f}")
else:
    print("Erro, insira as notas corretas!")