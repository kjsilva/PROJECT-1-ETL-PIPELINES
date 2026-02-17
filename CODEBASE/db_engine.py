from sqlalchemy import create_engine, text
from db_cred import dBCred
getpass = dBCred()

#importing the db credentials
env_vars = {}
with open(r'D:\desktop\Projects\PROJECT_7_ETL_WITH_API\TASK1_PYTHON_SCRAPER\CODEBASE\enccred.env', 'r') as cred:
    for line in cred:
        line = line.strip()

        key, value = line.split('=', 1)
        env_vars[key.strip()] = value.strip()

def my_engine():
    #decrypted password
    enc_pass = env_vars['encrypted_pass']
    dec_key = getpass.key_decryptor(env_vars)
    dec_pass = getpass.decryptor(enc_pass, dec_key)
    dec_pass = dec_pass.decode()

    user = env_vars['user']
    #print(user)
    password = dec_pass
    #print(password)
    host = env_vars['host']
    #print(host)
    port = env_vars['port']
    #print(port)
    database = env_vars['database']
    #print(database)

    engine = create_engine(
        f'mysql+pymysql://{user}:{password}@{host}:{port}/{database}',
        future=True
    )
    return engine


if __name__ == '__main__':
    my_engine()