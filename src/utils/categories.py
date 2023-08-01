categories = {
    "Terrorism": {"bandit", "terrorist", "terrorism", "shot", "kills", "killed", "attacked", "boko haram", "herdsmen", "explosion", "attack", "separatist", "agitation", "ipob", "farmer", "fulani", "gunmen", "ISWAP", "cattle rustlers", "oil war", "militants", "troops", "pipeline explosion", "ESN", "bomb", "pirates", "sea pirates", "customs", "MASSOB", "Amotekun", "shoot", "gun" "duel"},
    "Fraud": {"cybercrime", "atm" "fraud", "internet", "forgery", "scam", "wire fraud", "financial", "yahoo boy", "impersonation", "laundering", "Money", "efcc", "forgery"},
    "Robbery": {"highway robbery", "robbery", "robbers", "bullets", "rob",  "robber",   "armed", "theft", "burglary", "steal", "thieves"},

    "Violence": {"electoral violence", "explosive", "religious", "assault", "ballot box", "cult", "communal clash", "brutality", "war",
                 "ethno-religious", "child labor", "hoodlums", "cultist", "vigilante", "kill", "decomposed corpse", "police", "victim", "security agency", "security operative",
                 "soldiers", "gang", "war", "domestic violence", "found dead", "assailants", "crisis", "mob", "raze", "ablaze", "political violence", "task force", "NSCDC", "mosque", "church",
                 "Oro", "Ifa", "traditional", "worshipper", "convoy", "students", "ritual", "NURTW", "murder", "SARS", "tussle", "lynch", "guards", "jungle" "justice", "Shiites", "pipeline", "vandal", "masquerade", "human skull",
                 "body parts", "checkpoint", "protest", "assassination", "burn", "execute"
                 },

    "Human": {"human trafficking", "slavery"},
    "Drug trafficking": {"smuggling", "drug", "drug trafficking", "ndlea"},
    "Abduction": {"kidnapping", "kidnap", "abduction", "abduct"},
    "Sexual abuse": {"rape", "raping", "baby factories", "sex", "lovers", "minor"},
    "Others crimes": {"stab", "trial", "crime", "Bribery", "dead", "Corruption", "Conspiracy", "Slander", "malpractice", "killing", "uber", "death", "police"}
}


def categorize(crime):
    for k, v in categories.items():
        if (v.intersection(set(crime))):
            print(k)
            return k
