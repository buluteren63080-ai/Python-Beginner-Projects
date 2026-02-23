nostromo_crew = [
    {"name": "Ripley", "department": "Security", "status": "Alive"},
    {"name": "Dallas", "department": "Command", "status": "Missing"},
    {"name": "Ash", "department": "Science", "status": "Malfunctioning"},
    {"name": "Parker", "department": "Engineering", "status": "Alive"},
    {"name": "Brett", "department": "Engineering", "status": "Missing"}
]

def alive_or_not_check(N_crew):
    crew = N_crew["status"]

    match crew:
        case "Alive":
            return True
        case _ :
            return False

alive_members = [*filter(alive_or_not_check, nostromo_crew)]
members_for_escape_pod = [names["name"] for names in alive_members]

print(members_for_escape_pod)
