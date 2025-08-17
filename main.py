from reader import Reader
from person import *

if __name__ == "__main__":
    reader = Reader()
    participants = reader.get_participants()
    for participant in participants:
        print()
        print(participant)
        print("-" * 40)  # Separator for readability