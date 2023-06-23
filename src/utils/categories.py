categories = {
    "Terrorism": {"bandit","terrorist", "terrorism", "boko haram", "herdsmen", "explosion", "attack", "separatist", "agitation", "ipob"},
    "Fraud":{"cybercrime", "atm" "fraud", "internet", "forgery", "scam", "wire fraud", "financial", "yahoo boy", "impersonation", "laundering", "Money", "efcc", "forgery"},
    "Robbery": {"highway robbery", "robbery", "armed", "theft", "burglary","steal"},
    "Violence" :{"electoral violence", "explosive", "religious", "assault", "ballot box", "cult", "communal clash", "brutality", "war"},
    "Human": {"human trafficking", "slavery"},
    "Drug trafficking": {"smuggling", "drug", "drug trafficking", "ndlea"},
    "Abduction":{"kidnapping", "kidnap", "abduction", "abduct"},
    "Sexual abuse": {"rape","raping", "baby factories", "sex"},
    "Others crimes":{"murder", "stab", "ritual", "trial", "crime", "Bribery", "Corruption", "Conspiracy", "Slander", "malpractice", "killing", "uber", "burn","death", "police" }
}

def categorize(crime):   
    for k, v in categories.items():
        if (v.intersection(set(crime))): 
            print(crime)
            return k
        