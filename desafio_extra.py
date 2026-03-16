import pandas as pd
import matplotlib.pyplot as plt
import seaborn as sns

# 1. Importação dos dados
df = pd.read_csv('titanic_dataset.csv')

# 2. Compreensão e Limpeza (Tratamento de valores nulos)
print("--- Informações Gerais ---")
print(df.info())

# Verificando valores nulos
print("\n--- Valores Nulos por Coluna ---")
print(df.isnull().sum())

# Tratamento básico: preencher idades nulas com a média
df['Age'] = df['Age'].fillna(df['Age'].mean())

# 3. Análise Exploratória (Exemplo de Groupby)
# Taxa de sobrevivência por classe (Pclass)
sobrevivencia_classe = df.groupby('Pclass')['Survived'].mean()
print("\n--- Taxa de Sobrevivência por Classe ---")
print(sobrevivencia_classe)

# 4. Visualização Gráfica
plt.figure(figsize=(8, 6))
sns.barplot(x='Pclass', y='Survived', data=df)
plt.title('Taxa de Sobrevivência por Classe de Passageiro')
plt.ylabel('Proporção de Sobreviventes')
plt.xlabel('Classe (1ª, 2ª ou 3ª)')

# Salva o gráfico como imagem
plt.savefig('grafico_sobrevivencia.png')
plt.show()

print("\nAnálise inicial concluída e gráfico gerado!")