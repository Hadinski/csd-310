#Made by Haydn Hurst
#https://github.com/Hadinski/csd-310/tree/main/module_12
#import statements
import sys
import mysql.connector
from mysql.connector import errorcode

#configuration object
config = {
    "user": "whatabook_user",
    "password": "MySQL8IsGreat!",
    "host": "127.0.0.1",
    "database": "whatabook",
    "raise_on_warnings": True
}

#defining the function that shows the main menu and gets the correspoonding input
def viewMenu():

    #printing flair text and menu options
    print('\n -- Main Menu -- \n')
    print(' 1: View our books\n 2: View our store locations\n 3: View your account\n 4: Exit the program')

    #try/catch block for getting the user input
    try:
        #getting the input
        choiceInput = int(input('\nPlease select an option. '))

        #returning the input
        return choiceInput

    #handling bad user input
    except ValueError:
        print('\nInvalid input, please try again. ')
        sys.exit(0)           

#defining the function that displays all the books that the store has
def viewBooks(_cursor):

    #executing the query
    _cursor.execute('SELECT book_id, book_name, author, details FROM book')

    #getting query output
    books = _cursor.fetchall()

    #printing flair text
    print('\n-- Displaying our books --')

    #outputting query results
    for book in books:
        print('\nBook Name: {}'.format(book[1]),
              '\nBook ID: {}'.format(book[0]),
              '\nAuthor Name: {}'.format(book[2]),
              '\nBook Details: {}'.format(book[3]))

#defining the function that displays the store locations
def viewLocations(_cursor):

    #executing query
    _cursor.execute("SELECT store_id, locale FROM store")

    #getting wuery output
    storeLocations = _cursor.fetchall()

    #printing flair text
    print('\n-- Our store locations --')

    #outputting query results
    for store in storeLocations:
        print('\nStore Location: {}'.format(store[1]),
              '\nStore ID: {}'.format(store[0]))

#defining the function that determines which user is using the program
def authorizeUser():

    #try/catch block for getting the user input
    try:
        #getting the input
        user_id = int(input('\nPlease enter your customer ID (currently 1, 2, or 3): '))

        #controlling user input to make sure only numbers 1-3 are inputted
        if user_id < 1 or user_id > 3:
            print("\nInvalid customer number. \n")
            sys.exit(0)
        
        #returning the input
        return user_id

    #handling bad user input
    except ValueError:
        print('\nInvalid number. ')
        sys.exit(0)

#defining the function that displays the account menu and gets the corresponding input
def viewAccountMenu():

    #printing flair text and account menu options
    print('\n-- Account Menu --')
    print('\n 1: Your wishlist\n 2: Add to your wishlist\n 3: Back to main menu')

    #try/catch block for getting the user input
    try:
        #getting the input
        accountChoiceInput = int(input('\nPlease select an option.'))
        
        #returning the input
        return accountChoiceInput

    #handling bad user input
    except ValueError:
        print('\nInvalid input, please try again. ')
        sys.exit(0)

#defining the function that displaysthe user's wishlist
def viewWishlist(_cursor, _user_id):

    #defining the query
    query = ('SELECT user.user_id, user.first_name, user.last_name, book.book_id, book.book_name, book.author ' +
             'FROM wishlist ' +
             'INNER JOIN user ON wishlist.user_id = user.user_id ' +
             'INNER JOIN book ON wishlist.book_id = book.book_id ' +
             'WHERE user.user_id = {}'.format(_user_id))

    #executing the query
    _cursor.execute
    
    #getting the query output
    wishlist = _cursor.fetchall()
    print('\n-- Items in your wishlist --')

    #outputting the results
    for book in wishlist:
        print('\nBook Name: {}'.format(book[4]),
              '\nAuthor Name: {}\n'.format(book[5]),
              '\nBook ID: {}\n'.format(book[3]))

#defining the function that displays all the books available to be added to the user's wishlist
def viewBooksToAdd(_cursor, _user_id):

    #defining the query
    query = ('SELECT book_id, book_name, author, details '
             'FROM book '
             'WHERE book_id NOT IN (SELECT book_id FROM wishlist WHERE user_id = {})'.format(_user_id))
    
    #executing the query
    _cursor.execute(query)

    #getting the query output
    booksToAdd = _cursor.fetchall()

    #printing flair text
    print('\n-- Books available to add --')

    #outputting query results
    for book in booksToAdd:
        print('\nBook Name: {}'.format(book[1]),
              '\nBook ID: {}'.format(book[0]))

#defining the function that adds the desired book to the user's wishlist
def addToWishlist(_cursor, _user_id, _book_id):
    _cursor.execute('INSERT INTO wishlist(user_id, book_id) VALUES({}, {})'.format(_user_id, _book_id))

#starting the try/except block that executes everything
try:
    #connecting to the whatabook database
    db = mysql.connector.connect(**config)

    #defining the cursor for the MySQL queries
    cursor = db.cursor() 

    #printing the opening text flair
    print('\nWelcome to the WhatABook Application! \n')

    #displaying the main menu for the first time
    userChoice = viewMenu()

    #creating a while loop that will allow the user to keep performing actions until they exit the program
    while userChoice != 4:

        #calls the viewBooks function to display all books
        if userChoice == 1:
            viewBooks(cursor)

        #calls the viewLocations function to display the store locations
        if userChoice == 2:
            viewLocations(cursor)

        #calls the authorizeUser function to get the user ID
        #also displays the user account menu for the first time
        if userChoice == 3:
            tempUserID = authorizeUser()
            userAccountChoice = viewAccountMenu()

            #defining a while loop that allows the user to keep performing actions until they want to return to the main menu
            while userAccountChoice != 3:
                
                #calls the viewWishlist function to display the user's wishlist
                if userAccountChoice == 1:
                    viewWishlist(cursor, tempUserID)

                #calls the viewBooksToAdd function to display the books availble for adding to the user's wishlist
                if userAccountChoice == 2:
                    viewBooksToAdd(cursor, tempUserID)

                    #getting the user input
                    book_id = int(input('\nPlease enter the ID of the book you would like to add. '))

                    addToWishlist(cursor, tempUserID, book_id)

                    #committing the changes
                    db.commit()

                    #printing the output
                    print('\nBook with ID {} has been added to your wishlist. '.format(book_id))

                #controlling user input to make sure only numbers 1-4 are inputted
                if userAccountChoice < 1 or userAccountChoice > 3:
                    print('\nInvalid option, please try again. ')

                userAccountChoice = viewAccountMenu()

        #controlling user input to make sure only numbers 1-4 are inputted
        if userChoice < 1 or userChoice > 4:
            print('\nInvalid option, please try again. ') 

        userChoice = viewMenu()
    #printing end of program text flair
    print('\n\n-- Program ended --')    


#Handling any potential errors
except mysql.connector.Error as err:

    if err.errno == errorcode.ER_ACCESS_DENIED_ERROR:
        print('The supplied username or password are invalid')

    elif err.errno == errorcode.ER_BAD_DB_ERROR:
        print('The specified database does not exist')

    else:
        print('Uh oh, there was an error:\n', err)

finally:
   #closing the MySQL connection

    db.close()