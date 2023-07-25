
import pandas as pd

data = {
    'Nome': ['Ana', 'Bartolomeu', 'Caio', 'Dora'],
    'Idade': [28, 32, 25, 60],
    'Sexo': ['F', 'M', 'F', 'F'],
    'Medicamento': ['A', 'B', 'A', 'B']
}

df = pd.DataFrame(data)
print(df)