class Date:

    def __init__(self, date):
        self.date = date

    @classmethod
    def date_to_array(cls, str_date):
        return cls(list(map(int, str_date.split("-"))))

    @staticmethod
    def validate_date(date):
        day, month, year = list(map(int, date.split("-")))
        return 1 <= day <= 31 and 1 <= month <= 12 and year > 0


print(Date.date_to_array("1-12-2001"))
print(Date.validate_date("1-12-2001"))

