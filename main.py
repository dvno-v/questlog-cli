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

def main():
    file_path = "quests.json"

    contents = {}
    
    try:
        with open(file_path, 'x') as file:
            json.dump([], file, indent=4)
    except FileExistsError:
        with open(file_path) as file:
            contents = json.load(file) 
    
    while inpt := input():
        if inpt == "end":
            print(contents)
            return
        elif inpt == "help":
            print("program accepts only - add, complete {id}, list-complete, list-pending, list-failed, level, end")
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
                "has_to_be_completed_before": date,
                "failed": False,
                "complete": False,
                "id": str(uuid.uuid4())
            }
            print(quest)
        else:
            print("program accepts only - add, complete {id}, list-complete, list-pending, list-failed, level, end")

    
main()