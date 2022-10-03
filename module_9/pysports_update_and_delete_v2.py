#https://github.com/Hadinski/csd-310

#importing
import mysql.connector
from mysql.connector import errorcode

#define the configuration for connecting to the database
config = {
    'user': 'pysports_user',
    'password': 'MySQL8IsGreat!',
    'host': 'localhost',
    'database': 'pysports',
    'raise_on_warnings': True
}

#define show_players
def show_players(cursor, title):
    #this method can be called repeatedly to print out all the players
    #define the query
    show_query = "SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id"

    #execute the query
    cursor.execute(show_query)

    #obtaining that BREAD!  Ahem, I mean, obtaining the query results
    players = cursor.fetchall()

    #printing the flavor line
    print('\n --{}--'.format(title))

    #printing all of the results
    for player in players:
        print('Player ID: {}'.format(player[0]),
            '\nFirst Name: {}'.format(player[1]),
            '\nLast Name: {}'.format(player[2]),
            '\nTeam Name: {}\n'.format(player[3]))


#Start try except finally block
#This is where most of the meat happens
try:
    #connecting to the database
    db = mysql.connector.connect(**config)
    print('\n Database user {} connected to MySQL on host {} with database {}'.format(config['user'], config['host'], config['database']))

    #define cursor
    cursor = db.cursor()

    #Inserting new record:
    #define addPlayerQuery
    addPlayerQuery = ("INSERT INTO player(first_name, last_name, team_id) VALUES(Smeagol, Shire Folk, 1)")
    #execute adding the new player
    cursor.execute(addPlayerQuery)
    #commit the changes
    db.commit()
    #call the show_players method to show all the players after insert
    show_players(cursor, 'DISPLAYING PLAYERS AFTER INSERT')

    #Updating new record:
    #define the update query for the new player record
    updatePlayerQuery = ("UPDATE player SET team_id = 2, first_name = 'Gollum', last_name = 'Ring Stealer' WHERE first_name = 'Smeagol'")
    #execute the update query
    cursor.execute(updatePlayerQuery)
    #show all player records again
    show_players(cursor, 'DISPLAYING PLAYERS AFTER UPDATE')

    #Deleting new record:
    #define the delete query for the new player record
    deletePlayerQuery = ("DELETE FROM player WHERE first_name = 'Gollum'")
    #execute delete player query
    cursor.execute(deletePlayerQuery)
    #show all player records again
    show_players(cursor, 'DISPLAYING PLAYERS AFTER DELETE')

    input("\n\n Press any key to continue...")

    

except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('The supplied username or password is invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('The specified database does not exist')

    else:
        print('Uh oh, stinky!  There was an error :(')

finally:
    db.close()