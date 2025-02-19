## 📂 Estruturas de Dados em Python  

As **estruturas de dados** são usadas para armazenar e organizar informações de forma eficiente.  

### 🔹 Listas (`list`)  

Uma **lista** armazena múltiplos valores em uma única variável.  

```python
numeros = [1, 2, 3, 4, 5]
print(numeros[0])  # Acessa o primeiro elemento
numeros.append(6)  # Adiciona um elemento
```

### Métodos úteis:  

```python
numeros.remove(3)  # Remove um valor
numeros.sort()     # Ordena a lista
print(len(numeros)) # Retorna o tamanho da lista
```

---

### 🔹 Tuplas (`tuple`)  

Tuplas são semelhantes às listas, mas são **imutáveis**.  

```python
coordenadas = (10, 20)
print(coordenadas[0])  # Acessa o primeiro elemento
```

---

### 🔹 Conjuntos (`set`)  

Conjuntos armazenam valores **únicos** e **não ordenados**.  

```python
numeros_unicos = {1, 2, 3, 3, 4}
print(numeros_unicos)  # Saída: {1, 2, 3, 4}
```

---

### 🔹 Dicionários (`dict`)  

Dicionários armazenam **pares chave-valor**.  

```python
pessoa = {"nome": "Vinicius", "idade": 19}
print(pessoa["nome"])  # Saída: Vinicius
```

#### Adicionando e modificando valores:  

```python
pessoa["altura"] = 1.89
pessoa["idade"] = 20
```

---

Essas são as principais estruturas de dados!
