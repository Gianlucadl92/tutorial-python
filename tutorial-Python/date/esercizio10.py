from datetime import datetime

def settimana_anno(data):
    anno, num_settimana, _ = data.isocalendar()
    return f"Anno {anno}, settimana {num_settimana}"

data = datetime(2022, 5, 1)
print(settimana_anno(data))