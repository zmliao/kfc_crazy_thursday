from datetime import datetime, timedelta

def next_thursday():
    today = datetime.now()
    days_ahead = (3 + today.weekday()) % 7
    return today + timedelta(days=days_ahead)

class KFCError(Exception):
    def __init__(self, message):
        self.message = message
        super()
    

def kfc(cny):
    today = datetime.now()
    if today.weekday() != 3:
        thur_str = next_thursday().strftime("%Y-%m-%d")
        raise KFCError(f"Today Is NOT Thursday. Please Vivo Me 50 CNY on {thur_str}")
    try:
        assert cny >= 50
        print("Thank You For Vivo Me 50 CNY!")
        return cny - 50
    except Exception as e:
        raise KFCError("KFC Crazy Thursday WhoEver Vivos me 50 CNY, I Will Thank Him.")

