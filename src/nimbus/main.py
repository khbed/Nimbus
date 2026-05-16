from nimbus.interpreter import parse
from nimbus.executor import execute
from nimbus.formatter import display

def main():
    print("Nimbus — type 'exit' to quit\n")

    while True:
        user_input = input("aws> ").strip()

        if not user_input:
            continue

        if user_input.lower() in ("exit", "quit"):
            print("Bye!")
            break

        action = parse(user_input)

        if action is None:
            print("Not sure what to do with that. Try: list lambdas, list ec2, list s3\n")
            continue

        result = execute(action)

        if not result["ok"]:
            print(f"Error: {result['error']}\n")
            continue

        display(action, result)

if __name__ == "__main__":
    main()