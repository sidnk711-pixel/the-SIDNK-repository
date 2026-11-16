import random
import re
hour_clock = str(random.randint(0, 23))
minute_clock = random.randint(0,59)
lives = 8
if minute_clock < 10:
    minute_clock = "0" + str(minute_clock)
clock = f"{hour_clock}:{minute_clock}"
mil_time = int(hour_clock + str(minute_clock))
def guess():
    clock_validate = re.fullmatch(r"\d+:\d+", answer)
    if clock_validate == None:
        raise ValueError("Input must be in clock format, such as 13:43, or 3:06")
print("Now type your clock time below, use H:MM format or HH:MM format if hours is double digits.")    

guessed = False
while not guessed and lives > 0:
    print(f"Lives left: {lives}")
    answer = input()
    guess()
    if answer == clock:
        print(f"You got the correct time with {lives} life/lives left, congratulations!")
        guessed = True
    answer_split = answer.split(":")
    h, m = answer_split
    military_time_answer = int(h + m)
  
    if military_time_answer > mil_time:
        print("Too ahead of the real answer! You've lost a life, try again.")
        lives = lives - 1
    if military_time_answer < mil_time:
        print("Too below the real answer! You've lost a life, try again.")
        lives = lives - 1
if not guessed:
    print("You lost all of your lives, game over...")
