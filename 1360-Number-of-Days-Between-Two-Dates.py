class Solution(object):
    def daysBetweenDates(self, date1, date2):
        """
        :type date1: str
        :type date2: str
        :rtype: int
        """
        def f(date):
            # leep
            date_list = date.split("-")

            days = 0
            for y in range(1900, int(date_list[0])):
                if y % 4 == 0 and y % 100 != 0 or y % 400 == 0:
                    days += 366
                else:
                    days += 365
            for m in range(1, int(date_list[1])):
                if m in [1, 3, 5, 7, 8, 10, 12]:
                    days += 31
                elif m in [4, 6, 9, 11]:
                    days += 30
                else:
                    if int(date_list[0]) % 4 == 0 and int(date_list[0]) % 100 != 0 or int(date_list[0]) % 400 == 0:
                        days += 29
                    else:
                        days += 28
            days += int(date_list[2])
            return days

        return abs(f(date1) - f(date2))