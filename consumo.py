# Leitura da entrada
X = int(input())  # Distância total percorrida (em Km)
Y = float(input())  # Total de combustível gasto (em litros)

# Cálculo do consumo médio
consumo_medio = X / Y

# Exibindo o resultado com 3 casas decimais seguido de "km/l"
print(f"{consumo_medio:.3f} km/l")
