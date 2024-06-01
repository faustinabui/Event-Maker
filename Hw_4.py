from Date import Date
from Event import Event


def main():
    events = []

    while True:
        print("\n1. Add an Event")
        print("2. Cancel an Event")
        print("3. View all Events")
        print("4. Quit")
        choice = input("Choose an option (1-4): ")

        if choice == "1":
            try:
                day = int(input("Enter day: "))
                month = int(input("Enter month: "))
                year = int(input("Enter year: "))
                event_name = input("Enter event name: ")
                start_hour = int(input("Enter start hour (0-23): "))
                end_hour = int(input("Enter end hour (0-23): "))

                event_date = Date(day, month, year)
                new_event = Event(event_name, start_hour, end_hour, event_date)

                overlap = False
                for event in events:
                    if event.event_date == new_event.event_date:
                        if (event.start_hour <= new_event.start_hour < event.end_hour) or \
                                (event.start_hour < new_event.end_hour <= event.end_hour):
                            overlap = True
                            print("Overlap detected with: ", event)
                            break

                if not overlap:
                    events.append(new_event)
                    print("Event added successfully!")
                else:
                    print("Event overlaps with an existing event. Not added.")
            except ValueError as e:
                print(f"Invalid input: {e}")

        elif choice == "2":
            event_to_cancel = input("Enter the name of the event to cancel: ")
            event_found = False
            for event in events:
                if event.event_name == event_to_cancel:
                    events.remove(event)
                    event_found = True
                    print(f"Cancelled event '{event_to_cancel}'")
                    break

            if not event_found:
                print(f"No event named '{event_to_cancel}' found.")

        elif choice == "3":
            if not events:
                print("No events scheduled.")
            else:
                print("All Events:")
                for event in events:
                    print(event)

        elif choice == "4":
            print("Exiting program.")
            break

        else:
            print("Invalid choice. Please choose a number between 1 and 4.")


main()
