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



