import datetime

class SuperDate(datetime.datetime):
    SEASONS = {
        "Spring": (3, 4, 5),
        "Summer": (6, 7, 8),
        "Autumn": (9, 10, 11),
        "Winter": (12, 1, 2)
    }

    TIME_OF_DAY = {
        "Morning": (6, 12),
        "Day": (12, 18),
        "Evening": (18, 0),
        "Night": (0, 6)
    }

    def get_season(self):
        current_month = self.month
        for season, months in self.SEASONS.items():
            if current_month in months:
                return season

    def get_time_of_day(self):
        current_hour = self.hour
        for time_day, hours in self.TIME_OF_DAY.items():
            if hours[0] <= current_hour < hours[1]:
                return time_day

a = SuperDate(2024, 2, 22, 12)
print(a.get_season())
print(a.get_time_of_day())
