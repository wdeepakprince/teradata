# Pre-requisite:
# --------------

# Teradata Login & Environment is created
# Environment is actively running
# Review the same here : https://clearscape.teradata.com/dashboard
# Note: If the Environment is idle for 2 hours, environments are auto-showtdown by Teradata





# Import Tera Data SQL
# --------------------

import teradatasql as tds





# Initializing Variables
# ----------------------

# As provided in Teradata Login
tera_host = 'apollotest-b73bf6r3z4so77cp.env.clearscape.teradata.com'

# As provided in Teradata Login
tera_user = 'demo_user'

# As provided in Teradata Login
tera_password = 'Apollo@12345'

# Provide any sample DB name
tera_db = 'teradb_1'

# Provide any sample Table name
tera_table = 'teratable_1'

# Permanent Space for the DB as 10 MB ( same as 10000000 bytes)
tera_perm_space_byte = 10000000

# String to hold the SQL Queries
tera_sql_query=""





# Establish Connection with Teradata Host
# ---------------------------------------

try:
    con = tds.connect (
        
        host = tera_host,
        user = tera_user,
        password = tera_password
        
    )

    print("Connection established successfully!")
    print("\n")

except Exception as e:
    print("Connection NOT established!")
    print("\n")

    if "The UserId, Password or Account is invalid" in str(e):
        print("The UserId, Password or Account is invalid")
        print("\n")        
    else:
        print(f"An unexpected error occurred: {e}")
        print("\n")






# Create Cursor for the Connection
# ---------------------------------

try:
    cur=con.cursor()

except Exception as e:
    print("Cursor is NOT created!")
    print("\n")
    print(f"An unexpected error occurred: {e}")
    print("\n")





# Creating New DB
#----------------

# Create the SQL Query
# DBC is the Parent DB
tera_sql_query = f"""CREATE DATABASE {tera_db} FROM DBC AS PERMANENT = {tera_perm_space_byte} ;"""
print("SQL Query used:")
print(tera_sql_query)
print("\n")
    
# Execute the SQL Query

try:
    cur.execute(tera_sql_query)
    print(f"Database '{tera_db}' created successfully!")
    print("\n")

except Exception as e:
    # Fallback for anything else
    print("Database NOT created!")
    print("\n")

    if "already exists" in str(e):
        print("Database, user, or role already exists. Skipping creation.")
        print("\n")        
    else:
        print(f"An unexpected error occurred: {e}")
        print("\n")





# Viewing the DBs created so far
# ------------------------------

# Query the DBC.DatabasesV view to get a list of databases
# DBC.DatabasesV filters out databases you don't have access to.
# Create the SQL Query
tera_sql_query = f"""SELECT DatabaseName FROM DBC.DatabasesV ORDER BY 1"""
print("SQL Query used:")
print(tera_sql_query)
print("\n")
    
# Execute the SQL Query
try:
    cur.execute(tera_sql_query)
    print(f"Databases fetched successfully!")
    print("\n")
    
    # Print all DBs available in cursor
    for i in cur:
        print(i)

    print("\n")

except Exception as e:
    print("Database NOT fetched!")
    print("\n")
    print(f"An unexpected error occurred: {e}")
    print("\n")



