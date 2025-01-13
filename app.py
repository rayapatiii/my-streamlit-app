import streamlit as st
import snowflake.connector
import pandas as pd

# Snowflake connection details (use your actual Snowflake details here)
SNOWFLAKE_ACCOUNT = "kknhbdt-gw53127"
SNOWFLAKE_USER = "rayapatiii"
SNOWFLAKE_PASSWORD = "Balaruna123."
SNOWFLAKE_ROLE = "ACCOUNTADMIN"
SNOWFLAKE_WAREHOUSE = "COMPUTE_WH"
SNOWFLAKE_DATABASE = "FOOD_REVIEWS_DB"
SNOWFLAKE_SCHEMA = "REVIEWS_SCHEMA"

def create_snowflake_connection():
    return snowflake.connector.connect(
        user=SNOWFLAKE_USER,
        password=SNOWFLAKE_PASSWORD,
        account=SNOWFLAKE_ACCOUNT,
        warehouse=SNOWFLAKE_WAREHOUSE,
        database=SNOWFLAKE_DATABASE,
        schema=SNOWFLAKE_SCHEMA,
        role=SNOWFLAKE_ROLE
    )

def get_data_from_snowflake():
    conn = create_snowflake_connection()
    cursor = conn.cursor()
    
    # Query to fetch data from the table
    query = "SELECT * FROM AMAZON_FOOD_REVIEWS LIMIT 10;"
    cursor.execute(query)
    
    # Convert result to pandas dataframe
    data = cursor.fetchall()
    columns = [desc[0] for desc in cursor.description]
    df = pd.DataFrame(data, columns=columns)
    
    cursor.close()
    conn.close()
    
    return df

# Streamlit layout and functionality
st.title("Amazon Food Reviews")
st.write("Here are some of the latest reviews:")

# Fetch and display the data
df = get_data_from_snowflake()
st.write(df)
