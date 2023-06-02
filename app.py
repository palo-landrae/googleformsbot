from bot import Bot
from data import Data

from time import sleep
from tqdm import tqdm
from multiprocessing import Pool
import threading

# VARIABLES
chrome_path = "/usr/bin/google-chrome"
chrome_driver_path = "/usr/bin/chromedriver"
form_test = "https://forms.gle/FbmPetg3DUA8vakbA"
properties = {}


def submit(args):
    index, data = args
    try:
        # Track the index of the data being processed
        bot = Bot(form_test, chrome_path, chrome_driver_path, properties)
        bot.last_row = 0  # Reset the counter for each submission
        bot.driver.get(bot.url)  # Load the form URL for each submission
        bot.set_data(data)
        sleep(1.5)  # Wait for the page to load
        bot.process_page(True)

        return index, True
    except Exception as e:
        # Handle the exception
        print(f"Error processing data at index {index}")
        print(f"Exception: {e}")
        return index, False


def update_progress(progress_bar):
    while True:
        progress_bar.refresh()
        sleep(1)


def main():
    max_processes = 6  # Set the maximum number of processes running simultaneously

    print("Welcome to Google Forms Bot!")
    n = int(input("How many times should I submit: "))
    data = Data(n).data

    success_list = []
    futures = []

    try:
        # Use tqdm to track the progress with multiprocessing support
        with tqdm(total=n, desc="Processing", ncols=80, unit="data") as pbar:
            # Start a thread to update the progress bar
            progress_thread = threading.Thread(
                target=update_progress, args=(pbar,), daemon=True
            )
            progress_thread.start()

            with Pool(processes=max_processes) as pool:
                for item in enumerate(data):
                    future = pool.apply_async(submit, (item,))
                    futures.append(future)

                for future in futures:
                    _, success = future.get()
                    success_list.append(success)
                    pbar.update(1)

                # Wait for all processes to complete
                pool.close()
                pool.join()

    except Exception as e:
        # Handle the exception
        print("An error occurred during data processing:")
        print(f"Exception: {e}")

    # Process the success_list to know which processes ran successfully
    successful_processes = [index for index,
                            success in enumerate(success_list) if success]
    print(
        f"Successful processes: {len(successful_processes)}/{n} --> ", successful_processes)


if __name__ == "__main__":
    main()
