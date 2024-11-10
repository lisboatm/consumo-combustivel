# Desafio: Consumo de Combustível 🚗⛽

## Descrição
O desafio consiste em calcular o consumo médio de combustível de um automóvel, dado a distância total percorrida e o total de combustível gasto. O objetivo é apresentar o resultado com 3 casas decimais, seguido da unidade de medida "km/l".

## Entrada
O programa receberá dois valores:

1. **X**: um valor inteiro representando a distância total percorrida em quilômetros (Km).
2. **Y**: um valor real representando o total de combustível gasto em litros (L), com um dígito após o ponto decimal.

### Exemplo de Entrada
```
500
35.0
```

## Saída
O programa deverá calcular o consumo médio do automóvel utilizando a fórmula:

\[ \text{consumo médio} = \frac{X}{Y} \]

O resultado deve ser apresentado com **3 casas decimais**, seguido da unidade "km/l".

### Exemplo de Saída
```
14.286 km/l
```

## Explicação
- Dado que o automóvel percorreu 500 Km e consumiu 35.0 L de combustível, o cálculo será:
  \[
  \frac{500}{35.0} = 14.2857142857 \ldots
  \]
- O resultado é arredondado para 3 casas decimais, resultando em **14.286 km/l**.

## Como Executar o Programa
1. Certifique-se de ter o Python instalado em sua máquina.
2. Salve o código em um arquivo (por exemplo, `consumo.py`).
3. Abra o terminal, navegue até o diretório onde o arquivo está salvo e execute:
   ```bash
   python consumo.py
   ```
4. Insira os valores de entrada conforme o solicitado.

## Código em Python
```python
# Leitura dos valores de entrada
X = int(input())
Y = float(input())

# Cálculo do consumo médio
consumo_medio = X / Y

# Exibindo o resultado com 3 casas decimais
print(f"{consumo_medio:.3f} km/l")
```

## Explicação do Código
1. **Leitura dos dados**: Os valores `X` e `Y` são lidos do input.
2. **Cálculo**: A fórmula do consumo médio é aplicada (`X / Y`).
3. **Saída formatada**: O resultado é exibido com 3 casas decimais usando `f"{valor:.3f}"`.

## Testes Adicionais
### Entrada:
```
2254
124.4
```
### Saída:
```
18.119 km/l
```

### Entrada:
```
4554
464.6
```
### Saída:
```
9.802 km/l
```
