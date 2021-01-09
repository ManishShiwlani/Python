class Elevator:
    def __init__(self, floors):
        self.floors = floors
        self.buttons = [False]*floors
        self.state = 'stopped' # 'up', 'down', 'stopped'
        self.current_floor = 0

    def any_floor_selected(self, dir):
        if dir is 'up':
            return True in self.buttons[self.current_floor:]
        elif dir is 'down':
            return True in self.buttons[:self.current_floor]

    def other_dir(self, dir):
        return 'up' if dir is 'down' else 'down'

    def next_action(self):
        if self.state == 'stopped':
            for dir in ['up', 'down']:
                if self.any_floor_selected(dir):
                    self.set_next_state(dir)
        else:
            dir = self.state
            if self.any_floor_selected(dir):
                self.set_next_state(dir)
            else:
                if self.any_floor_selected(self.other_dir(dir)):
                    self.set_next_state(self.other_dir(dir))
                else:
                    self.set_next_state('stopped')

    def set_next_state(self, state):
        self.state = state

    def arrived_floor(self, floor):
        if self.buttons[floor]:
            print('open door in floor %d wait for a few seconds then close door' % floor)
        self.buttons[floor] = False
        self.current_floor = floor
        self.next_action()

    def select_floor(self, floor):
        self.buttons[floor] = True
        if self.state is 'stopped':
            self.next_action()

    # simulation
    def simulate_one_floor(self):
        print(" @floor %d " % self.current_floor)
        if self.state is 'up':
            if self.current_floor < self.floors - 1:
                self.arrived_floor(self.current_floor+1)

        elif self.state is 'down':
            if self.current_floor > 0:
                self.arrived_floor(self.current_floor-1)

        return self.state is not 'stopped'

    def simulate_until_stopped(self):
        while self.simulate_one_floor():
            pass

if __name__ == '__main__':
    elevator = Elevator(10)
    elevator.select_floor(5)
    elevator.simulate_until_stopped()
    elevator.select_floor(1)
    elevator.simulate_one_floor()
    elevator.select_floor(3)
    elevator.select_floor(6)
    elevator.simulate_until_stopped()

# Output
# $ python elevator.py
#  @floor 0
#  @floor 1
#  @floor 2
#  @floor 3
#  @floor 4
# open door in floor 5 wait for a few seconds then close door
#  @floor 5
#  @floor 4
# open door in floor 3 wait for a few seconds then close door
#  @floor 3
#  @floor 2
# open door in floor 1 wait for a few seconds then close door
#  @floor 1
#  @floor 2
#  @floor 3
#  @floor 4
#  @floor 5
# open door in floor 6 wait for a few seconds then close door