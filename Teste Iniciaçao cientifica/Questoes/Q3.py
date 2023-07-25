import numpy as np


arr1 = np.arange(1,5001)

maiorValor = None
for elemento in arr1:

    if maiorValor == None or elemento > maiorValor:
       maiorValor = elemento

print(maiorValor)

    


   