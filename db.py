import sqlite3
import os

class db:
    def __init__(self, db_name: str = 'databases/site.sqlite'):
        self.db = db_name
        self.conn = None

    def open_db(self):
        sqlite_file = self.db    # name of the sqlite database file
        # Connecting to the database file
        self.conn = sqlite3.connect(sqlite_file)
        c = self.conn.cursor()
        return c

    def commite_close_db(self):
        # Committing changes and closing the connection to the database file
        self.conn.commit()
        self.conn.close()

    def create_db(self):
        sqlite_file = self.db    # name of the sqlite database file

        os.makedirs(os.path.dirname(sqlite_file), exist_ok=True)

        table_name1 = 'helloWorld'  # name of the table to be created

        _columns = [('firstname', 'TEXT'), ('lastname', 'TEXT')]
        _columns.append( ('age', 'INT') ) # just to show
        columns = ''
        for x in _columns:
            if "" != columns:
                columns += ","
            columns += '"{name}" "{type}"'.format(name=x[0], type=x[1])

        c = self.open_db()

        # Creating a new SQLite table with 1 column
        c.execute("CREATE TABLE IF NOT EXISTS {table} ({columns})"\
                .format(table=table_name1, columns=columns))

        self.commite_close_db()


    def instert_row(self, table_name: str, columns: str, values: str):
        c = self.open_db()

        try:
            c.execute("INSERT INTO {tn} ({cl}) VALUES ({val})".\
                format(tn=table_name, cl=columns, val=values))
        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

        self.commite_close_db()

    def update_row(self, table_name: str, id: int, columns: str, values: str):
        c = self.open_db()

        try:
            c.execute("UPDATE {tn} SET '{cl}'='()'{val}' WHERE rowid=({idf})".\
                format(tn=table_name, idf=id, cl=columns, val=values))
        except sqlite3.IntegrityError:
            print('ERROR: ID already exists in PRIMARY KEY column {}'.format(id_column))

        self.commite_close_db()

    def set(self, table_name: str, _columns: list, _values: list, id: int = 0):
        columns = ""
        for x in _columns:
            if "" != columns:
                columns += ","
            columns += '"{column}"'.format(column=x)

        values = ""
        for x in _values:
            if "" != values:
                values += ","
            values += '"{value}"'.format(value=x)

        if 0 == id:
            self.instert_row(table_name, columns, values)
        else:
            self.update_row(table_name, id, columns, values)
