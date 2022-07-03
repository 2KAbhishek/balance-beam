# Get started with interactive Python
import turtle


class Pen(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("white")
        self.penup()
        self.speed(0)


class Goal(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("green")
        self.penup()
        self.speed(5)


class Player(turtle.Turtle):
    def __init__(self):
        turtle.Turtle.__init__(self)
        self.shape("square")
        self.color("yellow")
        self.penup()
        self.speed(3)

    def check_collision(self, move_to_x, move_to_y, direction):
        if (move_to_x, move_to_y) in finish:
            print("You win!")
            with open('result.txt', 'w') as f:
                f.write('Won')
                f.close()
        if (move_to_x, move_to_y) not in walls:
            self.goto(move_to_x, move_to_y)
        else:
            print(f'You hit {direction} wall')
            with open('result.txt', 'w') as f:
                f.write('Fall')
                f.close()

    def go_up(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() + 24

        self.check_collision(move_to_x, move_to_y, "up")

    def go_down(self):
        move_to_x = player.xcor()
        move_to_y = player.ycor() - 24

        self.check_collision(move_to_x, move_to_y, "down")

    def go_right(self):
        move_to_x = player.xcor() + 24
        move_to_y = player.ycor()

        self.check_collision(move_to_x, move_to_y, "right")

    def go_left(self):
        move_to_x = player.xcor() - 24
        move_to_y = player.ycor()

        self.check_collision(move_to_x, move_to_y, "left")


# Create Level Setup Function
def setup_board(level):
    for y in range(len(level)):
        for x in range(len(level[y])):
            # Get the Character at each x,y coordinate
            character = level[y][x]
            # Calculate the screen x, y coordinates
            screen_x = -288 + (x * 24)
            screen_y = 288 - (y * 24)

            # Check if it is an X (representing a wall)
            if character == "Z":
                end.goto(screen_x, screen_y)
                end.stamp()
                finish.append((screen_x, screen_y))
            elif character == "X":
                pen.goto(screen_x, screen_y)
                pen.stamp()
                walls.append((screen_x, screen_y))
            elif character == "P":
                player.goto(screen_x, screen_y)


# create Levels list
levels = []

# define first level
level_1 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP                      X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X XXXXXXXXXXXXXXXXXXXXX X",
    "X                      ZX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_2 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP                      X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X XXXX XXXXXX XXXXXXXXX X",
    "X                      ZX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

level_3 = [
    "XXXXXXXXXXXXXXXXXXXXXXXXX",
    "XP                      X",
    "X X XXXXXXXXXXXXXXXXXXX X",
    "X X  XXXXXXXXXXXXXXXXXX X",
    "X XX  XXXXXXXXXXXXXXXXX X",
    "X XX       XXXXXXXXXXXX X",
    "X XXXXXXXX  XXXXXXXXXXX X",
    "X XXXXXXXXX  XXXXXXXXXX X",
    "X XXXXXXXXXX   XXXXXXXX X",
    "X XXXXXXX    XXXXXXXXXX X",
    "X XXXXXX  XXXXXXXXXXXXX X",
    "X                      ZX",
    "XXXXXXXXXXXXXXXXXXXXXXXXX"
]

levels.append(level_1)
levels.append(level_2)
levels.append(level_3)

# Add maze to mazes list
""" This is the Balancing beam game!
    You can play the  game using instruction and give options using yes or no
"""

print("--------------- Welcome to the Balance Beam! -----------------")
print("      Please follow the menu and enter your preference      ")

next_level = "no"
level = 0

quit_game = input("Do you want to quit? (yes or no): ")
if quit_game == "Yes" or quit_game == "yes":
    print("You have quit the game! Bye!")

while quit_game == "No" or quit_game == "no":
    print(""" ************ MENU ************* """)

    ins = input("Do you want to get instructions on screen? (yes or no): ")
    back = "no"
    if ins == "Yes" or ins == "yes":
        while back == "No" or back == "no":
            print(""" You can select difficulty of the game ("Easy" or "Hard").
                    Press Up,Down,Right and Left keys for moving.
                  The goal is to reach the end of the maze.""")

            back = input("Do you want to go back? (yes or no): ")

    play = input("Do you want to play? (yes or no): ")
    with open('result.txt', 'w') as f:
        f.write('Correct')
    f.close()
    if play == "Yes" or play == "yes":
        levelQ = input("Do you want harder difficulty? (yes or no): ")
        if levelQ == "Yes" or levelQ == "yes":
            level = 2

    wn = turtle.Screen()
    wn.setup(700, 700)
    wn.bgcolor("black")

    # Create class instances
    end = Goal()
    pen = Pen()
    player = Player()

    # Walls
    walls = []
    finish = []

    # Set up the level
    setup_board(levels[level])

    # Keyboard Binding
    turtle.listen()
    turtle.onkey(player.go_left, "Left")
    turtle.onkey(player.go_right, "Right")
    turtle.onkey(player.go_up, "Up")
    turtle.onkey(player.go_down, "Down")

    # Main Game Loop
    while True:
        # Update Screen
        f = open("result.txt", "r")
        contents = f.read()
        f.close()

        if contents == "Correct":
            wn.update()
        elif contents == "Fall":
            print("You lose!")
            break
        elif contents == "Won":
            print("You win!")
            break

    quit_game = input("Do you want to quit (yes or no): ")
