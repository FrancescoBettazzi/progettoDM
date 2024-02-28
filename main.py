# This is a sample Python script.

# Press Shift+F10 to execute it or replace it with your code.
# Press Double Shift to search everywhere for classes, files, tool windows, actions, and settings.
import server.connection as connection
import pandas as pd
from IPython.display import display

TABLE_NAME = "docs"
# TABLE_NAME = "canto"

def print_hi(name):
    # Use a breakpoint in the code line below to debug your script.
    print(f'Hi, {name}')  # Press Ctrl+F8 to toggle the breakpoint.


# Press the green button in the gutter to run the script.
if __name__ == '__main__':
    print_hi('PyCharm')
    conn = connection.create_db_connection()
    results = connection.read_query(conn, "SELECT * FROM " + TABLE_NAME)

    from_db = []
    for result in results:
        result = list(result)
        from_db.append(result)

    columns = ["codice", "titolo", "autore", "tonalita", "pagina", "quaderno", "note"]
    df = pd.DataFrame(from_db, columns=columns)
    display(df)

# See PyCharm help at https://www.jetbrains.com/help/pycharm/
