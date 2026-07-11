events = []


def record(code):

    events.append(code)


def show():

    print("\nVisit History")
    print("-" * 20)

    for item in events:
        print(item)
