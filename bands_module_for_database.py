import sqlite3
"""
First sqlite3 is imported.
All functions in this file follow the same procedure.
1 Create a connection to sqlite3.
2 Create a cursor to point to data in the file.
3 Use the cursor to execute a query of some sort.
4 Save the action undertaken (most functions not all)
5 Close the connection

The queries for each function:

The create_band_table() function:
Create a table called bands if it does not already exist. Then the type of data integer,float,text etc has to be listed
and in this case 'band' is the primary key which is the identifying column for this program.

The band_info() function:
Put these values into the 'bands' table. The reason for the formatting chosen is to avoid a sql injection attack. 
The first question mark is assigned to the band variable and so on.

The list_band_info() function:
Select everything for the bands table. Iterate over the data and assign the first key,value pair to the 0 index 
and so on(second key,value pair to the 1 index etc). Store the new assigned data in a variable and return that variable.

The listened_to_album_info() function:
Update the bands table by setting key 'heard' to 1 if the user input is equal to the key 'album'

The delete_band_info() function:
Delete the selected data from the bands table if the 'band' key is equal to the user input.

"""
def create_band_table():
    connection = sqlite3.connect('band_data.db')
    cursor = connection.cursor()
    cursor.execute('CREATE TABLE IF NOT EXISTS bands (band text primary key,album text,producer text,heard integer)')
    connection.commit()
    connection.close()

def band_info(band,album,producer):
    connection = sqlite3.connect('band_data.db')
    cursor = connection.cursor()
    cursor.execute('INSERT INTO bands Values(?,?,?,0)',(band,album,producer))
    connection.commit()
    connection.close()



def list_band_info():
    connection = sqlite3.connect('band_data.db')
    cursor = connection.cursor()
    cursor.execute('SELECT * FROM bands')
    bands = [{'band':row[0],'album':row[1],'producer':row[2],'heard':row[3]} for row in cursor.fetchall()]
    connection.close()
    return bands


def listened_to_album_info(user):
    connection = sqlite3.connect('band_data.db')
    cursor = connection.cursor()
    cursor.execute('UPDATE bands SET heard = 1 WHERE album = ?',(user,))
    connection.commit()
    connection.close()



def delete_band_info(user):
    connection = sqlite3.connect('band_data.db')
    cursor = connection.cursor()
    cursor.execute('DELETE FROM bands WHERE band = ?',(user,))
    connection.commit()
    connection.close()



