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
    "quests": {}
}
QUEST_FILE = "quests.json"

def main():
    contents = INITIAL_BOOTSTRAP
    
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
            write_contents_to_file(QUEST_FILE, contents)
        elif inpt == "list-complete":
            completed_ids = [x for x in contents["quests"] if contents["quests"][x]["complete"]]
            for id in completed_ids:
                print(contents["quests"][id])
        elif "complete" in inpt:
            splitted = inpt.split()
            quest_id = splitted[1]

            if quest_id not in contents["quests"]:
                print("quest not found")
                continue

            if contents["quests"][quest_id]["complete"]:
                print("quest already completed")
                continue
            
            if parse(contents["quests"][quest_id]["has_to_be_completed_before"]) < datetime.datetime.now():
                print("cannot complete quests, date has expired")
                contents["quests"][quest_id]["complete"] = False
                contents["quests"][quest_id]["failed"] = True
            
            else:
                contents["quests"][quest_id]["complete"] = True
                contents["overall_xp"] += contents["quests"][quest_id]["xp"]
                contents["level"] = max(contents["overall_xp"] // 100, 1)
                
            write_contents_to_file(QUEST_FILE, contents)
        
        else:
            print("program accepts only - add, complete {id}, list-complete, list-pending, list-failed, level, end\n")

    
def write_contents_to_file(file_path, contents):
    with open(file_path, 'w') as file:
        json.dump(contents, file, indent=4)
    
main()