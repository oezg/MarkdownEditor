import sys

def rows():
    while True:
        try:
            row = int(input("Number of rows: "))
        except ValueError:
            print("The number of rows should be a positive number")
        else:
            if row > 0:
                return row
            else:
                print("The number of rows should be greater than zero")


def format(formatter):
    if formatter == "plain":
        return input("Text: ")
    elif formatter == "bold":
        return "**" + input("Text: ") + "**"
    elif formatter == "italic":
        return "*" + input("Text: ") + "*"
    elif formatter == "header":
        while True:
            try:
                level = int(input("Level: "))
            except ValueError:
                print("The level should be a number between 1 and 6")
            else:
                if 0 < level < 7:
                    break
                else:
                    print("The level should be within the range of 1 to 6")
        return "#" * level + " " + input("Text: ") + "\n"
    elif formatter == "link":
        label = input("Label: ")
        return "[" + label + "](" + input("URL: ") + ")"
    elif formatter == "inline-code":
        return "`" + input("Text: ") + "`"
    elif formatter == "ordered-list":
        return "\n".join(f"{i+1}. {input()}" for i in range(rows())) + "\n"
    elif formatter == "unordered-list":
        return "\n".join(f"* {input()}" for _ in range(rows())) + "\n"
    else:
        return "\n"
    

markdown = ""
formatters = "plain bold italic header link inline-code new-line ordered-list unordered-list !done !help"
formatters = set(formatters.split())

while True:
    formatter = input("Choose a formatter: ")
    
    while formatter not in formatters:
        print("Unknown formatting type or command")
        formatter = input("Choose a formatter: ")
    
    if formatter == "!done":
        file = open("output.md", "w")
        file.write(markdown)
        file.close()
        sys.exit()
    elif formatter == "!help":
        print(
            "Available formatters: plain bold italic header link "
            "inline-code new-line ordered-list unordered-list \n"
            "Special commands: !help !done"
            )
    else:
        markdown += format(formatter)
        print(markdown)
