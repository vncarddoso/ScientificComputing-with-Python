def arithmetic_arranger(problems, solve=False):
    # 1️ Verificar se há mais de 5 problemas
    if len(problems) > 5:
        return "Error: Too many problems."

    # Inicializando as listas para armazenar as linhas
    first_line = []
    second_line = []
    dashes = []
    results = []

    # 2️ Percorrer cada problema
    for problem in problems:
        parts = problem.split()
        
        # 3️ Separar os números e o operador
        num1, operator, num2 = parts

        # 4️ Validar o operador
        if operator not in ("+", "-"):
            return "Error: Operator must be '+' or '-'."

        # 5️ Validar se os números são dígitos
        if not (num1.isdigit() and num2.isdigit()):
            return "Error: Numbers must only contain digits."

        # 6️ Validar se os números têm no máximo 4 dígitos
        if len(num1) > 4 or len(num2) > 4:
            return "Error: Numbers cannot be more than four digits."

        # 7️ Determinar o espaçamento
        width = max(len(num1), len(num2)) + 2
        top = num1.rjust(width)
        bottom = operator + " " + num2.rjust(width - 2)
        line = "-" * width

        # Adicionar à lista de cada linha
        first_line.append(top)
        second_line.append(bottom)
        dashes.append(line)

        # 8️ Resolver a operação se solve=True
        if solve:
            result = str(eval(num1 + operator + num2)).rjust(width)
            results.append(result)

    # 9️ Criar a saída formatada
    arranged_problems = "\n".join([
        "    ".join(first_line),
        "    ".join(second_line),
        "    ".join(dashes),
    ])

    # Adicionar a linha de resultados, se necessário
    if solve:
        arranged_problems += "\n" + "    ".join(results)

    return arranged_problems

# Testes:
print(arithmetic_arranger(["32 - 698", "1 - 3801", "45 + 43", "123 + 49", "988 + 40"], True))
