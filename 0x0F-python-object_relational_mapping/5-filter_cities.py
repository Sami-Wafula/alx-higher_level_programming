#!/usr/bin/python3
'''script that takes state as an arg and lists all the cities of the arg
'''
import sys
import MySQLdb as b


if __name__ == '__main__':
    if len(sys.argv) >= 5:
        db_connection = b.connect(
            host='localhost',
            username=sys.argv[1],
            password=sys.argv[2],
            db=sys.argv[3],
        )
        cursor = db_connection.cursor()
        state = sys.argv[4]
        cursor.execute(''SELECT cities.name FROM cities' +
            ' INNER JOIN states ON cities.state_id = states.id' +
            ' WHERE CAST(states.name AS BINARY) = %s' +
            ' ORDER BY cities.id ASC;',
            [state_name]'
            )
        result = cursor.fetchall()
        for result in results:
            print(result)
        db.connection.close()
