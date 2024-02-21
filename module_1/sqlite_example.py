#Step 0 - import sqlite3 (comes with python library)
import sqlite3
import queries as q

#step 1 - connect to the database
#triple check spelling of database filename = will not throw error but create new file
connection =sqlite3.connect('rpg_db.sqlite3')

#step2 -make the cursor
cursor = connection.cursor()

#step 3 - write a query
#query = 'SELECT character_id, name FROM charactercreator_character;' - changed this as now using queries tab for all queries

#step 4 - execute query on cursor and fetch results - 'pulling the results'
#results = cursor.execute(query).fetchall() -changed this to below as moved queries to queries tab
results = cursor.execute(q.SELECT_ALL).fetchall()

if __name__ == '__main__':
    print(results[:5])
