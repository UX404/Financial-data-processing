import csv
from utils import DateCounter

def pad(filename: str):
    #---------------read_in---------------
    data = []
    with open(filename, mode='r') as file:
        reader = csv.reader(file)
        for row in reader:
            data.append(row)
    #---------------padding---------------
    newdata = []
    newdata.append(data[0])
    for n in range(1, len(data)-1):
        counter = DateCounter(data[n][1])
        counter.count()
        # print(counter.current_date())
        if (data[n][0] != data[n+1][0]) or (counter.current_date() == data[n+1][1]):  # 用户变更，或日起连续，不需要补齐
            newdata.append(data[n])
        else:
            newdata.append(data[n])
            while counter.current_date() != data[n+1][1]:
                newdata.append(data[n].copy())
                newdata[-1][1] = counter.current_date()
                counter.count()
    #--------------write_back--------------
    with open(filename, mode='w', newline='') as file:
        writer = csv.writer(file)
        writer.writerows(newdata)