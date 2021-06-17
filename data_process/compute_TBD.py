import csv

def tbd(filename: str):
    #---------------read_in---------------
    data = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    #-------------compute_TBD-------------
    newdata = []
    newdata.append(data[0] + ['TBD'])
    current_id, n_initial = '-1', -1
    for n in range(1, len(data)):
        if data[n][0] != current_id:  # 新用户
            current_id = data[n][0]
            n_initial = n
        if (n - n_initial < 27) or data[n][6] == '0':  # 差28天以内无法计算，equity为0无法计算
            newdata.append(data[n].copy() + ['-1'])
        else:
            close_pl = sum([float(data[m][7]) for m in range(n-26, n+1)])
            open_pl_start = float(data[n-27][8])
            open_pl_end = float(data[n][8])
            equity = float(data[n][6])
            tbd_result = (close_pl + open_pl_end - open_pl_start) / equity
            newdata.append(data[n].copy() + [str(tbd_result)])
    #--------------write_back--------------
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(newdata)