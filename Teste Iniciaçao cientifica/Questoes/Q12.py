import pandas as pd

data = {
    'Nome': [],
    'Idade': [],
    'Sexo': [],
    'Medicamento': []
}

df = pd.DataFrame(data)
df.sort_values(by='Idade',ascending=False )



print(df)
