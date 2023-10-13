from collections import Counter

# Sua lista de elementos
minha_lista = ['dig', 'earthquake', 'earthquake', 'cut', 'cut', 'cut', 'fly', 'fly', 'fly', 'fly']

# Use Counter para contar as repetições
contagem = Counter(minha_lista)

# Exiba os resultados em ordem decrescente de frequência
resultados_ordenados = sorted(contagem.items(), key=lambda item: item[1], reverse=True)
#print(resultados_ordenados[1][0])






