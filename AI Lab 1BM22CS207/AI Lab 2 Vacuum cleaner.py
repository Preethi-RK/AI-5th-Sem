agent_table = {
    ('Clean', 'A'): 'MoveRight',
    ('Clean', 'B'): 'MoveLeft',
    ('Dirty', 'A'): 'Suck',
    ('Dirty', 'B'): 'Suck',
}

class VacuumCleaner:
    def __init__(self, location='A', status='Clean'):
        self.location = location
        self.status = status

    def act(self, action):
        if action == 'MoveRight':
            self.location = 'B'
        elif action == 'MoveLeft':
            self.location = 'A'
        elif action == 'Suck':
            self.status = 'Clean'

if __name__ == "__main__":
    status_A = input("Enter the status of room A (Clean/Dirty): ").strip().capitalize()
    status_B = input("Enter the status of room B (Clean/Dirty): ").strip().capitalize()

    vacuum = VacuumCleaner(location='A', status=status_A)

    while status_A == 'Dirty' or status_B == 'Dirty':
        action = agent_table.get((vacuum.status, vacuum.location), 'NoOp')
        print(f"Percept: {vacuum.status}, Action: {action}")

        if action != 'NoOp':
            vacuum.act(action)

            # Update the status of the rooms based on the vacuum's actions
            if action == 'Suck':
                if vacuum.location == 'A':
                    status_A = 'Clean'
                else:
                    status_B = 'Clean'

        # Update vacuum status based on the current room status
        vacuum.status = status_A if vacuum.location == 'A' else status_B

        print(f"Location: {vacuum.location}, Status A: {status_A}, Status B: {status_B}")

    print("Both rooms are clean!")

