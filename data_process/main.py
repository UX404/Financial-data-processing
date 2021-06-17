from padding import pad
from compute_TBD import tbd

filename = '../data/processed_account_daily.csv'
padding = True
compute_tbd = True

if __name__ == '__main__':
    if padding:
        pad(filename)
        print('Padding completed.')
    if compute_tbd:
        tbd(filename)
        print('TBD computaion completed.')