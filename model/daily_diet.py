from datetime import datetime
from pytz import timezone

class DailyDiet:
    _next_id = 0

    def __init__(self, name, description, diet_is_value=False):
        DailyDiet._next_id +=1

        self.id = DailyDiet._next_id
        self.name = name
        self.description = description
        self.diet_is_value = diet_is_value
        self.data_time_created = self.__get_current_date_and_time()
    
    def __get_current_date_and_time(self):
        date_time = datetime.now()
        time_zone = timezone('America/Sao_Paulo')
        time_zone_sao_paulo = date_time.astimezone(time_zone)
        return time_zone_sao_paulo.strftime('%d/%m/%Y %H:%M:%S')
    
    def to_dict(self):
        return {
            "id": self.id,
            "name": self.name,
            "description": self.description,
            "diet_is_value": self.diet_is_value,
            "date_time": self.data_time_created
        }
