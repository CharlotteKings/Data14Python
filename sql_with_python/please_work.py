import pyodbc
# IN A CLASS
class NWProducts:
    def __init__(self):
        self.server = 'localhost,1433'
        self.database = 'Northwind'
        self.username = 'SA'
        self.password = 'Passw0rd2018'
        self.connection_string = "DRIVER={SQL Server};"
        self.connection_string += f"SERVER={self.server};"
        self.connection_string += f"DATABASE={self.database};"
        self.connection_string += f"UID={self.username};"
        self.connection_string += f"PWD={self.password}"
        self.docker_northwind = pyodbc.connect(self.connection_string)
        self.cursor = self.docker_northwind.cursor()

    def _sql_query(self, sql_query):
        return self.cursor.execute(sql_query)

    def average_unit_price(self):
        records = self._sql_query("SELECT * FROM Products;")
        unit_price = []
        for row in records:
            unit_price.append(row.UnitPrice)
        avg_unit_price = sum(unit_price)/len(unit_price)
        return avg_unit_price

# TEST THE CLASS CODE - so this code doesnt run when imported elsewhere 
if __name__ == __main__:
    new_query = NWProducts()
    print(new_query.average_unit_price())

#cursor.execute("SELECT * FROM Products;")
# row = cursor.fetchmany(5)  # .fetchone() = brings back one line at a time, printing again returns next line. No more lines returns None
#                            # .fetchall() = bring all lines
# print(row)


# for row in cursor:  # Iterate through rows. Better.
#     print(row.UnitPrice)      # row.<column name> = returns column
                                # Can print more than one at a time

# # WAY OF BREAKING LOOP
# while True:
#     record = cursor.fetchone()
#     if record is None:
#         break
#     else:
#         print(record)
#         print(record.UnitPrice)

# # SLIGHTLY MORE COMPLICATED QUERIES?
# query = """
#         < write your query
#         over many lines>
#         """
# cursor.execute(query)