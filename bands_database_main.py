import sqlite3

from utils import bands_final_database

"""
This main file is nearly identical to the main file called 'bands_text_file_main.py' located in my repository called 
Python-storing-data-in-a-text-file on Github which I explain everything on the page in depth. The main difference here 
is that the data is now being stored in a database and not in a txt file. Menu () is the main function here which 
directs the program based on the user's input. Each function inside the while loop achieves some small tasks like asking 
the users for basic input. This basic input gets past over to one of the functions in bands_database.py where the bulk 
of the logic is completed for the program.
"""
USER_INPUT = """
------------------------------------------------------------------------
Enter:
- 'a' to add a new band
- 'l' to list all the bands
- 'm' to mark an album as listened to
- 'd' to delete a band and it's info
- 'q' to quit the program
: 
------------------------------------------------------------------------
"""


# --------------------------------------------------START OF FUNCTIONS--------------------------------------------------
def menu():
    user_input = input(USER_INPUT).lower()
    bands_final_database.create_band_table()
    while user_input != 'q':
        if user_input == 'a':
            add_band()

        elif user_input == 'l':
            show_band()

        elif user_input == 'm':
            heard_album()

        elif user_input == 'd':
            delete_band()
        else:

            print("Not valid try again")
        user_input = input(USER_INPUT).lower()


def add_band():
    try:
        band = input("Enter a band ").lower()
        album = input("Enter an album ").lower()
        producer = input("Enter a producer ").lower()

        bands_final_database.band_info(band, album, producer)
    except sqlite3.IntegrityError:
        print("------------------------------------------------------------------------")
        print("\nThat band has already been added try another band.\n")
        print("------------------------------------------------------------------------")


def show_band():
    bands = bands_final_database.list_band_info()
    for band in bands:
        if band['heard'] == 0:
            read = "no"
        else:
            read = "yes"
        print(
            f"Band: {band['band']},Album: {band['album']},"
            f"Producer: {band['producer']},listened to: {read}")


def heard_album():
    user_album = input("Enter an album to mark as listened to ").lower()
    bands_final_database.listened_to_album_info(user_album)


def delete_band():
    band = input("Enter a band to delete ").lower()
    bands_final_database.delete_band_info(band)


# --------------------------------------------------END OF FUNCTIONS----------------------------------------------------
menu()
