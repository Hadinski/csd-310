#https://github.com/Hadinski/csd-310

#importing
from select import select
import mysql.connector
from mysql.connector import errorcode

#connecting to pysports database
config = {
    'user': 'pysports_user',
    'password': 'MySQL8IsGreat!',
    'host': 'localhost',
    'database': 'pysports',
    'raise_on_warnings': True
}

#Start of try except finally block
try:
    db = mysql.connector.connect(**config)

    print('\n Database user {} connected to MySQL on host {} with database {}'.format(config['user'], 
        config['host'], config['database']))

    #queries
    query = 'SELECT player_id, first_name, last_name, team_name FROM player INNER JOIN team ON player.team_id = team.team_id;'

    #setup for printing player query output
    cursor = db.cursor()
    cursor.execute(query)
    players = cursor.fetchall()

    #printing player query output
    print('-- DISPLAYING PLAYER RECORDS --')
    for player in players:
        print('Player ID: {}'.format(player[0]),
            '\nFirst Name: {}'.format(player[1]),
            '\nLast Name: {}'.format(player[2]),
            '\nTeam ID: {}\n'.format(player[3]))

    print('\n Press any key to continue...')




#handling any potential errors
except mysql.connector.Error as err:
    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('The supplied username or password is invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('The specified database does not exist')

    else:
        print('Uh oh, stinky!  There was an error :(')

#finishing things off
finally:
    db.close()

#end of program