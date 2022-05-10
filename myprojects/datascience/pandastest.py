import pandas as pd
expenditure = {'when': ['01/01/2022', '01/05/2022', '01/20/2022'], 
               'cost': [733,180,45],
               'what': ['health insurance', 'eletric bill', 'gas bill' ],
               'font': [13,13,13],
               'payment': [19,19,19],
               }
expenditure_df = pd.DataFrame(expenditure)
print(expenditure_df)