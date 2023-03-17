import pandas as pd

class Treat_csv():

    def __init__(self, file_location, month, year):
        self.df = pd.read_csv(file_location)
        self.month = month
        self.year = year
        

    def show_csv(self):
        print(self.df)


    def sum_val_f_m_y(self):
        '''filter df by month, year and sum all values'''
        f_m_df = self.df.loc[self.df.month == self.month]
        f_m_y_df = f_m_df.loc[f_m_df.year == self.year]
        self.sum_f_m_y_df = f_m_y_df['value'].sum()
        print(f'\n -  in {self.month}/{self.year} = R$ {self.sum_f_m_y_df} ')

    def show_balance(self):
        return self.sum_f_m_y_df
