steps = 0

while steps < 10000:
    command = input()
    if command == "Going home":
        steps_to_home = int(input())
        steps += steps_to_home
        break

    steps += int(command)

diff = abs(steps - 10000)
if steps >= 10000:
    print("Goal reached! Good job!" )
    print(f"{diff} steps over the goal!")
else:
    print(f"{diff} more steps to reach goal.")
