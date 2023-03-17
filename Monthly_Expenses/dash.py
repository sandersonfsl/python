from main_classes import Treat_csv

# change the two arguments (1 and 2020) to desired month and year
expenses_df = Treat_csv("./csvs_files/expenses.csv", 1, 2020)
incomes_df = Treat_csv("./csvs_files/incomes.csv", 1, 2020)


print('\n\033[34m- Expenses Table -\033[m\n')
expenses = expenses_df.show_csv()
print(' ')

print('\n\033[34m- Incomes Table -\033[m\n')
income = incomes_df.show_csv()


print('\n\033[34mSUM OF EXPENSES\033[m')
expenses_df.sum_val_f_m_y()

print('\n\033[34mSUM OF INCOMES \033[m')
incomes_df.sum_val_f_m_y()


print('\n\033[34mBALANCE \033[m')

balance = incomes_df.show_balance() - expenses_df.show_balance()
print(f'\n -  R$ {balance}')



