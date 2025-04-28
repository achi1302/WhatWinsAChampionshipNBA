import pandas as pd
import numpy as np
import matplotlib.pyplot as plt

weight = [78, 75, 83, 85, 87]
height = [1.83, 1.78, 1.75, 1.69, 1.72]
npweight = np.array(weight)
npheight = np.array(height)
bmi = npweight / npheight ** 2
print(bmi)

NACountries = {"Mexico": {"population": 1.56, "capital": "CDMX"},
                "USA": {"population": 10.21, "capital": "Washigton D.C"},
                "Canda": {"population": 5.82, "capital": "Ottowa"}}
print(NACountries['Mexico']['population'])

dict = {
	"country": ["Brazil", "Rusia", "India", "China"],
	"capital": ["Brasilia", "Moscow", "New Delhi", "Beijing"],
	"population": ["200.4", "143.5", "1252", "1357"]
}
df = pd.DataFrame(dict)
df.index = ["BR", "RU", "IN", "CH"]
print(df.loc[['BR', 'RU'], ['capital']])