import time
import threading

class Bomb:

    def __init__(self, bomb_type, timer, password):
        if not isinstance(timer, int) or timer < 0:
            raise ValueError("Timer cannot be lower than 0, or a non integer value.")
        self.password = password
        self.bomb_type = bomb_type
        self.timer = timer
        self.activated = False
    def threads(self, thread, boom_type):
        if thread == "t1":
            thread_1 = threading.Thread(target=self.disarm)
            thread_1.start()
        if thread == "t2":
            thread_2 = threading.Thread(target=self.Timer_run, args=(boom_type,))
            thread_2.start()
        

    def Activate(self, boom_type):
        if not isinstance(boom_type, str):
            raise ValueError("Boom_type argument must be a string")
        self.activated = True
        print(f"The starting timer is {self.timer}")
        if self.timer > 0:
            print("The bomb is about to start ticking, do you want to attempt to disarm? Respond with Y/N")
            response = input()
        print("Bomb is activated")
        self.threads("t2", boom_type)
        if response == "Y":
            self.threads("t1", boom_type)
        elif response == "N":
            print("Why the hell- Okay whatever enjoy your doom.")
        else:
            print("You can't follow instructions can you? Whatever, bomb runs anyways and you cant disarm it.")     

    def Timer_run(self, boom_type):
        while self.activated and self.timer > 0:
            self.timer = self.timer - 1
            time.sleep(1)
        if self.timer == 0:
            print(boom_type)
            self.activated = False

    def disarm(self):
        if not self.activated:
            print("Bomb is not activated, can't disarm if there is nothing to disarm.")
            return
        while self.activated:
            print("To disarm this bomb, type the password below.")
            answer = input()
            if self.timer == 0:
                print("It's TOO LATE!")
                return
            if answer == self.password:
                self.activated = False
                print("Bomb successfully disarmed!")
            else:
                print("Wrong password, try again.")


saddam_bomb = Bomb("Firework", 30, "birds SUCK")

print(saddam_bomb.bomb_type, saddam_bomb.timer)
saddam_bomb.Activate("BIG BOOM")
