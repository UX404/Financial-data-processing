class DateCounter():
    def __init__(self, date):  # date: '2021/06/05'
        date = date.split('/')
        self.year = int(date[0])
        self.month = int(date[1])
        self.day = int(date[2])
    def count(self):
        # day++
        self.day += 1
        if (self.day == 32) and (self.month in [1, 3, 5, 7, 8, 10, 12]):
            self.month += 1
            self.day = 1
        elif (self.day == 31) and (self.month in [4, 6, 9, 11]):
            self.month += 1
            self.day = 1
        elif (self.day == 30) and (self.month == 2) and ((self.year % 100 != 0 and self.year % 4 == 0) or self.year % 400 == 0):
            self.month += 1
            self.day = 1
        elif (self.day == 29) and (self.month == 2) and not ((self.year % 100 != 0 and self.year % 4 == 0) or self.year % 400 == 0):
            self.month += 1
            self.day = 1
        # month++
        if (self.month == 13):
            self.year += 1
            self.month = 1
    def current_date(self):
        return '%d/%d/%d' % (self.year, self.month, self.day)