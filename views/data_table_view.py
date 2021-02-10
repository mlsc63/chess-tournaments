import pandas as pd


class DataTableView:

    def __init__(self, data, index, columns):
        self.index = index
        self.columns = columns
        self.data = data

    def display(self):
        data_df = pd.DataFrame(self.data, self.index, self.columns)
        print(data_df)
        print('Appuyer sur une touche pour continuer ')
        input()
