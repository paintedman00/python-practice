# 2048.py 🕹️

# Let's import our logic.py file where all the magic happens! ✨
import logic

# This is like the main entrance to our game 🚪
if __name__ == '__main__':

    # Time to start the game and create the initial board 🏁
    mat = logic.start_game()

    # Let's keep playing until the game is over! 🔁
    while True:

        # Ask the player for their next move 👾
        x = input("Press the command (W/A/S/D): ")

        # If the player wants to move UP ⬆️
        if x.lower() == 'w':
            mat, flag = logic.move_up(mat)
            status = logic.get_current_state(mat)
            print(status)  # Let's tell the player what's happening 🗣️

            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)  # Drop a new 2 on the board! 🎲
            else:
                break  # Game over, time to stop! 🛑

        # If the player wants to move DOWN ⬇️
        elif x.lower() == 's':
            mat, flag = logic.move_down(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
            else:
                break

        # If the player wants to move LEFT ⬅️
        elif x.lower() == 'a':
            mat, flag = logic.move_left(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
            else:
                break

        # If the player wants to move RIGHT ➡️
        elif x.lower() == 'd':
            mat, flag = logic.move_right(mat)
            status = logic.get_current_state(mat)
            print(status)
            if status == 'GAME NOT OVER':
                logic.add_new_2(mat)
            else:
                break

        # Oops! The player pressed something weird 🤔
        else:
            print("Invalid Key Pressed! Please use W/A/S/D only. 🚫")

        # Show the current state of the board after every move 🧩
        print(mat)