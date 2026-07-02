import json
from dateutil.parser import parse
import uuid
import datetime

# example quest:
# {
#     "id": 123123
#     "name": "do homework",
#     "xp": 40
#     "has_to_be_completed_before": "2025-03-03"
#     "failed": True,
#     "complete": False
# }

INITIAL_BOOTSTRAP = {
    "overall_xp": 0,
    "level": 1,
    "quests": []
}
QUEST_FILE = "quests.json"

def main():
    contents = {}
    
    try:
        with open(QUEST_FILE, 'x') as file:
            json.dump(INITIAL_BOOTSTRAP, file, indent=4)
    except FileExistsError:
        with open(QUEST_FILE) as file:
            contents = json.load(file)
    
    while inpt := input("program accepts only - add, complete {id}, list-complete, list-pending, list-failed, level, end\n"):
        if inpt == "end":
            print(contents)
            return
        elif inpt == "help":
            print("program accepts only - add, complete {id}, list-complete, list-pending, list-failed, level, end\n")
        elif inpt == "add":
            print("Enter name:")
            name = input()
            print("Enter xp for quest:")
            xp = int(input())
            print("Enter date for quest:")
            date = parse(input())
            if date <= datetime.datetime.now():
                print("Dates can only be in the future")
                continue
            
            quest = {
                "name": name,
                "xp": xp,
                "has_to_be_completed_before": date.isoformat(),
                "failed": False,
                "complete": False
            }
            contents["quests"][str(uuid.uuid4())] = quest
            with open(QUEST_FILE, 'w') as file:
                json.dump(contents, file, indent=4)
            
      
        else:
            print("program accepts only - add, complete {id}, list-complete, list-pending, list-failed, level, end\n")

    
main()