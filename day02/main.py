with open("input.txt", "r") as f:
    lines = f.read().splitlines()


def get_num_balls(line: str) -> tuple[int, int, int]:
    balls = line.split(",")

    red_balls = -1
    green_balls = -1
    blue_balls = -1

    for ball in balls:
        if ball[0] == " ":
            ball = ball[1:]

        ball = ball.split()

        num = int(ball[0])
        color = ball[1]

        if color == "red":
            red_balls = num

        elif color == "green":
            green_balls = num

        elif color == "blue":
            blue_balls = num

    return red_balls, green_balls, blue_balls


def is_possible(line: str, red: int, green: int, blue: int) -> bool:
    games = line.split(";")

    for game in games:
        red_balls, green_balls, blue_balls = get_num_balls(game)

        if red_balls > red or green_balls > green or blue_balls > blue:
            return False

    return True


total = 0

for line in lines:
    index = line.index(":")
    game_id = int(line[4:index])

    if is_possible(line[index + 2 :], 12, 13, 14):
        total += game_id

print(f"Total: {total}")