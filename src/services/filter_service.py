from datetime import datetime

def filter_races_by_date(races_data):
    hoje = datetime.now().date()
    past_races = []
    upcoming_races = []
    
    for race in races_data:
        race_date = datetime.strptime(race['data_agendamento'], '%d/%m/%Y').date()
        if race_date < hoje:
            past_races.append(race)
        else:
            upcoming_races.append(race)
    
    return past_races, upcoming_races