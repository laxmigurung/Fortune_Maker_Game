import time

start_time = time.time()


def get_time_elapsed():
    stopper = input("Press enter to stop the game")
    end_time = time.time()
    time_duration = int(end_time - start_time)
    print(f"{time_duration} seconds")


get_time_elapsed()
