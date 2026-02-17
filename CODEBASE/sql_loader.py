#function to create table automatically
def create_table(df, table_name):
    #save column names to list
    dataset_columns = df.columns

    #create table script and table name
    sql_create_name_beg = f'CREATE TABLE {table_name} (\n'

    #datatype
    sql_varchar = 'VARCHAR(500)'
    
    #columns with data types
    column_defs = []

    #loop the column list
    for i in dataset_columns:
        col_names = f'{i.strip()} {sql_varchar}'
        column_defs.append(col_names)

    #join the column names with comma
    sql_columns = ",\n".join(column_defs)

    #concat all to make create table script
    create_sql = f"""{sql_create_name_beg}{sql_columns});
    """
    return create_sql.strip()