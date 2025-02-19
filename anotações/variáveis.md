## 🔢 Variáveis e tipos de dados em Python  

As **variáveis** são usadas para armazenar valores que podem ser reutilizados no programa.  

### 🔹 Declarando Variáveis  

```python
nome = "Vinicius"
idade = 19
altura = 1.90
peso = 70.0
ativo = True
```

### 🔹 Principais Tipos de Dados  

| Tipo     | Descrição        | Exemplo |
|----------|-----------------|---------|
| `int`    | Números inteiros | `10`    |
| `float`  | Números decimais | `3.14`  |
| `str`    | Texto (string)   | "Olá"   |
| `bool`   | Booleano (V/F)   | `True`  |

### 🔹 Conversão de Tipos  

```python
idade = "19"
idade_numero = int(idade)  # Converte para inteiro
altura_texto = str(altura)  # Converte para string
```

### 🔹 Entrada e Saída de Dados  

```python
nome = input("Digite seu nome: ")
print(f"Olá, {nome}!")
```

Agora que sabemos manipular variáveis, pule para **estruturas de dados**
