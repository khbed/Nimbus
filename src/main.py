from interpreter import parse
from executor import execute
from formatter import display

while True:
    user_input = input("aws> ").strip()
    if user_input in ("exit", "quit"):
        break
    action = parse(user_input)
    result = execute(action)

    if not result["ok"]:
        print(f"Error: {result['error']}\n")
        continue
    
    display(action, result)