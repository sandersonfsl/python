import pandas as pd
rating = {'date' : ['03/05/2022', '05/05/2022', '08/05/2022'],
         'name' : ['matafina', 'cubansandwich', 'pichardo'],
         'price' :['35','29','40'],
         'rate' : ['8','9','7'], }

rating_df = pd.DataFrame(rating)
print(rating_df)