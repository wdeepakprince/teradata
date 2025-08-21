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





# Insert Rows in tables
# ---------------------

# Create the SQL Query
tera_sql_query = f"""
    INSERT INTO {tera_db}.{tera_table} (ID, EmpName, Salary, JoiningDate)
    VALUES (101, 'Deepak', 12000, '2025-01-01')
"""
print("SQL Query used:")
print(tera_sql_query)

# Execute the SQL Query
try:
    cur.execute(tera_sql_query)
    print(f"Rows inserted successfully!")
    print("\n")
    
except Exception as e:
    print("Rows NOT inserted!")
    print("\n")
    print(f"An unexpected error occurred: {e}")
    print("\n")





# View inserted Rows
# ------------------

# Create the SQL Query
tera_sql_query = f"""
    SELECT * FROM {tera_db}.{tera_table}
"""
print("SQL Query used:")
print(tera_sql_query)

# Execute the SQL Query
try:
    cur.execute(tera_sql_query)
    print(f"Rows retrieved successfully!")
    print("\n")
    
    # Print all rows available in cursor
    for i in cur:
        print(i)
    print("\n")

except Exception as e:
    print("Rows NOT retrieved!")
    print("\n")
    print(f"An unexpected error occurred: {e}")
    print("\n")
    



# Update Rows in tables
# ---------------------

# Create the SQL Query
tera_sql_query = f"""
    UPDATE {tera_db}.{tera_table}
    SET Salary = Salary + 5000
    WHERE ID = 101;
"""
# update happens for all rows matching the above criteria

print("SQL Query used:")
print(tera_sql_query)

# Execute the SQL Query
try:
    cur.execute(tera_sql_query)
    print(f"Row updated successfully!")
    print("\n")
    
except Exception as e:
    print("Row was NOT updated!")
    print("\n")
    print(f"An unexpected error occurred: {e}")
    print("\n")





# Delete Rows in tables
# ---------------------

# Create the SQL Query
tera_sql_query = f"""
    DELETE FROM {tera_db}.{tera_table}
    WHERE ID = 101;
"""
# update happens for all rows matching the above criteria

print("SQL Query used:")
print(tera_sql_query)

# Execute the SQL Query
try:
    cur.execute(tera_sql_query)
    print(f"Row(s) deleted successfully!")
    print("\n")
    
except Exception as e:
    print("Row(s) NOT deleted!")
    print("\n")
    print(f"An unexpected error occurred: {e}")
    print("\n")




# View Rows
# ----------

# Create the SQL Query
tera_sql_query = f"""
    SELECT * FROM {tera_db}.{tera_table}
"""
print("SQL Query used:")
print(tera_sql_query)

# Execute the SQL Query
try:
    cur.execute(tera_sql_query)
    print(f"Rows retrieved successfully!")
    print("\n")
    
    # Print all rows available in cursor
    for i in cur:
        print(i)
    print("\n")
    
except Exception as e:
    print("Rows NOT retrieved!")
    print("\n")
    print(f"An unexpected error occurred: {e}")
    print("\n")
