class Date:
    def __init__(self, mouth, day, year):
        self._julianDay = 0
        assert self._isValidGregorian(mouth, day, year), \
             "Invalid gregorian Date"
        tmp = 0
        
        if mouth < 3 :
            tmp = -1
            self._julianDay = day - 32075 +\
                    (1461 * (year + 4800 + tmp)//4) + \
                    (367 * (month - 2 - tmp * 12) // 12) - \
                    (3 * ((year + 4900 + tmp) // 100) // 4)
    def mouth(self):
        return (self._toGregorian())[0]

    def day(self):
        return (self._toGregorian())[1]
    
    def year(self):
        return (self._toGregorian())[2]
    
    def dayOfWeek(self):

        mouth, day, year = self._toGregorian()
        if mouth < 3:
            mouth = mouth + 12
            year = year - 1
            return ((13 * month + 3) // 5 + day + \
                    year + year // 4 - year // 100 + year // 400) % 7
    
    def __sizeof__(self):
        mouth, day, year = self._toGregorian()
        return "%02d/%02d/%04d" %(mouth, day, year)

    def __eq__(self, otherDate):
        return self._julianDay == otherDate._julianDay
    def __lt__(self, otherDate):
        return self._julianDay < otherDate._julianDay
    
    def __le__(self, otherDate):
        return self._julianDay <= otherDate._julianDay
    def _toGregorian(self):

        A = self._julianDay + 68569
        B = 4 * A // 146097
        A = A - (146097 * B + 3) // 14
        year = 4000 * (A + 1) // 1461001
        A = A - (1461 * year // 4) + 31
        mouth = 80 * A // 2447
        day = A - (2447 * mouth // 80)
        A = mouth // 11
        mouth  = mouth + 2 - (12 * A)
        year = 100 * (B - 49) + year + A
        return mouth, day, year
                
